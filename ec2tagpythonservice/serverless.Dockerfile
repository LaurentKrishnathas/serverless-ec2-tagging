# @author Laurent Krishnathas
# @version 2017/11/22

FROM node:9.2.0
LABEL maintainer="Laurent Krishnathas <lk@dotmatics.com>"
LABEL description="serverless framework with python dependancy and awscli to test local and deploy remote"

RUN npm install -g serverless@1.24.1  && \
    apt-get update && \
    apt-get install python-dev -y && \
    apt-get clean && \
    curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    pip install awscli boto3  && \
    mkdir /code

WORKDIR /code
