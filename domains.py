import read
import collections

#This code analyzes the most poplar domain names
#The second part removes subdomains and redoes the count
hn_stories = read.load_data()
domains = hn_stories["url"]
print(collections.Counter(domains).most_common(10))

domains2=domains.tolist()

nosubdomains = []
for i in domains2:
    i = str(i)
    cnt =  i.count(".")
    if cnt >= 2:
        newstr = i.split(".",1)[1]
        nosubdomains.append(newstr)
    else:
        nosubdomains.append(i)
        
print("Removed subdomains", collections.Counter(nosubdomains).most_common(10))
        