# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join(".", "Resources", "election_results.csv")
# print(file_to_load)

# print(file_to_load)
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']

candidate_votes = {'Charles Casper Stockham':0, 
                    'Diana DeGette':0, 
                    'Raymon Anthony Doane':0}


# 1: Create a county list and county votes dictionary.
county_list = ['Jefferson', 'Denver', 'Arapahoe']
county_votes = {'Jefferson':0,
                'Denver':0,
                'Arapahoe':0}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.

largest_county = ""
vote_count = 0
turnout_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
        # print(row)
        # Add to the total vote count
        total_votes = total_votes + 1
        
        # print(total_votes)
        # Get the candidate name from each row.
        candidate_name = row[2]
        # print(candidate_name)
        # 3: Extract the county name from each row.
        county_name = row[1]
        # print(county_name)
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.


        candidate_votes[candidate_name] += 1


        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

        # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
            print(county_name)

        # 4c: Begin tracking the county's vote count.
        # county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
        # print(county_votes[county_name])


largest_county = max(county_votes, key=county_votes.get)
# print(largest_county)
county_perc={}
to_output_county=[]
to_output_candidate=[]

for dict_county_name in county_votes:
    # print(dict_county_name)

    # 6b: Retrieve the county vote count.
    dict_county_votes = county_votes[dict_county_name]
    

    # 6c: Calculate the percentage of votes for the county.
    county_percentages = float((dict_county_votes/total_votes)*100)

    county_perc[str(dict_county_name)]=county_percentages
    # final[dict_county_name]['Percentage']=county_percentages


    # 6d: Print the county results to the terminal.
    to_output_county.append(f"{dict_county_name}: {county_perc[dict_county_name]:.1f}% ({total_votes:,})")
#     print(f"{dict_county_name}: with {county_percentages} % of votes and {total_votes} total_votes")
for candidate_name in candidate_votes:


    # Retrieve vote count and percentage
    votes = candidate_votes.get(candidate_name)
    vote_percentage = float(votes) / float(total_votes) * 100
    to_output_candidate.append(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

print(winning_candidate)
election_results = (f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
        # f"{dict_county_name}: {county_perc[dict_county_name]:.1f}% ({total_votes:,})\n"
        f"{to_output_county[0]}\n"
        f"{to_output_county[1]}\n"
        f"{to_output_county[2]}\n"
        f"-------------------------\n\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n\n"
        f"{to_output_candidate[0]}\n"
        f"{to_output_candidate[1]}\n"
        f"{to_output_candidate[2]}\n"

        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {candidate_votes.get(winning_candidate)}\n"
        f"Winning Percentage: {winning_percentage}\n"
        f"===============================\n"

print(election_results, end="")
