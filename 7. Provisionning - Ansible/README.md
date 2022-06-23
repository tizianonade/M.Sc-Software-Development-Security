# Provisionning - Ansible

## Requirements

***SSH keygen generation***
```Bash
ssh-keygen
```

***Ansible Installation***

```Bash
sudo apt-get -y install ansible
```

***LXC/LXD***

BUILDING ENVIRONEMENT
```Bash
sudo bash lxc/env_net/inst_cont_env.sh
```

CREATION NETWORK & BRIDGE BR0
```Bash
sudo bash lxc/env_net/set_net.sh
```

CREATION CONTAINER X2 Ubuntu
```Bash
sudo bash lxc/container/creat_list_container.sh
```

START CONTAINER C1
```Bash
sudo bash lxc/container/start_container.sh c1
```

START CONTAINER C2
```Bash
sudo bash lxc/container/start_container.sh c2
```

STOP CONTAINER C1
```Bash
sudo bash lxc/container/stop_container.sh c1
```

STOP CONTAINER C2
```Bash
sudo bash lxc/container/stop_container.sh c2
```

## Configuration

***/etc/ansible/host***
```Bash
[lxc]
192.168.10.11 ansible_user=root
192.168.10.12 ansible_user=root
```

***SSH installation on clients***
```Bash
sudo bash ansible/ssh_env.sh c1
```

***Authorize Root login***
```Bash
lxc exec c1-- passwd
lxc exec c1 -- vi /etc/ssh/sshd_config
lxc exec c1 -- systemctl restart sshd
ssh-copy-id root@192.168.10.11
```

***Ping command***
```Bash
ansible lxc -m ping
```

# Exercices Ansible

## Question 1 install lxc ...

```Bash
vi packagesInstallation.yml
```

```Bash
---
- name: Installation of packages for clients
  hosts: lxc
  remote_user: root
  tasks:
  - name: Installation lxc
    apt: update_cache=yes
    apt: name=lxc state=present

  - name: Installation lxd
    apt: update_cache=yes
    apt: name=lxc state=present

  - name: Installation bridge utils
    apt: update_cache=yes
    apt: name=bridge-utils state=present
```

```Bash
 ansible-playbook packagesInstallation.yml
```