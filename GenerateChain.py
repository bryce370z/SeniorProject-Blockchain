from Block import Block
import datetime as date
from DataBuilder import DataBuilder
from CsvBuilder import CsvBuilder
from Pharmacy import Pharmacy
from Doctor import Doctor
from ChainMediator import ChainMediator

def genesis_block():
    """
    Creates initial block in blockchain
    """
    return Block(index=0, timestamp=str(date.datetime.now()), header="Genesis Block", data="", previous_hash="0")


def next_block(last_block):
    """
    Creates next block in blockchain
        args:
            last_block: the previous block in the blockchain
    """
    index = last_block.index + 1
    timestamp = str(date.datetime.now())
    header = "BLOCK: " + str(index)
    db = DataBuilder()
    data = db.build_data()
    last_block_hash = last_block.hash
    return Block(index=index, timestamp=timestamp, header=header, data=data, previous_hash=last_block_hash)

def main():
    # outputting hashes to CSV for analysis
    cb = CsvBuilder("output.csv")
    print("would you like to clear the csv output file, before taking in the next list of hashes? Y/N: ")
    choice = str(input())
    if choice == "Y":
        cb.clear_csv()

    # initializing entites to share generated chain
    cm = ChainMediator()
    doctor = Doctor(cm)
    pharmacy = Pharmacy(cm)

    # generating blockchain
    doctor.add_block(genesis_block())
    num_blocks = 20
    for i in range(1, num_blocks + 1):
        new_block = next_block(doctor.BlockChain[i - 1])
        doctor.add_block(new_block)
        cb.add_data(str(new_block.hash))

    pharmacy.print_chain()
    cb.write_to_csv()

if __name__ == "__main__":
    main()
