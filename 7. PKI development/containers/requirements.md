# Requirements

## Host Linux distribution

- The host is considered as an Ubuntu Server 20.4.

**Update distribution:**

```Bash
sudo apt update
```

```Bash
>sudo apt upgrade
```

## Packages installation

***LXC templates:***

```Bash
sudo apt-get -y install lxc lxctl lxc-templates
```

***Bridges utils:***

```Bash
sudo apt-get -y install bridge-utils
```

***QEMU:***

```Bash
sudo apt-get -y install qemu qemu-utils qemu-system-x86
```

***Docker:***

```Bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

```Bash
sudo apt-get install ca-certificates curl gnupg lsb-release
```

```Bash
curl -fsSL `https://download.docker.com/linux/ubuntu/gpg` | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

```Bash
echo   "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] `https://download.docker.com/linux/ubuntu`\ $(lsb_release -cs) stable test" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```Bash
sudo apt-get update
```

```Bash
sudo apt-get install docker-ce docker-ce-cli containerd.io`
```

***Application folder:***

```Bash
mkdir app_pki/
```