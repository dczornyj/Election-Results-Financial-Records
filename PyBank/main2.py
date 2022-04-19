import os
import csv


total_profit_losses=0
current_=0
last=0

total_change=0
months=0

greatest_increase=0
greatest_decrease=100000000000000

csvpath=os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)
    

    csv_header=next(csvreader)

    #loop through all rows in the csv file
    for row in csvreader:
        total_profit_losses= total_profit_losses + int(row[1]) 

        months= months + 1

        current=int(row[1])

        change=current-last

        #finding the total changes in profits/losses
        if months> 1:
        
            total_change=total_change+change
        
        #finding the greatest increase change in profits/losses
                   
        if change > greatest_increase:
            greatest_increase=change
            greatest_increase_month=row[0]
            

        #finding the greatest decrease change in profits/losses
        if change < greatest_decrease: 
            greatest_decrease=change
            greatest_decrease_month=row[0]
        
        last = int(row[1]) 
    #equation for our average change in profits
    average_change="$" + str(round(total_change/ (months-1),2)) 

    

#printing of pertient info to the terminal as well as to a txt file
with open("Analysis/PyBank.txt", "w") as txt_file:
    title="Financial Analysis\n------------"
    print(title)
    txt_file.write(title + "\n")

    output_total_months="Total Months: " + str(months) 
    print(output_total_months)
    txt_file.write(output_total_months + '\n')

    output_net_total="Total: " "$" + str(total_profit_losses)
    print(output_net_total)
    txt_file.write(output_net_total +'\n')


    output_average_change= 'Average Change: ' + (average_change)
    print(output_average_change)
    txt_file.write(output_average_change + '\n')

    
    output_highest_increase= ("Greatest Increase in Profits: " + greatest_increase_month + " " + "$" + str(greatest_increase))
    print (output_highest_increase)
    txt_file.write(output_highest_increase +'\n')

    output_highest_decrease= (("Greatest Decrease in Profits: " + greatest_decrease_month + " " + "$" + str(greatest_decrease)))
    print (output_highest_decrease)
    txt_file.write(output_highest_decrease)















