from Block import Block
import datetime as date
from DataBuilder import DataBuilder


def genesis_block():
    return Block(index=0, timestamp=date.datetime.now(), header="Genesis Block", data="", previous_hash="0")


def next_block(last_block):
    index = last_block.index + 1
    timestamp = date.datetime.now()
    header = "BLOCK: " + str(index)
    db = DataBuilder()
    data = db.build_data()
    last_block_hash = last_block.hash
    return Block(index=index, timestamp=timestamp, header=header, data=data, previous_hash=last_block_hash)


def main():

    blockchain = [genesis_block()]
    num_blocks = 20
    for i in range(1, num_blocks + 1):
        new_block = next_block(blockchain[i - 1])
        blockchain.append(new_block)
        print(new_block.header, "generated with Hash:", str(new_block.hash), "\n")
        print(new_block.data, "\n")

if __name__ == "__main__":
    main()
