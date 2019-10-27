# Imports
import sys
import os.path
from Comparison import Comparison

# effectively the program's main function.
def run():
    argument_amount = len(sys.argv)
    if argument_amount >= 3:
        json_file_A = sys.argv[1]
        json_file_B = sys.argv[2]
        
        # Validate that both the json files entered as parameters exist.
        if validate_file(json_file_A) and validate_file(json_file_B):
            print("Running", sys.argv[0], " on files:", json_file_A, "and", json_file_B)
            comp = Comparison(json_file_A, json_file_B)
        else:
            print("Please enter valid file paths. Program Exiting...")
    else:
        print("Not enough Arguements. Please include JSON files to compare.")
# TODO: Consider adding pathing manager?

# Validates if the file exists or not.
def validate_file(file_path):
    if file_path is None:
        print("No file/path entered.")
        return False
    elif os.path.exists(file_path):
        return True
    else:
        print("File name/path is Invalid:", file_path)
        return False
        
run()