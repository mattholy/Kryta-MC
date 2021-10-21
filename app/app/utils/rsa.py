# -*- encoding: utf-8 -*-
'''
rea.py
----
处理Kryta Server激活链接的加密


@Time    :   2021/10/11 21:21:05
@Author  :   Mattholy
@Version :   1.0
@Contact :   smile.used@hotmail.com
@License :   MIT License
'''

import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

class RsaController:
    def __init__(self) -> None:
        self.__rsa_public_key = RSA.importKey('''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAz3hZU1fLW4OqFq8Rl31f
SRlAINxnNsFI6JAK0RZzjeHbW9A9hmyj4YP0toG4OwKjbvyrNejIEekEZZGK5eqO
io6nPb+oARasMOKtdzw/OdkB5wqz9/Zh49RVD4AYWcVvPPJyXHK+uSL8Gu7QWTSa
IfjpnQV03qckcBoV6pYlNjVEt+LglOU9CTWGGn6pq6TIFS9Q+zBqjlTQ99gyGUMv
SQQBLuK7RyC3MVAUuJ5hIUQlzrTcrwuBHpU86AZvpfNTc9FG3RVx5EYtRwuU6N4F
xJLJ3bPyNCmzLsdgGBAb7kllSkx63M8oGpCVYFv0Iss2yVwd+m/jnoiP0dagHliQ
FwIDAQAB
-----END PUBLIC KEY-----''')

    def encrypt_data(self,msg) -> str:
        public_key = self.__rsa_public_key
        cipher = PKCS1_cipher.new(public_key)
        encrypt_text = base64.b64encode(cipher.encrypt(bytes(msg.encode("utf8"))))
        return encrypt_text.decode('utf-8')

    def decrypt_data(self,encrypt_msg) -> str:
        private_key = self.__rsa_private_key
        cipher = PKCS1_cipher.new(private_key)
        back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)
        return back_text.decode('utf-8')
    
    def rsa_private_sign(self,data) -> str:
        private_key = self.__rsa_private_key
        signer = PKCS1_signature.new(private_key)
        digest = SHA.new()
        digest.update(data.encode("utf8"))
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
        signature = signature.decode('utf-8')
        return signature
    
    def rsa_public_check_sign(self,text,sign) -> bool:
        publick_key = self.__rsa_public_key
        verifier = PKCS1_signature.new(publick_key)
        digest = SHA.new()
        digest.update(text.encode("utf8"))
        return verifier.verify(digest, base64.b64decode(sign))

if __name__ == '__main__':
    import json
    a = RsaController()
    print(a.encrypt_data(
        json.dumps(
            {
                "use_hub_backup":True,
                "username":"qwer",
                "password":"qwer"
            }
        )
    ))