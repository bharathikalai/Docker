# Types of network

- __Host Network__
- __Overlay Network__
- __Macvlan Network__
- __None Network__

## What is Docker’s Host Network Mode?
- Normally, when you run a Docker container, Docker creates a small, separate virtual network for the container. The container gets its own IP address that is different from the host’s IP address. When traffic goes in and out of the container, it has to go through this virtual network layer, and Docker handles translating traffic between the container and the host.

- However, with Host Network mode, Docker removes this virtual network layer. Instead of giving the container its own IP address, the container uses the same IP address and network interfaces as the host machine itself.



## HOst network example


__Without Host Network Mode:__


```
[Host IP: 192.168.1.100] <--> [Container IP: 172.17.0.2]
```

__With Host Network Mode:__

```
[Host IP: 192.168.1.100] <--> [Container uses 192.168.1.100]
```



____Run NGINX without Host Network____

```
docker run --name nginx-bridge -d -p 8080:80 nginx

```

____Run NGINX with Host Network Mode____

```

docker run --name nginx-host --network host -d nginx

```


