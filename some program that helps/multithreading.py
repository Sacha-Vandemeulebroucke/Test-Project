#multithreading = Used to perform multiple tasks concurrently (multitasking)
#                 Good for I/O bound tasks like reading files or fetching data from APIs
#                 threading. Thread(target=my_function)

import threading
import time

def walk_dog(name, lastname):
    time.sleep(8)
    print(f"You finish walking the dog {name} {lastname}")

def take_out_trash(location):
    time.sleep(2)
    print(f"You take out the {location} trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# walk_dog()
# take_out_trash()
# get_mail()

chore1 = threading.Thread(target=walk_dog, args=("Rantanplan","Dodoo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash,args=("inside",))
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print('All chores are complete')