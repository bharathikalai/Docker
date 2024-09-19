# Docker Volume commands

## Creat a volume

```
docker volume create <volume_name>
```

## List all volumes

```
docker volume ls
```

## Inspect a volume

```
docker volume inspect <volume_name>

```

## Remove a volume
```
docker volume rm <volume_name>
```

## Run a container with a volume:

```
docker run -d -v <volume_name>:/path/in/container <image_name>
```

## Bind mount a host directory as a volume:

```
docker run -d -v /path/on/host:/path/in/container <image_name>

```

## Create a container with an anonymous volume:

```
docker run -d -v /path/in/container <image_name>

```

## List volumes in use by containers

```
docker ps --filter volume=<volume_name>

```


# Two MySQL containers share the same Docker volume.


## 1st Command

```
docker volume create shared-mysql-data

```


## 2st Command 

```
docker run -d \
--name mysql1 \
-e MYSQL_ROOT_PASSWORD=root_password \
-e MYSQL_DATABASE=test_db \
-v shared-mysql-data:/var/lib/mysql \
mysql:latest

```

## 3rd Command

```

docker run -d \
--name mysql2 \
-e MYSQL_ROOT_PASSWORD=root_password \
-e MYSQL_DATABASE=test_db \
-v shared-mysql-data:/var/lib/mysql \
mysql:latest


```



## Tmpfs volume


```
docker run -d \
--name mysql_tmpfs \
-e MYSQL_ROOT_PASSWORD=root_password \
--tmpfs /var/lib/mysql:rw,size=256m \
mysql:latest
```