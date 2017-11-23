# @author Laurent Krishnathas
# @version 2017

import json
import boto3

def handle(event, context):
    version="2017-11-23_09h50"
    print("main version "+version)

    msg=update_all_regions()


    body = {
        "message": "Go Serverless version "+str(version)+"! Your function executed successfully! "+str(msg),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    print("function executed sucessfully")
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def update_all_regions():
    print("connecting to default region ...")
    ec2 = boto3.client('ec2')

    print("getting regions list ...")
    ec2_regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
    print(str(len(ec2_regions))+" regions found")
    count=0
    for region in ec2_regions:
        try:
            print("connecting to "+region+" ...")
            count=count+update_region(region)
            print("done "+region+" ...")
        except Exception as e: print(e)
    msg="updated "+str(count)+" in "+ str(len(ec2_regions))+" regions."


def update_region(region):
    ec2 = boto3.client('ec2',  region_name=region)
    count=0
    print("connected to "+region)
    response = ec2.describe_instances()
    print("test 0")
    size=len(response["Reservations"])
    print("test 1")
    print(str(size)+" instances found.")
    print("test 2")
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            count=count+1
            instanceId=instance["InstanceId"]
            mytags = [
                {
                    "Key" : "Region",
                    "Value" : region
                },
                {
                    "Key" : "State",
                    "Value" : instance["State"]["Name"]
                }
            ]
            print("creating tags for "+instanceId)
            ec2.create_tags(
                Resources=[instanceId],
                Tags=mytags
            )
    return count

