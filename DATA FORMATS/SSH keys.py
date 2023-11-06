from Crypto.PublicKey import RSA


with open("DATA FORMATS\bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub", "rb") as f:
    privateKeyData = f.read()

privateKey = RSA.importKey(privateKeyData)

print(privateKey)

private_key_d = privateKey.d
print(private_key_d)
