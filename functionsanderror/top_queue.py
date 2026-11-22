## Challenge: Move a Singer to the Top of the Queue

# Moving a singer to the top is two steps:
#  1) take them out of their current position, and
#  2) insert them at the beginning of the queue.

# 1. Write move_to_top(queue):
#    - Ask the host which position they want to move, and convert their answer to a number
#    - Take that singer out of the queue with .pop(). Watch for an off-by-one error: the queue starts at 1 for the host, but Python starts counting at 0, so position 1 is
#      index 0. Pass the host's number minus one as the argument to .pop()
#    - Put the singer back at the front of the queue with .insert()
#    - Print a message announcing who moved to the top

# 2. Call move_to_top in the app loop so the host can run the command, and add "top" to the Options menu.

# Here's what your output should look like:

# Current Queue:

# 1. Annie - Dancing Queen
# 2. Allen - Country Roads

# Options: add / next / top / remove / quit
# > top

# Who do you want to move to the top? Enter a number: 2

# Moved Allen to the top of the queue!

# Current Queue:

# 1. Allen - Country Roads
# 2. Annie - Dancing Queen

queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def show_queue(queue):
  """Print everyone currently in the queue"""
  print()
  print("Current queue:")
  print()
  for i, singer in enumerate(queue):
    name, song = singer
    print(f"{i + 1}. {name} - {song}")
  print()
  print("Options:  add / next / top / remove / quit")

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

def next_singer(queue):
  name, song = queue.pop(0)
  print()
  print(f"NOW UP: {name} - {song}")

# add move_to_top 
def move_to_top(queue):
  move_top = int(input("Who do you want to move to the top? Enter a number: "))
  name, song = queue.pop(move_top-1)
  queue.insert(0, (name, song))
  print()
  print(f"Moved {name} to the top of the queue!")

def remove_singer(queue):  
  """Remove singer fron the queue"""
  name = input("Who do you want to remove? ").strip().title()
  print()
  for singer in queue:
    if singer[0] == name:
      queue.remove(singer)
      print(f"Removed {name} from the queue.")
      return 
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
      elif command == "next":
        next_singer(queue)
      elif command == "top":
        move_to_top(queue)  
      elif command == "remove":
        remove_singer(queue)
      else: 
        print(f"Sorry, I don't know the command '{command}'")

run_app(queue)
