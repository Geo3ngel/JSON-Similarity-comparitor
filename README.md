# JSON-Similarity-comparitor
A command line tool for comparing JSON files by degree of similarity.

## Requirements:
* Take two files as command line arguements. (Positional or named arguements are fine)
* Should output 1.0 for any pair of JSON documents that contain the same data.
* Should output a value < 1.0 for any pair of documents that are not equal.
* Ideally uses intermediate scores to convey a degree of similarity between the documents.
* Focus on detecting equality before assessing similarity
* Don't write any code to parse the JSON, thats what built in language features and libraries are for.
* Include a README file that describes any assumptions made & highlights anything about the solutions I made that I'd like Quiq to know about.

## Assumptions

* No libraries for JSON comparison may be used
* Solution does not have to be optimal
* When taking in two files for command line arguements, requiring proper pathing from the program's directory is acceptable

## Design

The first thing that came to mind when I thought of how to compare JSON files was to convert them into JSON objects and recurse through them in a `top down` styled approach. This way JSON files of a similar purpose or task would likely have higher similarity scores, as the structures would be largely similar, and JSON files meant for different purposes would be less so.

Of course the values themselves also contribute, however say if some values are stored in a `list` in one JSON object, where as in the other they are a `dictionary`, we would want to penalize that, as those two JSON file's structural difference is indicitive of a different purpose. As such, this program would account for the `type difference` between these two, and also recursively count all of the `children` of the list/dicts against the similarity value.

This approach makes it easy to deal with the JSON files object (represented as a `tree`) being `uneven` in some circumstances. Take for example where one tree has a node that is of type string, where as the other is a dictionary of drinks. They are of `different types`, so there is the inital penalty for that, but then all of the drink key value pairs count against the similarity value as well. 

Or if they where `both dictionaries`, but one has `more entries` than the other, the key value pairs would be evaluated against one another, but then the remaining pairs on one side would be added to the `difference value`, which acts against the similarity value.

### However,

This approach is not with flaws, due to the `top down` approach ustalized, we do not detect similarity of `sub components`. Which means to say there could be the same drink key in two dictionaries, but say one of those dictionaries is in a list or nested in another strcture that this program recognises as different. In this scenario, they would not be registered as similar.

In order to combat this, a `bottum up` approach would be necessary. By a bottum up approach, I mean starting at the end leaf nodes of the two trees and working our way up. Although this method would be more complex, both time wise and to write, as it would have to deal with checking for a match against all other active edge nodes of the other tree until a match is found to traverse upwards.

Alternatively matching of value names to their values in a `hash table` for the first JSON object, then generating the second one over that and noting the matches/differences would also work to find similar end variables, however this approach lacks `knowledge of file structure`, and as such two files could have a high similarity rating that are drastically different.

## How it performs:

    It captures similarity accuratly between JSON files of with similar base structure. If it contains sub components that are similar, but the json files have different base structures, this format will not capture that well, if at all. This is due to the top down approach of comparison used.
    
    If I where to make further improvements to this, I would probably add the hashtable method mentioned above and incorperate it into the current top down approach to check for similarity in type difference evaluations from a certain node in the tree downwards.

| PERFORMANCE TABLE: | Breweries Master | Sample 1 | Sample 2 | Sample 3 | Sample 4 | Sample 5 |
|:------:|:----------------:|:--------:|:--------:|:--------:|:--------:|:-------:|
| Breweries Master |100%|100%|72.92%|71.64%|2.38%|88.89%|
| Sample 1 |100%|100%|2.20%|1.82%|1.19%|2.06%|
| Sample 2 |72.92%|2.20%|100%|10.63%|2.38%|64.81%|
| Sample 3 |71.64%|1.82%|13.84%|100%|1.94%|35.29%|
| Sample 4 |2.38%|1.19%|2.38%|1.94%|100%|2.22%|
| Sample 5 |88.89%|2.06%|64.81%|35.29%|2.22%|100%|

## Examples format for running code:

As per the requirements, this program runs in the command line with two `JSON` files as arguements.

In order to run, navigate into the src directory to run the `JSON_Compare.py` python script. 

Once in the proper directory, use the following command to run the program:

    python JSON_Compare.py file_1.json file_2.json

However please note you will have to replace `file_1.json` and `file_2.json` with the proper pathing to the json files you want to compare.

Here is an example using the Breweries samples in the Examples directory.

    python JSON_Compare.py ../Examples/BreweriesMaster.json ../Examples/BreweriesSample1.json

## Features to improve on
* Consider mapping of variable names to their actual values for use in comparison.
* A bottom up approach for better evaluation of JSON files that don't have a similar base structure.
* Hash table variable comparison method for two nodes
* Change to remove nodes of the tree once they are done being visited to reduce time complexity.
        
## Features that could be added
- An output log file of exactly what variables are different, and what the difference is. (Comparing objects)
- In that output log, include what attributes one object has/lacks in comparison to the other.