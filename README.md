# JSON-Similarity-comparitor
A command line tool for comparing JSON files by degree of similarity.

## Requirements:
* Take two files as command line arguements. (Positional or named arguements are fine)
* Should output 1.0 for any pair of JSON documents that contain the same data.
* Should output a value < 1.0 for any pair of documents that are not equal.\
* Ideally uses intermediate scores to convey a degree of similarity between the documents.
* Focus on detecting equality before assessing similarity
* Don't write any code to parse the JSON, thats what built in language features and libraries are for.
* Include a README file that describes any assumptions made & highlights anything about the solutions I made that I'd like Quiq to know about.

## BONUSES:
* Add additional information (more than just similarity score) that might help the user
  - difference output file?

## PLANNED BONUSES:
* An output log of exactly what variables are different, and what the difference is. (Comparing objects)
* In that output log, include what attributes one object has/lacks in comparison to the other.
