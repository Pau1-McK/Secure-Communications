from pwn import xor

lName = "label"
key = 13

def xorString(lName, key):
    xoredString = xor(lName, key)
    return xoredString


results = xorString(lName, key)

print(results)