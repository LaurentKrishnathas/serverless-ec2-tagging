# @author Laurent Krishnathas
# @version 2017


# serverless-ec2-tagging

serverless:
    sls create --template aws-python --path ec2TagPyService     #create service
    workon workon_name
    pip install -r requirement.txt
    sls invoke local -f hello                                   #function name is defined in serverless.yml
    sls plugin install -n serverless-python-requirements
    sls deploy                                                  #automatically cteate a zip file
    sls invoke -f hello


plugin used to package python external dependancy