# PKI

## Part 1 - RSA

***Generation of 1024 bits RSA key pair***

```bash
openssl genrsa -out rsakeys.pem 1024
```

***Print out they RSA key pair***

```bash
openssl rsa -in rsakeys.pem -check
```

***Print out they RSA key pair with modulus, prime & exponent***

```bash
openssl rsa -in rsakeys.pem -check -text
```

***Extract only the public key***

```bash
openssl rsa -in rsakeys.pem -pubout -out rsapub.pem
```

***Print out the public key***

```bash
openssl rsa -pubin -text -in rsapub.pem
```

***Transformation of the format - from PEM to DER***

```bash
openssl rsa -outform der -in rsakeys.pem -out rsakeys.der
```

***Transformation of the format - from DER to PEM***

```bash
openssl rsa -inform der -outform pem -in rsakeys.der -out rsakeys2.pem
```

***

## Signature RSA