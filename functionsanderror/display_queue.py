# Challenge: Display the Queue
# Replace show_queue()'s placeholder code with working code: 
# 1. Add a header that says "Current Queue:". Give it some visual space by adding a blank
#    line above and below.
# 2. Loop over the queue and print each singer's name and song. 
# 3. Move the options menu into show_queue(), since we want to keep display items together and show the options menu each time we show the queue. 

# Example output:

# ============================================
# Welcome to Sing Out: A Karaoke Queue Manager
# ============================================

# Current Queue:

# Annie - Dancing Queen
# Allen - Country Roads

# Options: add / remove / quit
# >

queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def show_queue(queue):
  """Print everyone currently in the queue"""
  print("")
  print("Current Queue:")

  for songs in queue:
    artist, song = songs
    print(f"{artist} - {song}")

  print("")
  print("Options:  add / remove / quit")

# Function stubs go here
def add_singer(queue):
  """Ask for the singer and add them to the queue"""
  print("[add a singer]")


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
