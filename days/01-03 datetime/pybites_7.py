from datetime import datetime
import os
import urllib.request


def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """  
    timestamp = line.split()[1]
    line_datetime = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
    return line_datetime


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    L = [l for l in loglines if SHUTDOWN_EVENT in l]
    diff = [convert_to_datetime(y) - convert_to_datetime(x) for x,y in zip(L,L[1:])]
    #L=[]
    #for line in loglines:
    #    if SHUTDOWN_EVENT in line:
    #        dt = convert_to_datetime(line)
    #        L.append(dt)
    #diff = [y - x for x,y in zip(L,L[1:])] 
    return diff


# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

SHUTDOWN_EVENT = 'Shutdown initiated'

with open(logfile) as f:
    loglines = f.readlines()
    
    print(time_between_shutdowns(loglines))
