import json
class Pharmacy:

    def __init__(self, mediator):
        self.BlockChain = []
        self.mediator = mediator
        self.subscribe()

    def subscribe(self):
        """
        Subscribes instance to defined mediator
        """
        self.mediator.Subscribers.append(self)

    def print_chain(self):
        """
        decrypts blockchain
        """
        password = "TzEQeLNDR~*r4<=L"
        key = hashlib.sha256(password).digest()

        for block in self.BlockChain:
            decryptor = AES.new(key, AES.MODE_CBC, IV=block.nonce)
            plain = decryptor.decrypt(block.data)
            print(block.header)
            print(plain)
            print("hash: " + block.hash + "\n")
