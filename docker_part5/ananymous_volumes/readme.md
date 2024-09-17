# Build the Docker image

```
docker build -t my-nginx .
```

# Run the container with an anonymous volume

```
docker run -d --name my-nginx-container -p 8081:80 my-nginx

```