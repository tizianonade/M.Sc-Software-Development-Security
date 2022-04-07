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

## Begin - Specification if sharing the file over internet is needed

> Signing consist in creating a ***Digest*** (md5, sha1, sha256...) and encrypt it by the asymetric method using the private key so as to prove the authenticity source of message

### Creation of RSA key pair

```bash
openssl genrsa -aes128 -passout pass:<phrase> -out private.pem 4096
```

### Extraction of the public key

```bash
openssl rsa -in private.pem -passin pass:<phrase> -pubout -out public.pem
```

### Generation of signatures

***Creation of the file***

```bash
touch file.txt
echo "hello world" > file.txt
```

***Generation of the digest of the file***

> openssl dgst -sha256 -sign **private-key** -out sign.sha256 **file**

```bash
openssl dgst -sha256 -sign private.pem -out sign.sha256 file.txt
```

***From binary to Base64 format***

> openssl base64 -in sign.sha256 -out **signature**

```bash
openssl base64 -in sign.sha256 -out sign.enc
```

### Verification of signatures

***From Base64 to binary format***

> openssl base64 -d -in **signature** -out veri_sign.sha256

```bash
openssl base64 -d -in sign.enc -out veri_sign.sha256
```

***Verification of the digest with public key***

> openssl dgst -sha256 -verify **pub-key** -signature veri_sign.sha256 **file**

```bash
openssl dgst -sha256 -verify public.pem -signature veri_sign.sha256 file.txt
```

***Source***

> https://www.zimuel.it/blog/sign-and-verify-a-file-using-openssl

## End - Specification if sharing the file over internet is needed

***

## RSA commands - version 1

### Generation of signatures 

***Generation of signature***

```bash
openssl rsautl -encrypt -inkey private.pem -in file.txt -out sign.enc
```

***Verification of signature***

```bash
openssl rsautl -decrypt -inkey public.pem -in sign.enc > secret_revealed.txt
```

***

## RSA commands - version 2

### Private keys

***Generation of 4096 RSA key pair with encryption of key file***

```bash
openssl genrsa -des3 -out private.pem 4096
```

***Print out RSA private key***

```bash
openssl rsa -in private.pem -text -noout
```

***Encryption of a file containin RSA keys***

```bash
openssl rsa -in private.pem -des3 -out private.pem
```

### Public keys

***Extract public key***

```bash
openssl rsa -in private.pem -pubout -out public.pem
```

***Print out RSA public key***

```bash
openssl rsa -in public.pem -pubin -text -noout
```

### Encryption 

***Encryption of data with RSA (private key)***

```bash
openssl rsautl -encrypt -in file.txt -inkey private.pem -out sign.enc
```

***Encryption of data with RSA (public key)***

```bash
openssl rsautl -encrypt -in file.txt -inkey public.pem -pubin -out sign.enc
```

### Decryption

***Decryption of data with RSA (private key)***

```bash
openssl rsautl -decrypt -in sign.enc -inkey private.pem -out file_releaded.txt
```

***Decryption of data with RSA (public key)***

```bash
openssl rsautl -decrypt -in sign.enc -inkey public.pem -pubin -out file_releaded.txt
```

***Source***

> https://www.fil.univ-lille1.fr/~wegrzyno/portail/PAC/Doc/TP-Certificats/tp-certif.pdf

*** 

## Part 2 - Signatures 

### Signature of little files

***Create a signature***

> openssl rsautl -sign -in **file** -inkey **private key** -out **signature**

```bash
openssl rsautl -sign -in file.txt -inkey private.pem -out sign.enc
```

***Verify signature***

> openssl rsautl -verify -in **signature** -inkey **public key** -pubin -out **file**

```bash
openssl rsautl -verify -in sign.enc -inkey public.pem -pubin -out file_revealed.txt
```

### Signature of big files

***Create a digest from the file***

> openssl dgst (-md5,-sha1,-sha256...) -out file.dgst -in file.txt

```bash
openssl dgst -sha256 -out file.dgst file.txt
```

***Create a signature***

> openssl rsault -sign -in **digest** -inkey **key** -out **signature**

```bash
openssl rsautl -sign -in file.dgst -inkey private.pem -out sign.enc
```

***Verify a signature***

> openssl rsautl -verify -in **signature** -pubin -inkey **key** -out **digest**

```bash
openssl rsautl -verify -in sign.enc -pubin -inkey public.pem -out new_file.dgst
```

>>> ->>> How to compare dgst ...?

***

## Part 3 - Certificates