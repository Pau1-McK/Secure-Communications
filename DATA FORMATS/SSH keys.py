# The SSH public key
ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCtPLqba+GFvDHdFVs1Vvdk56cKqqw5cdomlu034666UsoFIqkig8H5kNsNefSpaR/iU7G0ZKCiWRRuAbTsuHN+Cz526XhQvzgKTBkTGYXdF/WdG/6/umou3Z0+wJvTZgvEmeEclvitBrPZkzhAK1M5ypgNR4p8scJplTgSSb84Ckqul/Dj/Sh+fwo6sU3S3j92qc27BVGChpQiGwjjut4CkHauzQA/gKCBIiLyzoFcLEHhjOBOEErnvrRPWCIAJhALkwV2rUbD4g1IWa7QI2q3nB0nlnjPnjjwaR7TpH4gy2NSIYNDdC1PZ8reBaFnGTXgzhQ2t0ROBNb+ZDgH8Fy+KTG+gEakpu20bRqB86NN6frDLOkZ9x3w32tJtqqrJTALy4Oi3MW0XPO61UBT133VNqAbNYGE2gx+mXBVOezbsY46C/V2fmxBJJKY/SFNs8wOVOHKwqRH0GI5VsG1YZClX3fqk8GDJYREaoyoL3HKQt1Ue/ZW7TlPRYzAoIB62C0= bschneier@facts"

# Split the SSH public key string and extract the base64-encoded key
key_parts = ssh_public_key.split()
encoded_key = key_parts[1]

# Decode the base64-encoded key
decoded_key = base64.b64decode(encoded_key)

# Extract the modulus (n) from the decoded key
modulus_start = decoded_key.find(b'\x00\x00\x00\x80')  # The modulus usually starts with 0x00 0x00 0x00 0x80
modulus_end = decoded_key.find(b'\x00\x00\x01\x00', modulus_start)  # The modulus usually ends with 0x00 0x00 0x01 0x00

modulus_bytes = decoded_key[modulus_start + 4 : modulus_end]  # Extract the modulus bytes
modulus_decimal = int.from_bytes(modulus_bytes, byteorder='big')  # Convert to a decimal integer

# Print the modulus as a decimal integer
print(modulus_decimal)
