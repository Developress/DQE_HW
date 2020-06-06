import argparse
import json
import csv
from argparse import Namespace
from pprint import pprint

# define the needed arguments
parser = argparse.ArgumentParser()
parser.add_argument('-csv', '-Csv file path', help='Path where csv file is stored')
parser.add_argument('-json', '-Json file path', help='Path to write json file')

args: Namespace = parser.parse_args()

with open(args.csv + r"\user_details.csv") as f:
    # read the csv file
    reader = csv.DictReader(f)
    dict_list = []
    # create the dict list
    for line in reader:
        dict_list.append(line)
    # delete password column
    for element in dict_list:
        del element['password']
    # form the json string
    json_str = json.dumps(dict_list)

    with open(args.json, "w") as json_file:
        # write json string beautifully to the file
        pprint(json_str, json_file)
        print(f"Result to file {args.json} was saved successfully")
