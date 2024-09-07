# Docker architecture:

![alt text](image.png)


## Docker Engine
### Docker Daemon (dockerd): 
The Docker Daemon is a background process that manages Docker containers. It listens for Docker API requests and handles building, running, and monitoring containers. It can be run on a local machine or on a server.

### Docker CLI (docker): 
The Docker Command Line Interface (CLI) is the tool you use to interact with the Docker Daemon. Commands like docker run, docker build, and docker ps are executed through the CLI.

### Docker REST API: 
The Docker Daemon exposes a REST API that can be used to interact with it programmatically. This API allows for the management of Docker containers, images, networks, and volumes.


# HOw to install docker in ubuntu

``` sudo apt update
sudo apt install docker.io
sudo systemctl status docker
```

