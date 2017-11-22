from Doctor import Doctor
from Pharmacy import Pharmacy
class ChainMediator:

    def __init__(self):
        self.GoodChain = []
        self.Subscribers = []

    def add_block(self, new_block):
        """
        Adds Block to all Subscriber's blockchains
            args:
                new_block: new block to be appended to blockchain
        """
        for sub in self.Subscribers:
            sub.BlockChain.append(new_block)
            if(self.validate_chain(sub.BlockChain)):
                self.GoodChain.append(new_block)
                
    """
    TODO: add function that validates chain. Test validation after each block is added, by verifying
    that all BlockChains for all subscribers are not corrupted, after the addition of the block.
    If new block addition is valid on all subscribers, add new block to GoodChain. If any subscribers
    are corrupt, reset all subscribers to GoodChain.
    """
    def validate_chain(self, BlockChain):
        """
        Finds any corrupt blocks in the BlockChain
            args:
                BlockChain: blockchain to be validated
            return: boolean
        """
        for i in range(len(BlockChain)):
            current_block = BlockChain[i]
            old_hash = current_block.hash
            new_hash = current_block.hash_block()
            if old_hash != new_hash:
                print("BLOCK: " + str(current_block.index) + " is corrupt.")
                return False
        return True

