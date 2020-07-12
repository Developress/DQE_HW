import argparse
import csv
from pymongo import MongoClient


def insert_data_to_db(file, collection):
    """
        Read the data from the csv file and insert it to the appropriate collection

        :param file: the path to the file from which the data is readed
        :param collection: the collection of MongoDB to insert the data
    """
    with open(file) as f:
        # read the csv file as a dictionary
        content = csv.DictReader(f)

        for row in content:
            # insert the row to the collection
            collection.insert_one(row)


# define and parse the needed arguments
parser = argparse.ArgumentParser()

parser.add_argument('--file1', help='Path to the first csv file with the data for project collection')
parser.add_argument('--file2', help='Path to the second csv file with the data for task collection')

args = parser.parse_args()

# connect to MongoDB
mongo = MongoClient(host='localhost', port=27017)

# create the database
db = mongo.test

# drop the collections if previously existed
db.project.drop()
db.task.drop()

# create the collections again
project = db.project
task = db.task

insert_data_to_db(args.file1, project)
insert_data_to_db(args.file2, task)


print("All the records from the task table with status \"Canceled\"")

for record in task.find({"status": "Canceled"}):
    print(record)
