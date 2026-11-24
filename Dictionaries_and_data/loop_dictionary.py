# Challenge: Go for Run
# A dictionary stores how many miles you ran each day:

run_log = {
    "monday": 2,
    "tuesday": 4,
    "wednesday": 5,
    "thursday": 4,
    "friday": 0,
}

# 1. Loop over the dictionary and print a log:

# Expected output:
# On Monday I ran 2 miles.
# On Tuesday I ran 4 miles.
# On Wednesday I ran 5 miles.
# On Thursday I ran 4 miles.
# On Friday I ran 0 miles.

# 2. Loop over the dictionary again and print the total miles for the week.
#    Hint 1: Initialize a variable to hold a running total. As you loop over the dictionary, add each value to the running total.

# Expected output:
# Total miles this week: 15

for day, miles in run_log.items():
    print(f"On {day} I ran {miles} miles.")

total_miles = 0
for day, miles in run_log.items():
    total_miles += miles
print(f"Total miles this week: {total_miles}")