@author Laurent Krishnathas
@version 2017

# Serverless aws lambda

This is an implementation of python based aws lambda to loop over all regions and add
tags to ec2 instances.

Tools used are:
- serverless framework
- make
- awscli
- docker

Everything dockerized to avoid any local dependancies to specific OS, Make will build a docker image to run 
serverless commands. Not tested on windows yet, works ok on MacOs

Make target to build, deploy and run the function:
-    **make serverless_invokeLocal**    
-    **make serverless_deploy** 
-    **make serverless_invoke**      
-    **make serverless_logs** 
-    **make serverless_remove** 

    
serverless commands for reference:
```
$ Serverless create --template aws-python --path ec2TagPyService    #create service
$ workon workon_name
$ pip install -r requirement.txt
$ Serverless invoke local -f hello          #function name is defined in serverless.yml
$ Serverless plugin install -n serverless-python-requirements
$ Serverless deploy                         # automatically cteate a zip file          
$ Serverless invoke -f hello
```        
    
**WARNING**: 
* boto3 is included in lambda automatically, the serverless-python-requirements plugin was 
a bit bloated, created a 7m zip file, useful if other python import modules are used    

* by default timeout was 6s, need to increase in serverless yml file


Iam permission needed to run serverless: TODO

- "cloudformation:Describe*",
- "cloudformation:List*",
- "cloudformation:Get*",
- "cloudformation:PreviewStackUpdate"
- "cloudformation:CreateStack",
- "cloudformation:UpdateStack",
- "cloudformation:DeleteStack"
- "lambda:AddPermission",
- "lambda:CreateAlias",
- "lambda:DeleteFunction",
- "lambda:InvokeFunction",
- "lambda:PublishVersion",
- "lambda:RemovePermission",
- "lambda:Update*"
- "apigateway:*"
- "iam:PassRole"
 
 