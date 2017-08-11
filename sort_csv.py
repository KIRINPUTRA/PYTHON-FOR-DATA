import csv, sys, operator

filename = input("Please enter the name of the .csv file you want sorted.\n")
if filename[-4:] != ".csv":
    filename += ".csv"

key_col = int(input("Which column do you want to sort by? Enter 1 to sort by the first column, 2 to sort by the second column, and so on.\n")) - 1

with open(filename, "r") as infile, open(filename[:-4] + "_SORTED" + filename[-4:], "w") as outfile:
    reader = csv.reader(infile, delimiter = ',')
    writer = csv.writer(outfile)
    sort = sorted(reader, key = operator.itemgetter(key_col), reverse = False)
    for eachline in sort:
        writer.writerow(eachline)
