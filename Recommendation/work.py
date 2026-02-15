from datetime import datetime
from time import time
import pandas as pd

data=pd.read_csv("netflix.csv")
data=data.rename(columns={"date_added":"Date Added","release_year":"Release Year"})

# print(data['Date Added'].dtype)
# print(data['Date Added'].head())
data['duration']=data["duration"].astype(time)
print(data['duration'].dtype)