import os
import csv

file_path = os.path.join('..', "budget_data.csv")

#open up file
with open(file_path , 'r') as file:

#create csv handler
    reader = csv.reader(file, delimiter='-')
    print(reader)
#read each row

#print how many rows there arepy