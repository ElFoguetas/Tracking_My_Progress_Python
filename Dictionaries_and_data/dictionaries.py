# Challenge: Cutest Pet Contest

# Stored in the vote_tally dictionary are the final tallies for a cutest pet contest.

# 1. Find the first and second place pets in the tally, and save each name to
#    a variable. Use the variables as keys to look up each pet's votes, and print the
#    results.

#    Expected output: 
#    Winner: Snuggles with 4821 votes
#    Second place: Walter with 3967 votes

# 2. Prompt for a pet name, then print that pet's vote count.

#    Expected output:
#    Get vote count for: Cinnamon
#    Cinnamon got 1588 votes.

vote_tally = {
    "Snuggles": 4821,
    "Walter": 3967,
    "Duke": 2140,
    "Cinnamon": 1588,
    "Fluff": 312,
}

first_place = vote_tally["Snuggles"]
second_place = vote_tally["Walter"]

print(f"Winner: Snuggles with {first_place} votes")
print(f"Second place: Walter with {second_place} votes")

pet_name = input("Get vote count for: ").strip().title()
vote_count = vote_tally[pet_name]

print(f"{pet_name} got {vote_count} votes")