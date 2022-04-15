# Pomodoro Timer:

# import the time module
import time


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')

time_intervals = (10,2,10,2,10,2,10,5)

for time in time_intervals:

# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
