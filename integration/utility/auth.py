import base64
from Cryptodome.Cipher import AES


class AESCipher(object):

    def __init__(self, key, iv):
        self.bs = 16
        self.key = bytes(key, "utf-8")
        self.iv = bytes(iv, 'utf-8')

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = self.iv

        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = self.iv
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc)).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]
