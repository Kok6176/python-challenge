import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")
# Read in the CSV file
with open(csvpath, encoding = 'utf8') as csvfile:

    # writing into a text file

    with open('analysis/kok_PyPoll_results.txt','w') as f:

        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')

        header = next(csvreader, None)  # skip the headers

        total_votes = 0
        election_dict = {"candidates" : [],
                        "c_total_votes" :[]
                        }
        

        print("Election Results")
        f.write("Election Results\n")

        print('-' * 30)
        f.write('-' * 30)

        for row in csvreader:
        # The total number of votes cast
            total_votes += 1
        # A complete list of candidates who received votes
            if len(election_dict["candidates"]) == 0 or row[2] not in election_dict["candidates"]:
                election_dict["candidates"].append(row[2])
                election_dict["c_total_votes"].append(1)
            else:
                index = election_dict["candidates"].index(row[2])
                election_dict["c_total_votes"][index] += 1
        print(f"Total Votes: {total_votes}")
        f.write(f"\nTotal Votes: {total_votes}\n")

        print('-' * 30)
        f.write('-' * 30)
        f.write('\n')

        max_votes = 0
        for index,item in enumerate(election_dict["candidates"]):
            # The percentage of votes each candidate won
            percent = round(election_dict["c_total_votes"][index] / total_votes * 100, 3)

            # The total number of votes each candidate won
            print(f'{election_dict["candidates"][index]}: {percent}% ({election_dict["c_total_votes"][index]})')
            f.write(f'{election_dict["candidates"][index]}: {percent}% ({election_dict["c_total_votes"][index]})\n')

            # The winner of the election based on popular vote
            if election_dict["c_total_votes"][index] > max_votes:
                max_index = index
                max_votes = election_dict["c_total_votes"][index]
        
        print('-' * 30)
        f.write('-' * 30)

        print(f'Winner: {election_dict["candidates"][max_index]}')
        f.write(f'\nWinner: {election_dict["candidates"][max_index]}\n')

        print('-' * 30)
        f.write('-' * 30)

    

    
    
    
    


    
    

















