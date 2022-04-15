import time


time_intervals = []

work_int = input('Work interval (seconds): ')
break_int = input('Break interval (seconds): ')

n = 0
while n < 3:
    time_intervals.append(work_int)
    time_intervals.append(break_int)
    n += 1

long_break_int = input('Long break interval (seconds): ')
time_intervals.append(long_break_int)

print(time_intervals)
print(time_intervals[0:5:2])

