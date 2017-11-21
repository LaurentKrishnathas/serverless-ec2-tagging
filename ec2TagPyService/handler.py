# this block needed bby
try:
    import unzip_requirements
except ImportError:
    pass


import json
import boto3

def hello(event, context):
    s3 = boto3.resource('s3')
    s = ""


    for bucket in s3.buckets.all():
        print(bucket.name)

        s+=bucket.name
        s+=","

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully! s3 list :"+s,
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








