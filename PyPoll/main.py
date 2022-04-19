
import os
import csv
from re import M

#animals 

candidates={}

#total animals
total_votes=0

most_votes_obtained=0
most_votes_name=""


csvpath=os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)
    

    csv_header=next(csvreader)

    for row in csvreader:
      candidate_name=row[2]

      total_votes = total_votes + 1

      if candidate_name in candidates:
        candidates[candidate_name] = candidates[candidate_name] + 1
      else:
        candidates[candidate_name] = 1


with open("Analysis/PyPoll.txt", "w") as txt_file:

  output= "Election Results\n-----------"
  print(output)
  txt_file.write(output + "\n")

  output= "Total Votes" + ":" + str(total_votes)
  print(output)
  txt_file.write(output)
  
  output="\n-----------"
  print(output)
  txt_file.write(output+'\n')

  
  for key, value in candidates.items():
    if value > most_votes_obtained:
      most_votes_name = key
      most_votes_obtained = value
    votes_per_candidate= str(value)
    percentage_of_votes=(value/total_votes)*100 

    output= key + ": " + str(round(percentage_of_votes,3))+ "% "  + (str(value))
    print(output)
    txt_file.write(output+'\n')
   
   
  output="-----------"
  print(output)
  txt_file.write(output+'\n')

  
  output= "Winner: " + most_votes_name
  print(output)
  txt_file.write(output+'\n')

  output="-----------"
  print(output)
  txt_file.write(output+'\n')

