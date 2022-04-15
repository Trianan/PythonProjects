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


time_intervals = (10,2,10,2,10,2,10,15)
for interval in time_intervals:
    t = interval

    if t == 10:
        print('Work for 25 minutes.')
    elif t == 2:
        print('Break-time for 5 minutes.')
    elif t == 15:
        print('Break-time for 30 minutes.')
    else:
        print('unusual time interval')

    countdown(int(t))