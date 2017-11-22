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

SERVICE=hello
SERVERLESS=docker run -it -v $(PWD):/code -v $(HOME)/.aws:/root/.aws $(image_name):$(image_version) serverless


#hello_script:
#	$(FUNC) test
#
docker_build:
	docker build -t $(image_name):$(image_version) --rm=false -f $(dockerfile) .

serverless_invokeLocal: docker_build
	$(SERVERLESS) invoke local -f $(SERVICE) --verbose

serverless_invoke: docker_build
	$(SERVERLESS) invoke -f $(SERVICE) --verbose

serverless_deploy: docker_build
	$(SERVERLESS) deploy --verbose

serverless_remove: docker_build
	$(SERVERLESS) remove --verbose



































