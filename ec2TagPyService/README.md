# @author Laurent Krishnathas
# @version 2017


# serverless-ec2-tagging
    
Project dockerized to avoid local dependancy on tools like npm, serverless, python, boto3
    make serverless_invokeLocal
    make serverless_invoke
    make serverless_deploy
    make serverless_remove

    
serverless commands
serverless:
    sls create --template aws-python --path ec2TagPyService     #create service
    workon workon_name
    pip install -r requirement.txt
    sls invoke local -f hello                                   #function name is defined in serverless.yml
    sls plugin install -n serverless-python-requirements
    sls deploy                                                  #automatically cteate a zip file
    sls invoke -f hello
        
    
    
WARNING: boto3 is included in lambda automatically    


