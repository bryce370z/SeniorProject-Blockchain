from Block import Block
import datetime as date

def genesis_block():

    return Block(index=0, timestamp=date.datetime.now(), data="Genesis Block", previous_hash="0")

def next_block(last_block):

    index = last_block.index + 1
    timestamp = date.datetime.now()
    data = "BLOCK: " + str(index)
    last_block_hash = last_block.hash
    return Block(index=index, timestamp=timestamp, data=data, previous_hash=last_block_hash)

def main():
    blockchain = [genesis_block()]
    num_blocks = 20
    for i in range(1, num_blocks +  1):
        new_block = next_block(blockchain[i - 1])
        blockchain.append(new_block)
        print(new_block.data, "generated with Hash:", str(new_block.hash), "\n")
if __name__ == "__main__":
    main()
