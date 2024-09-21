# Bridge Network

## Description: 

- This is the default network type for standalone containers. Containers in the same bridge network can communicate with each other, while external communication is limited to mapped ports.
- Use case: Useful for creating isolated networks where containers can communicate internally without exposing all services to the external network.

# Commands 

```

```

```
docker run --network network_name Created_image
```

```
docker network connect my_bridge container_name
```