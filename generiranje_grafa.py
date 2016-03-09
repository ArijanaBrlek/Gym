import scipy as sp
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

db = pd.read_csv("db.csv")
n = sum([1 if c == "+" else 0 for c in db.ix[:,1]])
a = sum([1 if c == '+' else 0 for c in db.ix[:,2]])

plt.figure(figsize=(17,10))
plt.xlim([0,1])
plt.ylim([0, np.max([a,n])+3])
bar_width = 0.2

rects1 = plt.bar(0.3, n, bar_width, color='b', label='Nino')
rects2 = plt.bar(0 + bar_width + 0.3, a, bar_width, color='r', label='Arijana')

plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off') 
plt.legend()
plt.savefig("graph.png")
