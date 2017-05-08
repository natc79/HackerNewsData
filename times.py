import read
import collections
from dateutil.parser import parse

#This code analyzes the most common times articles are submitted
hn_stories = read.load_data()
time = hn_stories["submission_time"]

#Test
temp = hn_stories["submission_time"][1]
dateobj = parse(temp)
print(temp, dateobj, "hour:", dateobj.hour)

def extract_hour(datestr):
    dateobj = parse(datestr)
    return(dateobj.hour)
    
hours = hn_stories["submission_time"].apply(extract_hour)

print(hours.value_counts())