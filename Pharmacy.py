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
<<<<<<< HEAD
        prints blockchain
        """
        for block in self.BlockChain:
            print(block.header)
            print(block.data)
=======
        decrypts blockchain
        """
        password = "TzEQeLNDR~*r4<=L"
        key = hashlib.sha256(password).digest()

        for block in self.BlockChain:
            decryptor = AES.new(key, AES.MODE_CBC, IV=block.nonce)
            plain = decryptor.decrypt(block.data)
            print(block.header)
            print(plain)
>>>>>>> 455e7cd4ff59a2159224295547e806edf5bbccd3
            print("hash: " + block.hash + "\n")
