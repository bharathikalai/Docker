# Docker Containor commands
__Here is a list of useful Docker container commands that cover container management, inspection, interaction, and removal:__

## Start a Container :

```
docker start <container_name_or_id>
```

## Stop a Container :

```
docker stop <container_name_or_id>

```
## Restart a Container

```
docker restart <container_name_or_id>
```

## Pause a Container
```
docker pause <container_name_or_id>

```

## Unpause a Container

```
docker unpause <container_name_or_id>
```

## Remove a Container

```
docker rm <container_name_or_id>
```

## Force Remove a Running Container

```
docker rm -f <container_name_or_id>
```
## List Running Containers
```
docker ps
```

## List All Containers (Running and Stopped)

```
docker ps -a
```


## Create a New Container and Run It

```
docker run -d --name <container_name> <image_name>
```


## Create a New Container with Interactive Terminal

```
docker run -it <image_name> /bin/bash
```
## Attach to a Running Container

```
docker attach <container_name_or_id>

```

## Inspect a Container's Details

```
docker inspect <container_name_or_id>
```

## View Logs of a Container

```
docker logs <container_name_or_id>
```

##  View Real-Time Logs

```
docker logs -f <container_name_or_id>
```

## Copy Files/Folders Between Container and Host

- Copy from container to host:

```
docker cp <container_name_or_id>:<container_path> <host_path>
```

- Copy from host to container:

```
docker cp <host_path> <container_name_or_id>:<container_path>
```

## Execute a Command in a Running Container

```
docker exec -it <container_name_or_id> <command>
```

## View Resource Usage Statistics (CPU, Memory, etc.)

```
docker stats <container_name_or_id>

```

##  Rename a Container

```
docker rename <old_name> <new_name>
```

## Export a Container as a Tarball

```
docker export <container_name_or_id> -o <file_name.tar>
```

## View the Top Processes Inside a Container

```
docker top <container_name_or_id>
```

## Update Container Resources (e.g., memory, CPU)

```
docker update --memory <value> --cpus <value> <container_name_or_id>
```

## Check Differences in File System Between the Container and its Image

```
docker diff <container_name_or_id>
```

## Commit Changes of a Container to Create a New Image

```
docker commit <container_name_or_id> <new_image_name>

```
## Kill a Running Container (Force Stop)

```
docker kill <container_name_or_id>
```

## Remove All Stopped Containers
```
docker container prune
```



