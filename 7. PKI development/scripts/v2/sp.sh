#!/bin/bash
import cryptography
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509

f = open("/home/v2/certificate/pki_pub_key.pem")
imagestring = f.read()
byteArray = bytes(imagestring,encoding='utf8')


issuer_public_key = load_pem_public_key(byteArray)

f = open("/home/v2/certificate/v1.crt")
imagestring = f.read()
byteArray = bytes(imagestring,encoding='utf8')


cert_to_check = x509.load_pem_x509_certificate(byteArray)
issuer_public_key.verify(
    cert_to_check.signature,
    cert_to_check.tbs_certificate_bytes,
    # Depends on the algorithm used to create the certificate
    padding.PKCS1v15(),
    cert_to_check.signature_hash_algorithm,
)
