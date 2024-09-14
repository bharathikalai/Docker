## Command 


### Build the Docker Image
```
docker build -t my-apache-image .

```

### Run the Docker Container

```
docker run -d -p 8080:8080 --name my-apache-container my-apache-image
```