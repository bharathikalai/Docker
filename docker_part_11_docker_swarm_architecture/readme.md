# Manager Nodes:

```
At the top, show multiple manager nodes (one leader and some followers) responsible for orchestration, service discovery, and load balancing.
```


# Worker Nodes:

```
Below the manager nodes, display worker nodes. Each worker node should have one or more containers (tasks) representing the workload.
```


# Service:

```
On the manager nodes, have a box labeled "Service," defining how many replicas to create.
Show arrows from the service definition to the worker nodes, where containers (replicas) are actually running.
```

# Overlay Network:

```
Draw an overlay network connecting both the manager and worker nodes, indicating communication between them.

```


# command ubuntu conatinor

```
docker run --privileged -d --name dind-container-1 docker:dind  


docker run --privileged -d --name dind-container-2 docker:dind

```


# docker swarm init command

```
sudo docker swarm init --advertise-addr 192.168.0.127
```

# docker swarm commands

```
docker swarm leave
docker swarm inspect
```

# create our first service 

```
sudo docker service create --replicas 2 -p 80:80 --name web1 httpd

```