# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv") 
# Sssing a variable to save the fole to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter. 
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_porcentage = 0

# Open the election results and read the file,
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read the header row 
    headers = next(file_reader)

#Print each row in the CSV file.
    for row in file_reader:
    # Add to the total vote count. 
        total_votes += 1

# Print the candidates name from each row 
        candidate_name = row[2]

        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list. 
           candidate_options.append(candidate_name)
        # Begin tracking that candidate's vote count. 
           candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Interate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrive vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_porcentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count, and porcentage of 
        # vote to the terminal.
        print(f"{candidate_name}: {vote_porcentage:.1f}% ({votes:,})\n")

        # Determine the winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_porcentage > winning_porcentage):
            # If true then set winning count = votes and winning _porcent =
            # vote porcentage.
            winning_count = votes
            winning_porcentage = vote_porcentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        # To do: print out the winning candidate, vote count and percentage to
        # terminal
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Porcentage: {winning_porcentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    


