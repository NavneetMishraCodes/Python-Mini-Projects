# importing required libraries and modules
import os
import numpy as np

# loading the list of files
input_address = input("Enter a valid address: ")

# handling the error case
try:
    files_arr = np.array(os.listdir(input_address))
except Exception as e:
    print("Something went wrong (maybe invalid address):", e)
    exit()

# the main searching loop 
while True:
    required_file = input("Enter the name of file you want to find (to exit write: DX): ")

    if required_file == "DX":
        exit()

    if np.isin(required_file, files_arr):
        with open("founded_files.txt", "a") as f:
            f.write(f"File Name = {required_file}\n")
        print("File Found: TRUE !!")
    else:
        with open("notFounded_files.txt", "a") as f:
            f.write(f"File Name = {required_file}\n")
        print("File Found: FALSE !!")


