# Challenge: Create the output display for the PayUp app.

# 1. Check out the example output in `example_output.md`
# 2. Define a variable for each item: event name, cost, service charge,
#    group size, grand total, and total per person. Use made-up values for now —
#    we'll do the math later!
# 3. Build the display line by line using print() and f-strings. 
#    Remember: an empty print() creates a blank line.
# 4. Run it and make sure it matches the example.

cost = 300
service_charges = 30
group_size = 3
grand_total = cost + service_charges
person_pay = grand_total / group_size

print("Welcome to PayUp!")
print("")
print("Here's the breakdown for dinner at Fantastic Pizza: ")
print("")
print(f"Cost: {cost}")
print(f"Service Charges: {service_charges}")
print(f"Group Size: {group_size}")
print(f"Grand Total: {grand_total}")
print("")
print(f"Each person must PayUp: {person_pay}")