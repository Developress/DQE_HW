import argparse
import csv
from argparse import Namespace

# define the needed arguments
parser = argparse.ArgumentParser()
parser.add_argument('-path', '-Input path', help='Path in which we are searching')
parser.add_argument('-bed', '-Amount of beds', help='Amount of beds with the biggest percentage')

args: Namespace = parser.parse_args()
percentage_list = []
percentage = 0

with open(args.path + r"\HRR Scorecard_ 20 _ 40 _ 60 - 20 Population.csv") as f:
    # read csv file
    csv_file = csv.DictReader(f)
    # omit headers
    next(csv_file)

    for row in csv_file:
        # calculate the percentage of available beds
        percentage = round(int(row["Available Hospital Beds"].replace(",", ""))
                           / int(row["Total Hospital Beds"].replace(",", "")) * 100, 2)

        # append to percentage list the item which is list itself
        # consisting of line num and percentage value
        percentage_list.append([csv_file.line_num, percentage])

    # sort the percentage list by value of percentage in reverse order
    percentage_list.sort(key=lambda x: x[1], reverse=True)

    print(f"{args.bed} HRRs with the biggest percentage of available beds")

    for i in range(0, int(args.bed)):
        # read csv file again
        f.seek(0)
        csv_file = csv.DictReader(f)
        # omit headers
        next(csv_file)

        for row in csv_file:
            # if the index of line in file matches with the index from list
            if csv_file.line_num == percentage_list[i][0]:
                print(row["HRR"], percentage_list[i][1], "%")
                break
