# Challenge: Remove a Singer
# Find the singer in the queue and remove them. 

# In the `remove_singer()` function: 
# 1. Prompt the host for who to remove. Clean the input: title-cased, no extra spaces. 
# 2. Loop through the queue looking for a matching singer name. Each singer is a (name, song) tuple, so compare against the name inside the tuple rather than the tuple itself. Check hints.md
#    if you need help!
# 3. If you find a match, remove the whole tuple with .remove(), print a confirmation and return.
# 4. If the loop finishes without a match, print a message telling the host no match was found. 

# Example output:

# > remove
# Who do you want to remove? allen

# Removed Allen from the queue.

# > remove
# Who do you want to remove? sarah

# There's no one named Sarah in the queue.

queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def show_queue(queue):
  """Print everyone currently in the queue"""
  print()
  print("Current queue:")
  print()
  for singer in queue:
    name, song = singer
    print(f"{name} - {song}")
  print()
  print("Options:  add / remove / quit")

def prompt_for_singer():
  """Ask for a name and a song, and return them cleaned up."""
  name = input("Name: ").strip().title()
  song = input("Song: ").strip().title()
  return name, song

def add_singer(queue):
  """Ask for the singer and add them to the queue"""
  name, song = prompt_for_singer()
  queue.append((name, song))
  print()
  print(f"Added {name} to the queue.")

# MENTAL ADVICE
def remove_singer(queue): 
  """Remove singer fron the queue"""
  name = input("Who do you want to remove: ").strip().title()
  print()
  for artist in queue: # HERE YOU ARE ACCESSING THE ENTIRE ELEMENT OF THE TUPLE
    if artist[0] == name: # HERE YOURE ACCESSING THE FIRST ELEMENT OF THE ENTIRE ELEMENT
      singer, song = artist # HERE YOU COULD REMOVE THE ELEMENT EARLIER ITS NOT NECESSARY TO UNPACK AGAIN THE TUPLE
      if singer == name:
        queue.remove(artist)
        print(f"Removed {name} from the queue.")
        return
  else:
        print(f"There's no one named {name} in the queue.")  

def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True 

    while is_running: 
      show_queue(queue)
      command = input("> ")

      if command == "quit": 
        is_running = False
        print("The queue is closed. Good night!")
      elif command == "add": 
        add_singer(queue)
      elif command == "remove":
        remove_singer(queue)
      else: 
        print(f"Sorry, I don't know the command '{command}'")

run_app(queue)
