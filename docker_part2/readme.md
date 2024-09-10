# What is docker image and how to create a docker file & docker containor 

_videolink_ [youtube](https://youtu.be/mr1TRseW-y4?si=O9oho2WQPakr8fFB)


```
FROM python:3.8-slim
CMD ["python","-c","print("hello world")"]

```

## Docker image build command

``` 
sudo docker build -t python-helloworld:latest

```

## Docker containor run command

```
sudo docker run python-helloworld:latest

```


## Baseimage retrieval

_The FROM instruction specifies the base image (e.g., python:3.9-slim), which could be an operating system or language runtime (like Python)_
---
## Layered Filesystem

## Layered file system is a union file system

- [x] FROM: Creates the first layer (the base image).
- [x] COPY: Adds files to the image, creating another layer.
- [x] RUN: Executes commands in the image and creates another layer.

---
_These layers are cached so that if the build process is repeated and nothing has changed in the Dockerfile, Docker can reuse the cached layers. This speeds up future builds_
---

## Architecture : 
![alt text](image.png)

### Storing the Image
_Docker stores the resulting image in its local image repository (stored on your machine, typically under /var/lib/docker)._
_The image is immutable, meaning it cannot be modified. Any changes to it would result in a new layer._
***



