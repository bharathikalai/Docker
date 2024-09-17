# Build the Docker image
```
docker build -t my-nginx-1 .
```

# Create a named volume
```
docker volume create my_named_volume-1
```

# Run the container with the named volume

```
docker run -d --name my-nginx-container-1 -v my_named_volume:/usr/share/nginx/html -p 8082:80 my-nginx-1
```