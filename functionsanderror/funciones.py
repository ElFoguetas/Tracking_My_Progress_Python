# Challenge: Write some functions!
# You've very generously decided to pick up coffee for six of your favorite coworkers this morning. 

# 1. Write a function announcing your coffee run. 
# Example output: "I am headed to the coffee shop! Who wants a latte?"

# 2. Write a function to calculate the total cost if you buy them each a latte for $5. In an f string, print how many lattes and what the total comes to.  
# Example output: 
# 6 lattes comes to $30.

# 3. Your coworkers thank you profusely. To save a little time, write a function that prints "You're welcome!" twice, then call it as many times as you need to thank all six coworkers. 

# 4. Put all your function calls in a new function called coffee_run(), and call it to start your coffee run!

LATTE_COST = 5
num_coworkers = 6

def coffe_coworkers():
    print("I am headed to the coffee shop! Who wants a caramel macchitato?")

def coffe_total_cost():
    total_latte = LATTE_COST * num_coworkers
    print(f"{num_coworkers} comes to ${total_latte}")

def twice_welcome():
    print("Your welcome!!")
    print("Your welcome!!")

def coffe_run():
    coffe_coworkers()
    coffe_total_cost()

    num_thanks = 1
    while num_thanks <= num_coworkers:
        twice_welcome()
        num_thanks += 1

coffe_run()
    
    