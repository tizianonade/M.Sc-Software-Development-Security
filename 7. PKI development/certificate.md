# Certificate

## PKI - Gateway - Hub

```Bash
apt update
```

```Bash
apt-get install openssl -y
```

***Create key pair rsa***

```Bash
mkdir -p /home/pki/certificate
```

```Bash
openssl genrsa -out "/home/pki/certificate/pki_key.pem" 2048
```

***Create certificate for the CA using CA key***

```Bash
openssl req -x509 -days 365 -key "/home/pki/certificate/pki_key.pem" -out "/home/pki/certificate/ca.crt" -subj "/C=FR/ST=Paris/L=Paris/O=URCA/OU=MASTER RT/CN=pki"
```

## Gateway

***Create folder***

```Bash
mkdir -p /home/gateway/certificate
```

***Create key pair rsa***

```Bash
openssl genrsa -out "/home/gateway/certificate/gateway_key.pem" 2048
```

***Create a certificate request .csr***

```Bash
openssl req -new -key "/home/gateway/certificate/gateway_key.pem" -out "/home/gateway/certificate/gateway.csr" -subj "/C=FR/ST=Paris/L=Paris/O=URCA/OU=MASTER RT/CN=gateway"
```

## Hub

```Bash
mkdir -p /home/hub/certificate
```

***Create key pair rsa***

```Bash
openssl genrsa -out "/home/hub/certificate/hub_key.pem" 2048
```

***Create a certificate request .csr***

```Bash
openssl req -new -key "/home/hub/certificate/hub_key.pem" -out "/home/hub/certificate/hub.csr" -subj "/C=FR/ST=Paris/L=Paris/O=URCA/OU=MASTER RT/CN=hub"
```

## PKI

***Create a certificate for the gateway***

```Bash
openssl x509 -req -in "/home/pki/certificate/gateway.csr" -CA ca.crt -CAkey "/home/pki/certificate/pki_key.pem" -CAcreateserial -out "/home/pki/certificate/gateway.crt" -days 365
```

***Create a certificate for the hub***

```Bash
openssl x509 -req -in "/home/pki/certificate/hub.csr" -CA ca.crt -CAkey "/home/pki/certificate/pki_key.pem" -CAcreateserial -out "/home/pki/certificate/hub.crt" -days 365
```
