import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")
# Read in the CSV file
with open(csvpath, encoding = 'utf8') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader, None)  # skip the headers

    total_months = 0
    net_total_amount = 0
    total_change = 0
    previous = 0
    change = 0
    max_change_amt = 0
    min_change_amt = 0
    max_change_date = ''
    min_change_date = ''
    
    for row in csvreader:
# The total number of months included in the dataset
        total_months += 1 
        


# The net total amount of "Profit/Losses" over the entire period
        net_total_amount += int(row[1])
        
   
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
        if previous != 0:
            total_change += int(row[1]) - previous
            change = int(row[1]) - previous
# The greatest increase in profits (date and amount) over the entire period
            if change > max_change_amt:
                max_change_amt = change
                max_change_date = row[0]
# The greatest decrease in profits (date and amount) over the entire period
            if change < min_change_amt:
                min_change_amt = change
                min_change_date = row[0]

        previous = int(row[1])
    average_change = round(total_change / (total_months - 1),2)

    print("Financial Analysis")
    print("-" * 20)
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total_amount}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {max_change_date} (${max_change_amt})') 
    print(f'Greatest Decrease in Profits: {min_change_date} (${min_change_amt})')

# writing into a text file

with open('analysis/kok_PyBank_results.txt','w') as f:
    
    f.write("Financial Analysis\n")
    f.write("-" * 20)
    f.write(f'\nTotal Months: {total_months}\n')
    f.write(f'Total: ${net_total_amount}\n')
    f.write(f'Average Change: ${average_change}\n')
    f.write(f'Greatest Increase in Profits: {max_change_date} (${max_change_amt})\n') 
    f.write(f'Greatest Decrease in Profits: {min_change_date} (${min_change_amt})\n')

      




