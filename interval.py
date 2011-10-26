mport sys
import re
import time

def get_time(line):
    print line
    match = re.findall("([A-Za-z]{3} [0-9]{2} ([0-9]{2}:?){3})",line)
    timestamp = match[0][0]
    timestruct = time.strptime(timestamp+" 2011","%b %d %H:%M:%S %Y")
    timefloat = time.mktime(timestruct)
    return timefloat


def interval(start_tag,end_tag,afile):
    start = False
    start_time,end_time=0,0
    time_list = []
    for line in afile:
        if start == False:
            if re.findall(start_tag,line):
                start = True
                start_time = get_time(line)
        else:
            if re.findall(end_tag,line):
                start = False
                end_time = get_time(line)
                interval = end_time-start_time
                print interval
                time_list.append(interval)
    print sum(time_list)/len(time_list)

if len(sys.argv)==3:
    interval(sys.argv[1],sys.argv[2],sys.stdin)
~                         
