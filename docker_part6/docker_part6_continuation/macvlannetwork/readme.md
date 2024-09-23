# Macvlan

A Macvlan Network allows Docker containers to appear as separate devices on your physical network. Each container gets its own MAC address and IP address, just like any physical machine on the network.


# Why Use Macvlan Network?
- Direct Access: Containers can communicate directly with other devices on the same physical network (e.g., printers, servers) without going through the Docker bridge network.
- Network Isolation: Each container can be isolated and managed as a separate entity on the network.
- Legacy Applications: Useful for applications that require a dedicated network interface


# COMMANDS:

```
ip addr
```

```
docker network create -d macvlan \
--subnet=192.168.0.0/24 \
--gateway=192.168.0.1 \
-o parent=wlp0s20f3 my_macvlan

```