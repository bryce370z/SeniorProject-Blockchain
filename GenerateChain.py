from Block import Block
import datetime as date
from DataBuilder import DataBuilder
import sys


def genesis_block():
    return Block(index=0, timestamp=date.datetime.now(), header="Genesis Block", data="In the beginning God created the heavens and the earth.", previous_hash="0")


def next_block(last_block):
    index = last_block.index + 1
    timestamp = date.datetime.now()
    header = "BLOCK: " + str(index)
    db = DataBuilder()
    # data = db.build_data()
    last_block_hash = last_block.hash
    return Block(index=index, timestamp=timestamp, header=header, data=db.data, previous_hash=last_block_hash)


def main():

    blockchain = [genesis_block()]
    num_blocks = 0
    #for i in range(1, num_blocks + 1):
    while True:
        print("Options: [display] contents of the blockchain, [create] a new block, or [quit]\n")
        decision = raw_input("")
        if (decision == "quit"):
            sys.exit()
        elif (decision == 'display'):
            for i in range(0, len(blockchain)):
                print("Block number: " + str(blockchain[i].index))
                print("Timestamp: " + str(blockchain[i].timestamp))
                print("header: " + str(blockchain[i].header))
                print("Data: " + str(blockchain[i].data))
                print("Previous Hash: " + str(blockchain[i].previous_hash))
                print("Block Hash: " + str(blockchain[i].hash))
                
        elif(decision == 'create'):
            new_block = next_block(blockchain[len(blockchain) - 1])
            blockchain.append(new_block)
            print(new_block.header, "generated with Hash:", str(new_block.hash), "\n")
        else:
            print("Please enter one of the 3 options.")

if __name__ == "__main__":
    main()
