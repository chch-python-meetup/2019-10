from collections import Counter 
import string
import numpy as np
import matplotlib.pyplot as plt

with open('treaty.txt') as f:
  f = f.read().lower()
  f = f.strip(string.punctuation)
  f = f.replace("(","").replace(")","").replace("[","").replace("]","").replace(" - ","")
  f = f.split()


# build list of words with greater then a count of 1.
cnt = Counter()
for word in f:
    cnt[word] += 1
    
finalCnt = Counter()
for item in cnt:
    if cnt[item] > 1:
       finalCnt[item] = cnt[item] 
    
# set up plots.
labels, values = zip(*finalCnt.most_common())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels, rotation=90)
plt.show()