# Network

## Theory

The network is is composed only of two main containers the gateway, the hub and a bridge to connect them.

|             Network address             |  192.168.0.0  |
|:---------------------------------------:|:-------------:|
|                 Netmask                 | 255.255.255.0 |
| Bridge br1 that connects all containers |  192.168.0.1  |
|             Gateway address             |   19.168.0.2  |
|               Hub address               |  192.168.0.3  |
|               Pki address               |  192.168.0.4  |

## Configuration

### Bridges

Bridges is created using the Docker engine.

***Net1: br1 creation***

```Bash
sudo docker network create --driver=bridge -o "com.docker.network.bridge.name=br1" \
--subnet=192.168.0.0/24 net1
```

### Containers

To connect all containers to their bridges, the following command must be used:

> sudo docker network connect --ip IPofContainer RelatedNetwork NameofContainer

For instance, the gateway is connected thanks to the following command:

```Bash
sudo docker network connect --ip 192.168.0.2 net1 gateway
```