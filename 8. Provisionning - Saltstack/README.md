# Provisionning Saltstack

## Requirements

### Master

***Packages***
```Bash
apt-get update && apt-get -y install curl && apt-get -y install python3.7 && apt-get -y install nano
```

***Download installation script***
```Bash
curl -L https://bootstrap.saltstack.com -o install_salt.sh
```

***Execution installation script***
```Bash
sudo sh install_salt.sh -P -M -N
```

***Master configuration***
```Bash
sudo nano /etc/salt/master.d/local.conf
```

```Bash
# The address of the interface to bind to:
interface: 192.168.10.1
```

```Bash
sudo systemctl restart salt-master
```

```Bash
sudo salt-key --finger-all
```
> Copy 
> master.pub:  64:12:61:93:3e:09...

```Bash
sudo salt-key --finger-all
```

```Bash
sudo salt-key -A
```

```Bash
sudo salt-run manage.up
```

```Bash
sudo salt '*' test.ping
```

### Minion

```Bash
apt-get update && apt-get -y install curl && apt-get -y install python3.7 
```

```Bash
curl -L https://bootstrap.saltstack.com -o install_salt.sh
```

```Bash
sudo sh install_salt.sh -P
```

```Bash
nano /etc/salt/minion.d/local.conf
```

```Bash
# The address of the interface to bind to:
interface: 192.168.10.1
```

```Bash
systemctl restart salt-minion
```

```Bash
nano /etc/salt/minion
```
>
> master_finger: '64:12:61:93:3e:09...'
> id : c1

```Bash
systemctl restart salt-minion
```

```Bash
sudo salt-call key.finger --local
```