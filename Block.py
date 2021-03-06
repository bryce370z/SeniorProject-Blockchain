import hashlib as hasher
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Padding


class Block:

    def __init__(self, index, timestamp, header, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.header = header
        self.nonce = Random.get_random_bytes(16)
        # self.data = data
        self.data = self.encryptionAES(data, self.nonce)
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    def encryptionAES(self, data, nonce):
         password = "TzEQeLNDR~*r4<=L"
         key = hasher.sha256(password.encode('utf-8')).digest()
         data = Padding.pad(data.encode('utf-8'), 16)
         encryptor = AES.new(key, AES.MODE_CBC, IV=nonce)
         ciphertext = encryptor.encrypt(data)
         return ciphertext

    def hash_block(self):
        sha = hasher.sha256(str(self.index).encode('utf-8') +
                            str(self.timestamp).encode('utf-8') +
                            str(self.header).encode('utf-8') +
                            str(self.data).encode('utf-8') +
                            str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()
