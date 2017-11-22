class Doctor:

    def __init__(self, mediator):
        self.BlockChain = []
        self.mediator = mediator
        self.subscribe()

    def subscribe(self):
        """
            Subscribes instance to defined mediator
        """
        self.mediator.Subscribers.append(self)

    def add_block(self, new_block):
        """
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
