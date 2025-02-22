# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
total_votes = len(data)

# Define lists and dictionaries to track candidate names and vote counts
candidates = data['Candidate'].unique()

# Winning Candidate and Winning Count Tracker
candidates = data['Candidate'].unique()
votes_per_candidate = data['Candidate'].value_counts()


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        percentage_votes = (votes_per_candidate / total_votes) * 100

        # Get the candidate's name from the row


        # If the candidate is not already in the candidate list, add them


        # Add a vote to the candidate's count


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)


    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary
    winner = votes_per_candidate.idxmax()
winner_votes = votes_per_candidate.max()

    # Save the winning candidate summary to the text file
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
        for candidate in candidates:
    print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes_per_candidate[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
