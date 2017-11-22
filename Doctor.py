class Doctor:

    def __init__(self, mediator):
        self.BlockChain = []
        self.mediator = mediator
        self.subscribe()

    def subscribe(self):
        """
<<<<<<< HEAD
        Subscribes instance to defined mediator
=======
            Subscribes instance to defined mediator
>>>>>>> 455e7cd4ff59a2159224295547e806edf5bbccd3
        """
        self.mediator.Subscribers.append(self)

    def add_block(self, new_block):
        """
<<<<<<< HEAD
        adds block to blockchain, through mediator
        """
        self.mediator.add_block(new_block)
=======
            adds block to blockchain, through mediator
        """
        self.mediator.add_block(new_block)

    def print_chain(self):
        """
        prints blockchain unencrypted
        """
        for block in self.BlockChain:
            print(block.header)
            print(block.data)
            print("hash: " + block.hash + "\n")
>>>>>>> 455e7cd4ff59a2159224295547e806edf5bbccd3
