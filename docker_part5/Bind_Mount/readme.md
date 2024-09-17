# Build the Docker image

```
docker build -t my-nginx-2 .
```

# Run the container with a bind mount

```
docker run -d --name my-nginx-container-2 -v /home/bharathibk/github/Docker/docker_part5/Bind_Mount/abc/html:/usr/share/nginx/html -p 8083:80 my-nginx-2
```
