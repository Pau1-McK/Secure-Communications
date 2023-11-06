# First i had to convert the .pub to a .pem with ssh-keygen and it gave me the key bellow 

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

public_key_pem = """
-----BEGIN RSA PUBLIC KEY-----
MIIBigKCAYEArTy6m2vhhbwx3RVbNVb3ZOenCqqsOXHaJpbtN+OuulLKBSKpIoPB
+ZDbDXn0qWkf4lOxtGSgolkUbgG07Lhzfgs+dul4UL84CkwZExmF3Rf1nRv+v7pq
Lt2dPsCb02YLxJnhHJb4rQaz2ZM4QCtTOcqYDUeKfLHCaZU4Ekm/OApKrpfw4/0o
fn8KOrFN0t4/dqnNuwVRgoaUIhsI47reApB2rs0AP4CggSIi8s6BXCxB4YzgThBK
5760T1giACYQC5MFdq1Gw+INSFmu0CNqt5wdJ5Z4z5448Gke06R+IMtjUiGDQ3Qt
T2fK3gWhZxk14M4UNrdETgTW/mQ4B/BcvikxvoBGpKbttG0agfOjTen6wyzpGfcd
8N9rSbaqqyUwC8uDotzFtFzzutVAU9d91TagGzWBhNoMfplwVTns27GOOgv1dn5s
QSSSmP0hTbPMDlThysKkR9BiOVbBtWGQpV936pPBgyWERGqMqC9xykLdVHv2Vu05
T0WMwKCAetgtAgMBAAE=
-----END RSA PUBLIC KEY-----
"""

public_key = serialization.load_pem_public_key(public_key_pem.encode())

modulus = public_key.public_numbers().n
print(modulus)