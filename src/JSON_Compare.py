import sys
import json
import os.path
import Equivalence_Processor as eq

# TODO: Command line arguements for files to compare.

# effectively the program's main function.
def run():
    # TODO: Consider inclusion of colored coded print outs?
    argument_amount = len(sys.argv)
    if argument_amount >= 3:
        json_file_A = sys.argv[1]
        json_file_B = sys.argv[2]
        
        # Validate that both the json files entered as parameters exist.
        if validate_file(json_file_A) and validate_file(json_file_B):
            print("Running", sys.argv[0], " on files:", json_file_A, "and", json_file_B)
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
        
# Converts files to objects
def open_files_as_objects(filename_A, filename_B):
    json_object_a = None
    json_object_b = None
    # TODO: Open both JSON files and store as objects
    with open(filename_A) as json_file:
        json_object_a = json.load(json_file)
        
    with open(filename_B) as json_file:
        json_object_b = json.load(json_file)
        
    # Temporary print outs for the objects. Include in Verbos call?
    for p in json_object_a:
        print(p)
    print()
    for p in json_object_b:
        print(p)
        
    eq.compare_json_objs(json_object_a, json_object_b)

run()
# Current testing command: python JSON_Compare.py ../Examples/BreweriesMaster.json ../Examples/BreweriesSample1.json