import os
import csv

path = "/Users/cfhor/Desktop/personal-data/python-challenge/PyPoll/"
file_path = os.path.join(path, "election_data.csv")
#print(file_path)

# open up the file
with open(file_path , 'r') as file:

# create csv handler
    reader = csv.reader(file)
    line_count = 0
    for row in reader:
        if line_count == 0:
   #       print(f'Column names are {", ".join(row)}')
            line_count += 1
        #    print(f'\t{row[0]}  {row[1]} {row[2]}')
        line_count += 1
    #print(f'Processed {line_count} lines.')
    votes_output = line_count-2

# count votes
voterid = [ ]
with open(file_path , 'r') as file:
    reader = csv.reader(file)
    voterid = [row[0] for row in reader]

county = [ ]
with open(file_path , 'r') as file:
    reader = csv.reader(file)
    county = [row[1] for row in reader]

candidate = [ ]
with open(file_path , 'r') as file:
    reader = csv.reader(file)
    candidate = [row[2] for row in reader]

# count votes
Khancount = 0
Khanpercent = 0
for i in range(1,votes_output):
    if (candidate[i] == "Khan"):
            Khancount += 1
Khanpercent = round((Khancount / votes_output)*100,2)

Correycount = 0
Correypercent = 0
for j in range(1,votes_output+1):
    if (candidate[j] == "Correy"):
            Correycount += 1
Correypercent = round((Correycount / votes_output)*100,2)

Licount = 0
Lipercent = 0
for k in range(1,votes_output+1):
    if (candidate[k] == "Li"):
            Licount += 1
Lipercent = round((Licount / votes_output)*100,2)

OTooleycount = 0
OTooleypercent = 0
for l in range(1,votes_output+1):
    if (candidate[l] == "O'Tooley"):
            OTooleycount += 1
OTooleypercent = round((OTooleycount / votes_output)*100,2)

# who won?
if Khancount > max(Correycount, Licount, OTooleycount):
    Winner = "Khan"
if Correycount > max(Khancount, Licount, OTooleycount):
    Winner = "Correy"
if Licount > max(Khancount, Correycount, OTooleycount):   
    Winner = "Li"
if OTooleycount > max(Khancount, Licount, Correycount):    
    Winner = "O'Tooley"  

# beautify output to screen
print('Election Results')
print('________________________')
print(f'Total Votes: {votes_output}')
print('________________________')

print(f'Khan {Khanpercent} %  ({Khancount})')
print(f'Correy {Correypercent} %  ({Correycount})')
print(f'Li {Lipercent} %  ({Licount})')
print(f'OTooley {OTooleypercent} %  ({OTooleycount})')
print("________________________")
print(f'Winner {Winner}')
print('________________________')

# write output to file
f = open('lesson3_Election.txt', 'w')
f.write(f'\nElection Results')
f.write(f'\n________________________')
f.write(f'\nTotal Votes: {votes_output}')
f.write(f'\n________________________')

f.write(f'\nKhan {Khanpercent} % ({Khancount})')
f.write(f'\nCorrey {Correypercent} % ({Correycount})')
f.write(f'\nLi {Lipercent} % ({Licount})')
f.write(f'\nOTooley {OTooleypercent}% ({OTooleycount})')
f.write(f'\n________________________')
f.write(f'\nWinner {Winner}')
f.write(f'\n________________________')
f.close()