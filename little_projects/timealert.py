from datetime import datetime
import time as tm
from time import sleep

import pygame

def set_alarm():

    running = True

    alarm_time_ = input("Please put an alarm on this format HH:MM:SS ")

    while running:
        tm.sleep(1)
        now_ = datetime.now().strftime("%H:%M:%S")

        print(now_)

        if now_ == alarm_time_:

            print("It's time to wake up")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                tm.sleep(1)

            running = False


if __name__ == "__main__":
    sound_file = "sound.mp3"
    set_alarm()