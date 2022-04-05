# OpenSSL

## Part 1 - Intro

***List of commands of openssl:***

```bash
man openssl
```

***Version of openssl:***

> OpenSSL 1.1.1f  31 Mar 2020

***Display list of SSL/TLS ciphers:***

```bash
openssl ciphers -v
```
## Part 2 - Encryption & Decryption

***Encryption of file***

```bash
touch file.txt
echo "hello world" > file.txt
openssl enc -des-cbc -in file.txt -out secret.txt
cat secret.txt
```

***Content of the encrypted file***

> Salted__`cj�����M@���E�Plb��I�yf��=U�9��z��

***Meaning of the salt***

> In cryptography, a salt is random data that is used as an additional input to a one-way function that hashes data, a password or passphrase. Salts are used to safeguard passwords in storage. -> A short random set of character that are appened to the end of a message

***Decryption of the file***

```bash
openssl enc -d -des-cbc -in secret.txt -out newfile.txt
cat newfile.txt
```

***Encryption with "-p" option which print out the salt, key & iv***

```bash
openssl enc -p -des-cbc -in file.txt -out secret2.txt
```

***Output***

> salt=06A30006A4967886\
> key=A9CFF5F24AF41A2F \
> iv =91048AC829B615EB

> By retyping the command the output will be different

***Use -nosalt option for not appending the salt***

## Part 3 - First steps with RSA

***Generate a RSA key 1024 bits named "signature.pem"***
