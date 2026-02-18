from time import time
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\user\Desktop\Projects\AI\Data\netflix.csv")

movies=data[data['type']=="Movie"].shape[0]
# print(data['type'].unique())
print(movies)