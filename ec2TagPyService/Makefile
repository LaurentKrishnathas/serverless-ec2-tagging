# @author Laurent Krishnathas
# @version 2017/10/19

# common variables
FUNC=makefile.sh

SERVICE=hello

# pip requirement should be installed separately


deploy:
	sls deploy

invoke:
	sls invoke -f $(SERVICE)

invokeLocal:
	sls invoke local -f $(SERVICE)

remove:
	sls remove


#hello_script:
#	$(FUNC) test
#
#docker_build:
#	docker build -t $(image_name):$(image_version) --rm=false -f $(dockerfile) .
#
#docker_stop:
#	docker stop $(container_name) || echo WARNING $(container_name) may not exist
#	docker rm -f $(container_name) || echo WARNING $(container_name)  may not exist
#
#docker_run: docker_stop docker_build
#	docker image ls |grep $(container_name)
#	docker run -d --name $(container_name) -v $$HOME/.aws:/root/.aws  $(image_name):$(image_version)
#
#docker_log:
#	docker image ls |grep $(container_name)
#	docker ps |grep $(container_name)
#	docker logs -f $(container_name)
#
#docker_push: docker_build
#	docker tag $(image_name):$(image_version) $$ECR_REGISTRY_URI/$(image_name):$(image_version)
#	docker push $$ECR_REGISTRY_URI/$(image_name):$(image_version)
#
#docker_all: docker_run docker_log
#
#docker_exec:
#	docker exec $(container_name) tail -f /var/log/script.log
