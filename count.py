import read
import collections

#This counts the 100 most popular words in headlines
hn_stories = read.load_data()
strheadlines = ""
for i in hn_stories["headline"]:
    #print(i)
    strheadlines = strheadlines + str(i)

strheadlines = str.lower(strheadlines)
data = strheadlines.split(" ")
print(collections.Counter(data).most_common(100))




