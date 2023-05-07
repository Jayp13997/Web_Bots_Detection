import os
from datetime import datetime, timezone
import re
from statistics import stdev


#threshhold for human or bot identifier
threshold = 0.20

def get_time_list(log_file):
    time_list = []
    file = open(log_file, 'r')
    lines = file.readlines()
    #print(lines)
    #print(log_file)
    #print('length of lines: ' + str(len(lines)))
    
    for line in lines:
        #get next line
        # line = file.readline()
        #print(line)
        #find the date time part in the line
        r = re.findall("[\d]{1,2}\/[ADFJMNOS]\w*\/[\d]{4} [0-2][0-9]:[0-5][0-9]:[0-5][0-9]", line)
        #print(r)
        #if the line has date time part, add the time to the list
        if len(r) > 0:
            #print('found a line with date time')
            time = datetime.strptime(r[0], "%d/%b/%Y %H:%M:%S").astimezone(timezone.utc)
            time_list.append(time)

    return time_list

#identify if log_file is human or bot 
def identify(log_file):
    #get list of time from log_file
    time_list = get_time_list(log_file)
    #print(time_list)
    time_interval_list = []

    for i in range (len(time_list)):
        if i+1 < len(time_list):
            interval = (time_list[i + 1].astimezone(timezone.utc) - time_list[i].astimezone(timezone.utc)).seconds
            time_interval_list.append(interval)
    # #get distinct/unique number of intervals
    # time_interval_set = set(time_interval_list)
    # #print(time_interval_list)
    # if len(time_interval_set) <= threshold:
    #     return 0
    # else:
    #     return 1
    interval_std = abs(1 - stdev(time_interval_list))
    #print(interval_std)

    if interval_std <= threshold:
        return 0
    else:
        return 1



#get list of log_files 
log_file_list = os.listdir('Logs/')

total_files = 0
correctly_identified = 0

for log_file in log_file_list:
    if 'bot_random' in log_file or 'human' in log_file:
        total_files += 1
        file_identified = identify('Logs/' + log_file)
        if 'human' in log_file and file_identified == 1:
            print('Correctly identified: ' + log_file)
            correctly_identified += 1
        elif 'bot' in log_file and file_identified == 0:
            print('Correctly identified: ' + log_file)
            correctly_identified += 1
        else:
            print('Incorrectly identified: ' + log_file)

correctness_per = (correctly_identified/total_files) * 100
print('success rate: ' + str(correctness_per) + '%')



