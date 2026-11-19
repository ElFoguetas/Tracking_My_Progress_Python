name_event = input("Where did you go now? ")
cost = input("How much did you spend? (Enter a whole number like 300) ")
service_charges = input("Did you leave any tip? ")
group_size = input("How many people were with you? ")
grand_total = 300
person_pay = 300

# Por razones obvias en las que no puedes hacer operaciones matematicas con Strings los valores: grand_total y person_pay
# Estaran hardcoded solo por esta vez

print("Welcome to PayUp!")
print("")
print(f"Here's the breakdown for {name_event}: ")
print("")
print(f"Cost: {cost}")
print(f"Service Charges: {service_charges}")
print(f"Group Size: {group_size}")
print(f"Grand Total: {grand_total}")
print("")
print(f"Each person must PayUp: {person_pay}")