import json
import boto3

def update_all_regions():
    print("connecting to default region ...")
    ec2 = boto3.client('ec2')

    print("getting regions list ...")
    ec2_regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
    for region in ec2_regions:
        update_region(region)

def update_region(region):
    print("connecting to "+region)
    ec2 = boto3.client('ec2',  region_name=region)
    response = ec2.describe_instances()
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instanceId=instance["InstanceId"]
            print(instanceId)
            mytags = [
                {
                    "Key" : "Region",
                    "Value" : region
                },
                {
                    "Key" : "State",
                    "Value" : instance["State"]["Name"]
                },
                {
                    "Key" : "Team",
                    "Value" : "xteam2"
                }
            ]
            print("creating tags for "+instanceId)
            ec2.create_tags(
                Resources=[instanceId],
                Tags=mytags
            )

def hello(event, context):
    update_all_regions()

    msg="test wtf"

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully! s3 list :"+msg,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """








