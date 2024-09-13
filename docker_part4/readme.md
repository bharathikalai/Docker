
# Docker file commands


## FROM

- Purpose: Specifies the base image to use for the Docker image.
- Usage: Every Dockerfile must begin with a FROM command.
- Example: FROM ubuntu:20.04
- Explanation: This command sets the base image to Ubuntu 20.04. Docker builds your image on top of this base.

## RUN

- Purpose: Executes commands in a new layer on top of the base image, typically used to install dependencies.
- Usage: Can be used multiple times to run various shell commands.
- Example: RUN apt-get update && apt-get install -y python3
- Explanation: This installs Python 3 on the image by running a shell command during the image build process.

## CMD

- Purpose: Provides default commands to be executed when a container is started.
- Usage: Only one CMD instruction is allowed per Dockerfile. If more than one CMD is specified, only the last one is used.
- Example: CMD ["python3", "app.py"]
- Explanation: This runs python3 app.py when the container starts.

## ENTRYPOINT

- Purpose: Configures the container to run as an executable. Similar to CMD, but it cannot be overridden by arguments passed to docker run.

- Example: ENTRYPOINT ["python3", "app.py"]

- Explanation: This will ensure that python3 app.py is always executed when the container starts.


## WORKDIR

- Purpose: Sets the working directory inside the container for subsequent commands (e.g., RUN, CMD, ENTRYPOINT, etc.).

- Example: WORKDIR /app

- Explanation: This sets /app as the working directory, so any commands like RUN or COPY will operate from this directory.

## COPY 

- Purpose: Copies files or directories from the host machine to the container’s filesystem.

- Example: COPY . /app

- Explanation: This copies the contents of the current directory on the host into the /app directory inside the container.


## ADD

- Purpose: Similar to COPY, but with additional functionalities like extracting .tar files or fetching remote URLs.

- Example: ADD file.tar.gz /app

- Explanation: This extracts file.tar.gz into the /app directory inside the container.



## ENV

- Purpose: Sets environment variables inside the container.

- Example: ENV APP_ENV=production

- Explanation: This sets an environment variable APP_ENV to production, which can be accessed by any processes running inside the container.


## EXPOSE

- Purpose: Informs Docker that the container listens on specified network ports at runtime.

- Example: EXPOSE 8080

- Explanation: This exposes port 8080 for external access to the container.


## VOLUME

- Purpose: Creates a mount point with a specified path and marks it as a storage volume from the host system

- Example: VOLUME /data

- Explanation: This will mount a volume at /data inside the container, allowing persistent storage.


## USER

- Purpose: Sets the user to use when running the image or commands within the Dockerfile.

- Example: USER appuser

- Explanation: This sets the user to appuser for running the application or executing commands, improving security by not running as root.


## LABEL

- Purpose: Adds metadata to the image as key-value pairs.

- Example: LABEL version="1.0" maintainer="you@example.com"

- Explanation: This adds metadata about the image’s version and maintainer for documentation or tracking purposes.



## ARG

- Purpose: Defines build-time variables that can be passed to the Docker build process.

- Example: ARG VERSION=1.0

- Explanation: This defines a build argument VERSION that can be used in the Dockerfile.


## STOPSIGNAL

- Purpose: Sets the system call signal used to stop the container

- Example: STOPSIGNAL SIGINT

- Explanation: This instructs the container to stop using the SIGINT signal instead of the default SIGTERM.



## SHELL 

- Purpose: Specifies the default shell to use for the RUN command.


- Example: SHELL ["/bin/bash", "-c"]

- Explanation: This makes sure that subsequent RUN commands use Bash instead of the default /bin/sh.


## HEALTHCHECK


- Purpose: Adds a health check to the container to monitor if the service is healthy.

- HEALTHCHECK CMD curl --fail http://localhost:8080 || exit 1


- Explanation: This runs a health check that tries to curl the localhost at port 8080 to see if the service is running


## ONBUILD

- Purpose: Adds triggers to your image that will be executed when the image is used as a base for another build.

- Example: ONBUILD RUN apt-get update && apt-get install -y some-package

- Explanation: When this image is used as a base for another image, the RUN command will automatically execute.


## ARG with ENV



- Purpose: Combines build-time arguments (ARG) with environment variables (ENV), allowing them to be used interchangeably.

```
ARG VERSION=1.0
ENV APP_VERSION=${VERSION}

```

- Explanation: Here, the VERSION build argument is used to set the environment variable APP_VERSION.