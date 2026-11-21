# Challenge: Add a Singer
# Adding a singer is two separate tasks: 1) prompt the host for a name and a song, and
# 2) append that singer to the queue. Write a function for each:

# 1. Write prompt_for_singer():
#    - Ask the host for a name and a song
#    - The function should return the name and the song, title cased and stripped of any extra spaces
#    - A function can return two values at once if you separate them with a comma:
#      `return name, song`. You unpack them the same way you would a tuple. 

# 2. Fill in the add_singer() function:
#    - Call prompt_for_singer(), unpack what comes back, and save to variables
#    - Add the singer and their song to the end of the queue
#    - Print a message confirming the singer was added

# Example output: 

# Current Queue:

# Annie - Dancing Queen
# Allen - Country Roads

# Options: add / remove / quit
# > add

# Name:    mike reed
# Song: LET IT BE

# Added Mike Reed to the queue.

# Current Queue:

# Annie - Dancing Queen
# Allen - Country Roads
# Mike Reed - Let It Be

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

# prompt for singer 
def prompt_for_singer():
  print()
  name = input("Name: ").strip().title()
  song = input("Song: ").strip().title()
  return name, song

# Function stubs go here
def add_singer(queue):
  """Ask for the singer and add them to the queue"""
  name, song = prompt_for_singer()
  queue.append((name, song)) # I CAN USE THE FUKING APPEND HERE BUT I FORGOT THAT AND VS CODE DIDNT GIVE ME THE OPTION AAAAAHHHH!!!!
  print()
  print(f"Added {name} to the queue.")


def remove_singer(queue): 
  """Remove singer fron the queue"""
  print("[remove a singer]")

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
      # your commands go here 
      elif command == "add": 
        add_singer(queue)
      elif command == "remove":
        remove_singer(queue)
      else: 
        print(f"Sorry, I don't know the command '{command}'")

run_app(queue)
