# Containers Creation

## Gateway

As mentioned in the introduction the gateway is a Docker container, it was chosen to create it from an Ubuntu 20:04 image for the same reason as for the container representing vehicles. The gateway can both receive messages from vehicles and forward them to the hub through MQTT communication protocol. So, a MQTT broker is installed on it with Mosquito solution. A shared folder was created between the host and the container to develop scripts directly inside the container using an IDE.

***Host's environement***

```Bash
mkdir -p ~/app_pki/scripts/gateway
```

***Creation of container***

```Bash
sudo docker create -it --name gateway -v \
~/app_pki/scrits/gateway:/home/gateway/scripts/ ubuntu /bin/bash
```

## Hub

About the hub, it is also a Docker container, it is built from an Ubuntu 20:04 Docker image. It receives data from the gateway so a Mosquitto broker is installed in the container. The container is called eventhub and it was created by sharing a folder with the host.

***Host's environment***

```Bash
mkdir -p ~/app_pki/scripts/hub
```

***Creation of containers***

```Bash
sudo docker create -it --name hub -v ~/app_pki/scripts/hub/:/home/hub/scripts/ ubuntu /bin/bash
```

```Bash
sudo docker create -it --name gateway -v ~/app_pki/scripts/gateway/:/home/gateway/scripts/ ubuntu /bin/bash
```

```Bash
sudo docker create -it --name pki -v ~/app_pki/scripts/pki/:/home/pki/scripts/ ubuntu /bin/bash
```