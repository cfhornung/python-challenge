import os
import csv

path = "/Users/cfhor/Desktop/personal-data/python-challenge/PyBank/"
file_path = os.path.join(path,"budget_data.csv")
print(file_path)

#Assignment
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


# open up the file
with open(file_path , 'r') as file:

# create csv handler
    reader = csv.reader(file)
    line_count = 0
    for row in reader:
        if line_count == 0:
  #          print(f'Column names are {", ".join(row)}')
            line_count += 1
  #      print(f'\t{row[0]}  {row[1]}')
        line_count += 1
   # print(f'Processed {line_count} lines.')
    months_output = line_count-2

# calculate total
with open(file_path , 'r') as file:
    reader = csv.reader(file)

# skip the header row
    next(reader)
    total = 0
    for row in reader:
        total += int(row[1])
total_output = total

# calculate average change
month = [ ]
with open(file_path , 'r') as file:
    reader = csv.reader(file)
    month = [row[0] for row in reader]

profits = [ ]
with open(file_path , 'r') as file:
    reader = csv.reader(file)
    profits = [row[1] for row in reader]

# print(month)
# print(profits)
# print(month[10])
# print(profits[10])

# loop through
total_change = 0
for i in range(1,(months_output-1)):
     total_change += (int(profits[i+1])-int(profits[i]))    
average_change_output = round(((total_change)/months_output),1)

# calculate Greatest Increase
greatest_change = 0
this_month = 0
next_month = 0
greatest_month = 0
for i in range(1,(months_output-1)):
     this_month = (int(profits[i+1])-int(profits[i]))   
     next_month = (int(profits[i+2])-int(profits[i+1]))  
     if next_month > greatest_change:
            greatest_change = next_month
            greatest_month = i+1
greatest_change_output = round((greatest_change),1)
greatest_month_output = month[greatest_month]

# calculate Greatest Decrease
greatest_decrease = 0
this_month = 0
next_month = 0
smallest_month = 0
for j in range(1,(months_output-1)):
     this_month = (int(profits[j+1])-int(profits[j]))   
     next_month = (int(profits[j+2])-int(profits[j+1]))  
     if next_month < greatest_decrease:
            greatest_decrease = next_month
            smallest_month = j+1
greatest_decrease_output = round((greatest_decrease),1)
smallest_month_output = month[smallest_month]

# beautify output to screen
print("Financial Analysis")
print("________________________")
print(f'Total Months: {months_output}')
print(f'Total: ${total_output}')
print(f'Average Change: ${average_change_output}')
print(f'Greatest Increase in Profits: ${greatest_change_output} {greatest_month_output}')
print(f'Greatest Decrease in Profits: ${greatest_decrease_output} {smallest_month_output}')

# write output to file
f = open('lesson3_budgetdata.txt', 'w')
f.write("Financial Analysis\n")
f.write("________________________\n")
f.write(f'\nTotal Months: {months_output}')
f.write(f'\nTotal: ${total_output}')
f.write(f'\nAverage Change: ${average_change_output}')
f.write(f'\nGreatest Increase in Profits: ${greatest_change_output} {greatest_month_output}')
f.write(f'\nGreatest Decrease in Profits: ${greatest_decrease_output} {smallest_month_output}')
f.close()