import numpy as np
import random
import csv

height = np.array([random.gauss(0,1)*20 +160 for x in range(100)])
weight = np.array([random.gauss(0,1)*10 +60 for x in range(100)])

bmi = weight / (height*0.01)**2

is_fat = []
for element in bmi:
    if element > 28:
        is_fat.append(True)
    else:
        is_fat.append(False)

# print(is_fat)


import csv


with open('data.csv', 'w', encoding="utf8", newline='') as csvfile:
    w = csv.writer(csvfile, delimiter=',')
    for x in range(100):
        w.writerow([height[x],weight[x],is_fat[x]])