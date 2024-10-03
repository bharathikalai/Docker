# Commands

## Docker login

```
docker login

```


## Docker build command

```
docker build -t <imagename:tag> .
```

## Docker tag

```
docker tag <local-image>:<tag> <dockerhub-username>/<repository>:<tag>

```

## Docker push 

```
docker push <dockerhub-username>/<repository>:<tag>
```

## local image path

```
/var/lib/docker/
```



## api path

## sudo cat ~/.docker/config.json

```
{
	"auths": {
		"https://index.docker.io/v1/": {
			"auth": "sssgfgfgsfgfsf"
		}
	}
}

```