# send some signal to process in container
docker kill --signal=HUP my_container

# run command inside container
docker exec -it my_container /bin/sh
