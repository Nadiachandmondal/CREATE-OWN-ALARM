from audioplayer import AudioPlayer
import time

clear = "\033[2J"
clear_and_return = "\033[H"
def alarm(sec):
    counter = 0
    print(clear)
    while counter<sec:
        time_left = sec - counter
        print(f"{clear_and_return}{time_left} sec left")
        time.sleep(1)

        counter = counter + 1
        
alarm(10)
AudioPlayer("audio5.mp3").play(block=True)