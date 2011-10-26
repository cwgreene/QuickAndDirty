import sys
import re
import time
import optparse

def get_time(line):
    print line
    match = re.findall("([A-Za-z]{3} [0-9]{2} ([0-9]{2}:?){3})",line)
    timestamp = match[0][0]
    timestruct = time.strptime(timestamp+" 2011","%b %d %H:%M:%S %Y")
    timefloat = time.mktime(timestruct)
    return timefloat


def interval(start_tag,end_tag,afile,options):
    start = False
    start_time,end_time=0,0
    time_list = []
    errors=0
    for line in afile:
        if options.filter and not re.findall(options.filter,line):
            continue
        if start == False:
            if re.findall(start_tag,line):
                start = True
                start_time = get_time(line)
        else:
            if re.findall(start_tag,line):
                print "Oops!"
                print line
                errors+=1
                start = True
                start_time = get_time(line)
            if re.findall(end_tag,line):
                start = False
                end_time = get_time(line)
                interval = end_time-start_time
                print interval
                time_list.append(interval)
    time_list=filter(lambda x:x>=0,time_list)
    print "errors",errors
    print sum(time_list)/len(time_list)

def main(args):
    parser = optparse.OptionParser()
    parser.add_option("-f",dest="filter",default=None)
    options,args = parser.parse_args(args)
    if len(args)==2:
        interval(args[0],args[1],sys.stdin,options)

if __name__=="__main__":
    main(sys.argv[1:])
