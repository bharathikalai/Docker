# In IT these all the commands using in docker 


## Docker inspect 

```
docker inspect <container_name_or_id>
```
## Docker restart 

```
docker restart <container_name_or_id>
```


## Docker log

```
docker logs -n 1000 <container_name_or_id> -f
```


## Start an intractive shell inside  a container

```

docker exec -it <container_name_or_id> /bin/bash

```

## Check the container cpu , memory

```
docker stats <container_name_or_id>
```



## Shows Docker disk usage, which can be useful for cleaning up unused containers, images, volumes, and networks.
```
docker system df
```


# prune

```
docker system prune
```


# Shows the history of changes to a Docker image, which can help debug issues with how the image was built.

```
docker history <image name>

```


# copy command

```
docker cp /home/user/config.json my_container:/app/config/
```

```
docker cp my_container:/app/config/ home/user/

```

# restart 

```
docker run --restart=always -d <image_name>

```