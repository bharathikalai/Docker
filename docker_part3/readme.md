# A Docker container is a lightweight, portable, and self-contained unit of software that packages an application and its dependencies. Here's a simple explanation

## Key Points:

### Isolated Environment: _Containers run in isolation from other containers and the host system, meaning they don't interfere with each other._

### Runs Anywhere: _Since containers include all the necessary code, libraries, and settings, they can run on any system that supports Docker, making them very portable._

### Lightweight: _Unlike virtual machines (VMs), containers share the host system’s operating system kernel, so they are more efficient and use fewer resources._



## Docker container command_

```
sudo docker run python-helloworld:latest

```

***Limiting CPU and RAM for Docker Containers***

___CPU Limit___
```
sudo docker run --cpu-shares 512 python-helloworld:latest
```

___CPU Quota and Period___

```
sudo docker run --cpu-quota=50000 --cpu-period=100000 python-helloworld:latest
```

___CPU Limit___
```
sudo docker run --cpus="1.5" python-helloworld:latest
```
---

___RAM Limit___

```
sudo docker run --memory="512m" --memory-swap="1g" python-helloworld:latest

```
---

___Docker Commands___

```
sudo docker ps
sudo docker images
sudo docker stats
```
---