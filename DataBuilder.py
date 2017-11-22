import json
import datetime
import random

class DataBuilder:

    data = None

    def __init__(self):
        self.data = self.build_data()

    def build_data(self):
        """
        Generated Randomized data for a block
        """

        # doctors = ["Dr. Nate Ambrose", "Dr. Damon Bradley", "Dr. Ethan Carter", "Dr. Courtney Ellis", "Dr. Arthur Jackson"
        #           , "Dr. Gwen Pennington", "Dr. Lillian Price", "Dr. Dan Prince", "Dr. Raleigh Stewart", "Dr. Ana Syphax", "Dr. Ben Turner"
        #           , "Dr. Geoffrey Weiss", "Dr. Wesley Williams"]
        doctors = raw_input("Please enter the Doctor's name: ")
        deaNumber = raw_input("Please enter the DEA regulation number: ")
        address = raw_input("Please enter the patient's address: ")
        birth = raw_input("Please enter the patient's date of birth: ")

        #
        prescription_date = str(datetime.datetime.now())

<<<<<<< HEAD
        #
        # doctor_phone_numbers = ["202-555-0102", "202-555-0171", "202-555-0193", "202-555-0111", "202-555-0191", "202-555-0147"
        #                        , "202 - 555 - 0114", "202 - 555 - 0180" ,"202 - 555 - 0127", "202 - 555 - 0180" ,"202 - 555 - 0128"
        #                        , "202 - 555 - 0107"]
        doctor_phone_numbers = raw_input("Please enter the Doctor's phone number: ")

        # patient_names = ["Mario Speedwagon", "Petey Cruiser", "Anna Sthesia", "Paul Molive", "Anna Mull", "Gail Forcewind"
        #                 ,"Paige Turner", "Bob Frapples", "Walter Melon", "Nick R.Bocker", "Barb Ackue", "Buck Kinnear"
        #                 ,"Greta Life", "Ira Membrit", "Shonda Leer"]
        patient_names = raw_input("Please enter the patient's name: ")

        # drug_names = ["Atorvastatin Calcium","Levothyroxine","Lisinopril","Omeprazole","Metformin","Amlodipine",
        #               "Simvastatin","Hydrocodone","Metoprolol ER","Losartan","Azithromycin","Zolpidem","Hydrochlorothiazide",
        #               "Furosemide","Metoprolol"]
        drug_names = raw_input("Please enter the prescription drug name: ")
        # drug_amounts = ["500mg", "200mg", "600mg", "100mg", "50mg", "900mg"]
        drug_amounts = raw_input("Please enter the drug amount in milligrams: ")
        tablet_amounts = raw_input("Please enter the tablet amount: ")
        patient_instructions = raw_input("Please enter the patient instructions: ")
        refills = raw_input("Please enter the number of refills: ")

        block_data = {'doctor' : doctors,
                      'DEA number' : deaNumber,
=======
        doctor_phone_numbers = ["202-555-0102", "202-555-0171", "202-555-0193", "202-555-0111", "202-555-0191", "202-555-0147"
                               , "202 - 555 - 0114", "202 - 555 - 0180" ,"202 - 555 - 0127", "202 - 555 - 0180" ,"202 - 555 - 0128"
                               , "202 - 555 - 0107"]
        patient_names = ["Mario Speedwagon", "Petey Cruiser", "Anna Sthesia", "Paul Molive", "Anna Mull", "Gail Forcewind"
                        ,"Paige Turner", "Bob Frapples", "Walter Melon", "Nick R.Bocker", "Barb Ackue", "Buck Kinnear"
                        ,"Greta Life", "Ira Membrit", "Shonda Leer"]
        drug_names = ["Atorvastatin Calcium","Levothyroxine","Lisinopril","Omeprazole","Metformin","Amlodipine",
                      "Simvastatin","Hydrocodone","Metoprolol ER","Losartan","Azithromycin","Zolpidem","Hydrochlorothiazide",
                      "Furosemide","Metoprolol"]
        drug_amounts = ["500mg", "200mg", "600mg", "100mg", "50mg", "900mg"]

        block_data = {'doctor': random.choice(doctors),
>>>>>>> 455e7cd4ff59a2159224295547e806edf5bbccd3
                      'prescription_date': prescription_date,
                      'doctor_phone_numbers': doctor_phone_numbers,
                      'patient_names': patient_names,
                      'address' : address,
                      'birth' : birth,
                      'drug_names': drug_names,
                      'drug_amounts': drug_amounts,
                      'tablets' : tablet_amounts,
                      'instructions' : patient_instructions,
                      'refills' : refills
                      }

        json_block_data = json.dumps(block_data, indent=4)

        return json_block_data
