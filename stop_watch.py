import os
import time

# Simple Stopwatch Using Python


def instruction(word) :

    start_time = time.time()
    end_time = time.time()

    print('Press ENTER to begin, Press CTRL+C to exit the stopwatch')
    choice = input()
    if choice.upper() == 'Enter'.upper() :
        start(start_time)
    else :
        print('INVALID')


def start(begin) :
    
    second = 0
    minute = 0
    hours = 0

    while True :
        print("\n\n\n\n\n\n\n")
        print("\t\t\t\t------------")
        print(f"\t\t\t\t {hours} : {minute} : {second} ")
        # print('\t\t\t\t  %d : %d : %d ' %(hours, minute, second))
        print("\t\t\t\t------------")
        # Wait for 1 second
        time.sleep(1)
        second+=1
        if second == 60 :
            second = 0
            minute+=1
        elif minute == 60 :
            minute = 0
            hours+=1
        os.system ('cls')

print("Simple Stopwatch (in python) Created by Kelly Ovbiye...\n")
instruction('word')
