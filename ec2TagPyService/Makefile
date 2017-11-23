# @author Laurent Krishnathas
# @version 2017/10/19

# common variables
container_name=serverless
image_name=laurent_krishnathas/serverless

#gitversion=`git rev-parse --short HEAD`
image_version=snapshot
dockerfile=serverless.Dockerfile
created=""

FUNC=makefile.sh

SERVICE=ec2tagging
SERVERLESS=docker run -it -v $(PWD):/code -v $(HOME)/.aws:/root/.aws $(image_name):$(image_version) serverless
SERVERLESS_DEBUG=docker run -it -v $(PWD):/code -v $(HOME)/.aws:/root/.aws -e SLS_DEBUG=* $(image_name):$(image_version) serverless


LOG_GROUP_NAME=/aws/lambda/ec2tagpyservice-dev-ec2tagging

AWS_GET_STREAM_NAME=aws logs describe-log-streams --log-group-name $(LOG_GROUP_NAME) --order-by LastEventTime | jq -r ".logStreams[-1].logStreamName"
STREAM_NAME=$(shell $(AWS_GET_STREAM_NAME) )

#hello_script:
#	$(FUNC) test
#
docker_build:
	docker build -t $(image_name):$(image_version) --rm=false -f $(dockerfile) .

serverless_invokeLocal: docker_build
	$(SERVERLESS) invoke local -f $(SERVICE) --verbose

serverless_invoke: docker_build
	$(SERVERLESS) invoke -f $(SERVICE) --verbose

serverless_invoke_debug: docker_build
	$(SERVERLESS_DEBUG) invoke -f $(SERVICE) --verbose

serverless_deploy: docker_build
	$(SERVERLESS) deploy --verbose

serverless_remove: docker_build
	$(SERVERLESS) remove --verbose



logs_group:
	aws logs describe-log-groups --log-group-name-prefix $(LOG_GROUP_NAME) --output=text

logs:
	echo printing for group: $(LOG_GROUP_NAME), stream: $(STREAM_NAME)
	aws logs get-log-events --log-group-name  $(LOG_GROUP_NAME)  --log-stream-name `$(AWS_GET_STREAM_NAME)` --output=text
	echo group: $(LOG_GROUP_NAME), stream: $(STREAM_NAME)

























