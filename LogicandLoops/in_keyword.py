# Challenge: Raffle Drawing
# Build a feature that manages a charity raffle. The program picks a random winner but
# makes sure nobody wins twice. If the random winner has already won a prize, keep 
# drawing a random winner until you land on someone new.
# 1. Draw a random name from entrants.
# 2. If that name is already in winners, keep drawing until you get one
#    that isn't.
# 3. Add the new winner to winners and print: "Winner: <name>"

import random

entrants = ["Amara", "Diego", "Priya", "Leo", "Sofia", "Kwame"]
winners = ["Diego", "Sofia"]

pick_winner = random.choice(entrants)

while pick_winner in winners:
    pick_winner = random.choice(entrants)

print(f"The winner is {pick_winner}")
winners.append(pick_winner)