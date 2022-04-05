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

***

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

***

## Part 3 - First steps with RSA

***Generate a 1024 RSA key pair named "signature.pem"***

```bash
openssl genrsa -out signature.pem 1024
```

***Visualise the content***

```bash
openssl rsa -in signature.pem -text -noout
```

***Output***

> RSA Private-Key: (1024 bit, 2 primes)\
> modulus:\
>   00:b6:34:03:c8:09:a5:fc:d9:eb:ed:59:32:78:fb: \
>   ...\
> publicExponent: 65537 (0x10001)\
> privateExponent:\
>    00:9a:28:2e:1e:dc:92:f4:f9:08:55:3b:c7:a9:76:\
>    ...\
> prime1:\
>   00:e9:b3:7b:a0:4e:14:06:db:f4:90:cd:e7:71:df:\
>   ...\
> prime2:\
>    00:c7:96:9d:35:95:07:ff:11:89:af:bf:a6:6b:72:\
>    ...\
> exponent1:\
>    41:7a:52:36:f5:e9:52:8a:aa:19:30:37:9a:85:fc:\
>    ...\
> exponent2:\
>    00:87:b2:c1:64:42:d5:52:f8:8b:92:70:4d:27:d4:\
>    ...\
> coefficient:\
>    00:d3:eb:0e:dc:72:a7:10:a0:88:e1:9f:a8:bd:df:\
>    ...

***Explanation:***

> Private key contains the prime numbers, modulus, public exponent, private exponent and coefficients.

> Public key contains modulus and public exponent.

> Modulus (n) is the product of two prime numbers used to generate the key pair.

> Public exponent (d) is the exponent used on signed / encoded data to decode the original value.

***

***Source***

> https://medium.com/@bn121rajesh/understanding-rsa-public-key-70d900b1033c#:~:text=Modulus%20(n)%20is%20the%20product,to%20decode%20the%20original%20value.

***

***Why 65537 for the pub exponent?***

> It is the largest known prime number of the form 

***Extract public key from a key pair file***

```bash
openssl rsa -in signature.pem -pubout > public_signature.pem
cat public_signature.pub
```

### Encryption & Decryption of files with RSA

***Create a file with a size inferior of 100 bytes***

```bash
echo "Hello world" > file.txt
```

***Encryption the file with the public key***

```bash
openssl rsautl -encrypt -inkey public_signature.pem -pubin -in file.txt -out secret.enc
```

***Output of cat secret.enc***

> K�o���Wg�N�ENt�m�Ly� Ń
                 }Tb��������@�0S疛��蛛"#=���U�yoNo��P�#<i�UڄQ&Q��y9\�=��'����Zߔ�!'�


***Decryption of the secret file with the private key***

```bash
openssl rsautl -decrypt -inkey signature.pem -in secret.enc > secret_revealed.txt
```

***At the opposite -> Ecryption with private key and decryption with public key -> Not possible!!!***

***

***Help:***

> https://opensource.com/article/21/4/encryption-decryption-openssl

***

## Part 4 - Encryption & data size 

***Generate a 2048 key pair***

```bash
openssl genrsa -out signature.pem 2048
```

***Extraction of the public key***

```bash
openssl rsa -in signature.pem -pubout > public_signature.pem
cat public_signature.pem
```

***Creation of a new file with a size above 100 MB***

```bash
curl https://dl-cdn.alpinelinux.org/alpine/v3.15/releases/x86_64/alpine-standard-3.15.4-x86_64.iso -o alpine.img
```

***Encryption of the new file***

```bash
openssl rsautl -encrypt -inkey public_signature.pem -pubin -in alpine.img -out secretAlpine.enc
```

***Output***

> RSA operation error\
> 139863429395776:error:0406D06E:rsa routines:RSA_padding_add_PKCS1_type_2:data too large for key size:

***Explanation***

> the size (number of bytes) of the input data should be smaller than the size (number bytes) of the modulus, which is also the RSA key size.

***

## Part 5

***Generate a 512 key pair***

```bash
openssl genrsa -out signature.pem 512
```

***Extract the public key***

```bash
openssl rsa -in signature.pem -pubout > public_signature.pem
cat public_signature.pem
```

***Generate a random 256 key pair***

```bash
openssl genrsa -out random_signature.pem 256
```
