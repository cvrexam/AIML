import pandas as pd
import numpy as np

data = pd.read_csv("dataset.csv")
#data = pd.read_csv()
print(data)

a = np.array(data.iloc[:, :-1])
print(a)

t = np.array(data.iloc[:, -1]) 
print(t)

def find_s_algorithm(c, t):
    specific_hypothesis = None
    for i, val in enumerate(t):
        if val == "Y":
            specific_hypothesis = c[i].copy()
            break
    if specific_hypothesis is None:
        return "No positive example found"
    
    for i, val in enumerate(c):
        if t[i] == "Y":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
    return specific_hypothesis

print("The final hypothesis is:", find_s_algorithm(a, t))

