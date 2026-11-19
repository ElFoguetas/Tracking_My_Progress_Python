name_event = input("Where did you go now? ")
cost = float(input("How much did you spend? (Enter a whole number like 300) "))
service_charges = int(input("Did you leave any tip? ").strip("%"))
group_size = int(input("How many people were with you? "))
service_charge_total = float(cost * service_charges / 100)
grand_total = cost + service_charge_total
person_pay = grand_total / group_size

print("Welcome to PayUp!")
print("")
print(f"Here's the breakdown for {name_event}: ")
print("")
print(f"Cost: {cost:.2f}")
print(f"Service Charges: {service_charge_total:.2f}")
print(f"Group Size: {group_size}")
print(f"Grand Total: {grand_total:.2f}")
print("")
print(f"Each person must PayUp: {person_pay:.2f}")