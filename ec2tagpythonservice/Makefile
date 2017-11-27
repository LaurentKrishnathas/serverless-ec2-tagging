# @author Laurent Krishnathas
# @version 2017/10/19

container_name=serverless
image_name=laurent_krishnathas/serverless
image_version=snapshot
dockerfile=serverless.Dockerfile

#FUNC=makefile.sh

# Need to keep the following upto date with serverless.yml file
SERVICE=serverless-ec2tagpythonservice
FUNCTION=create_tags
STAGE=dev

DEBUG_ENV=
ifeq ($(DEBUG),true)
   DEBUG_ENV=-e SLS_DEBUG=*
endif

DOCKER_RUN_CMD=docker run -it -v $(PWD):/code -v $(HOME)/.aws_test-tf:/root/.aws $(DEBUG_ENV) $(image_name):$(image_version)
SERVERLESS=$(DOCKER_RUN_CMD) serverless

docker_build:
	docker build -t $(image_name):$(image_version) --rm=false -f $(dockerfile) .

serverless_invokeLocal: docker_build
	$(SERVERLESS) invoke local -f $(FUNCTION) --verbose

serverless_deploy: docker_build
	$(SERVERLESS) deploy --verbose

serverless_invoke: docker_build
	$(SERVERLESS) invoke -f $(FUNCTION) --verbose

serverless_logs:
	$(SERVERLESS) logs -f $(FUNCTION) --tail

serverless_remove: docker_build
	$(SERVERLESS) remove --verbose

#serverless contains a log command so no need to do complicated aws cli based script, good to keep for reference
# following var are just for reference
#LOG_GROUP_NAME=/aws/lambda/$(SERVICE)-$(STAGE)-$(FUNCTION)
#AWS_GET_STREAM_NAME=$(DOCKER_RUN_CMD) aws logs describe-log-streams --log-group-name $(LOG_GROUP_NAME) --order-by LastEventTime | jq -r ".logStreams[-1].logStreamName"
#STREAM_NAME=$(shell $(AWS_GET_STREAM_NAME) )
#
#serverless_last_logs:
#	echo printing for group: $(LOG_GROUP_NAME), stream: $(STREAM_NAME)
#	$(DOCKER_RUN_CMD) aws logs get-log-events --log-group-name  $(LOG_GROUP_NAME)  --log-stream-name `$(AWS_GET_STREAM_NAME)` --output=text
#	echo group: $(LOG_GROUP_NAME), stream: $(STREAM_NAME)
#

















