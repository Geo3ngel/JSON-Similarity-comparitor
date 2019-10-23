# The purpose of this Class is to hold relevant JSON objects for purpose of comparison with reference
# To their respective file names.

# Imports
import Equivalence_Processor as eq
import json
    
class Comparison():
    
    # Initialize a comparison with the json file name
    def __init__(self, json_filename_a, json_filename_b):
        print("Initialized new comparison")
        # Store the file names
        self.filename_a = json_filename_a
        self.filename_b = json_filename_b
        
        # Store the json objects for easier referencing
        self.json_object_a, self.json_object_b = self.open_files_as_objects(json_filename_a, json_filename_b)
        
        # Initialize similarity metrics
        self.similarity = 1.0
        
        # TODO: Handle file differences as some kind of tree structure?
        self.file_a_differences = 0
        self.file_b_differences = 0
        
        # TODO: Consider mapping of filename/objects and related information?
        
        # Run comparison on the json objects
        self.similarity = eq.compare_json_objs(self)
        result = self.similarity*100
        print("\nSimilarity Result:", str(result)+"%")
    
    # Converts files to objects
    def open_files_as_objects(self, filename_A, filename_B):
        json_object_a = None
        json_object_b = None
        
        # Opens both JSON files and stores them as objects
        with open(filename_A) as json_file:
            json_object_a = json.load(json_file)
            
        with open(filename_B) as json_file:
            json_object_b = json.load(json_file)
        
        # Return both json objects
        return json_object_a, json_object_b
