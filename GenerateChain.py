from Block import Block
import datetime as date
from DataBuilder import DataBuilder
from CsvBuilder import CsvBuilder
from Pharmacy import Pharmacy
from Doctor import Doctor
from ChainMediator import ChainMediator
import sys

def genesis_block():
    """
    Creates initial block in blockchain
    """
    return Block(index=0, timestamp=str(date.datetime.now()), header="Genesis Block", data="In the beginning God created the heavens and the earth.", previous_hash="0")


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
    # data = db.build_data()
    last_block_hash = last_block.hash
    return Block(index=index, timestamp=timestamp, header=header, data=db.data, previous_hash=last_block_hash)


def main():
    # outputting hashes to CSV for analysis
    cb = CsvBuilder("output.csv")
    print("would you like to clear the csv output file, before taking in the next list of hashes? Y/N: ")
    choice = str(input())
    if choice == "Y" or choice == "y":
        cb.clear_csv()

    # initializing entites to share generated chain
    cm = ChainMediator()
    doctor = Doctor(cm)
    pharmacy = Pharmacy(cm)
    doctor.add_block(genesis_block())

    while True:
        print("Options:")
        print("[1] Doctor: Write a prescription")
        print("[2] Doctor: View the blockchain (encrypted)")
        print("[3] Pharmacist: Fill a prescription (decrypted)")
        print("[4] Corrupt the blockchain")
        print("[5] Validate the blockchain")
        print("[6] Output blockchain to CSV")
        print("[quit] exit program")

        decision = str(input(""))
        if decision == "quit":
            sys.exit()
        elif decision == "1":
            """
            Doctor: Write a prescription

            Add a block to the chain
            """
            print("How many prescriptions (blocks) would you like to write? ")
            num_blocks = int(input())
            for i in range(1, num_blocks + 1):
                new_block = next_block(doctor.BlockChain[i - 1])
                doctor.add_block(new_block)
                cb.add_data(str(new_block.hash))

        elif decision == "2":
            """
            Doctor: View the blockchain (encrypted)

            View an encrypted version of the blockchain
            """
            doctor.print_chain()

        elif decision == "3":
            """
            Pharmacist: Fill a prescription (decrypted)
            """
            pharmacy.print_chain()

        elif decision == "4":
            """
            Corrupt the blockchain
            """
            doctor.BlockChain[1].timestamp = str(date.datetime.now())
            pharmacy.BlockCsshain[1].timestamp = str(date.datetime.now())
            print("Blockchain corrupted.")

        elif decision == "5":
            """
            Validate the blockchain
            """
            i = 0
            for sub in cm.Subscribers:
                if(cm.validate_chain(sub.BlockChain)):
                    i+=1
                else:
                    print("Blockchain is invalid. Delete cascading through depending blocks.")
                    """
                    ###########################################
                    Do all the crazy delete things/restore to moderator's goodchain version
                    ###########################################
                    """

            if(i == len(cm.Subscribers)):
                print("Blockchain validated.")


        elif decision == "6":
            cb.write_to_csv()
            print("Output complete.")
        else:
            print("Please enter one of the valid options.")

        # # generating blockchain
        #
        # num_blocks = 20
        # for i in range(1, num_blocks + 1):
        #     new_block = next_block(doctor.BlockChain[i - 1])
        #     doctor.add_block(new_block)
        #     cb.add_data(str(new_block.hash))
        #
        # pharmacy.print_chain()
        # cb.write_to_csv()

if __name__ == "__main__":
    main()
