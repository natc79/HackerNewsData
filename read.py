import pandas as pd

#This reads in the stories headlines f
hn_stories = pd.read_csv("hn_stories.csv")
hn_stories.columns = ["submission_time","upvotes","url","headline"]
print(hn_stories.head())
def load_data():
   return(hn_stories)