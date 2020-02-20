#create a pomodoro (tomato) timer, 25 min 
from datetime import datetime, timedelta, time
import time as tm
import sys


tomato = timedelta(minutes=25)

start_time = datetime.now()
t = time(hour=start_time.hour,minute=start_time.minute,second=start_time.second)
end_time = start_time + tomato
end_time = time(hour=end_time.hour,minute=end_time.minute,second=end_time.second)
print("Start time:  " + str(t))
print("End time:  " + str(end_time))

for remaining in range(24, 0, -1):
    min_remain = remaining
    for remaining in range(59, 0, -1):
        curr_time = datetime.now()
        display_time = time(hour=curr_time.hour,minute=curr_time.minute,second=curr_time.second)
        clock = time(minute=min_remain, second=remaining)
        #replaces line instead of new line
        sys.stdout.write("\r")
        sys.stdout.write("{} time remaining...".format(clock))
        sys.stdout.write("Current time: {}".format(display_time))
        sys.stdout.flush()
        tm.sleep(1)

sys.stdout.write("\rComplete!                  \n")
