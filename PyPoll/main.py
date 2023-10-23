import pandas as pd

file_path = "election_data.csv"
election_data = pd.read_csv(file_path)

total_votes = len(election_data)

candidate_votes = election_data["Candidate"].value_counts().reset_index()
candidate_votes.columns = ["Candidate", "Vote Count"]

candidate_votes["Vote Percentage"] = (candidate_votes["Vote Count"] / total_votes) * 100

winner = candidate_votes["Candidate"].iloc[0]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(candidate_votes.to_string(index=False))
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_file = "election_results.txt"
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    file.write(candidate_votes.to_string(index=False) + "\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print(f"Results have been saved to {output_file}")
