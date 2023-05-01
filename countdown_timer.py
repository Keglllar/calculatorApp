# import time module
import time
import os

def countDown(time_length) :

    while time_length :
        mins, secs = divmod(time_length, 59)
        timer = ' {:02d} : {:02d} '.format(mins, secs)
        print(timer)

        # wait for 1 sec
        time.sleep(1)
        time_length -= 1
        if time_length == 1 :
            secs = 58
            mins -= 1
        elif mins == 0 and secs == 1 :
            print('Time Up!!')
    
# user input the length of the countdown in seconds
time_length = input('Enter time length: ')
# Function call
countDown(int(time_length))
