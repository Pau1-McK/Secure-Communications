from Crypto.PublicKey import RSA
from base64 import b64decode


with open("DATA FORMATS\privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem", "rb") as f:
    privateKeyData = f.read()

privateKey = RSA.importKey(privateKeyData)

print(privateKey)

private_key_d = privateKey.d
print(private_key_d)
