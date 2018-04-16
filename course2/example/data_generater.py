import numpy as np
import random
import csv

# data generation
data_number = 1000

height = np.array([random.gauss(0, 1)*20 +150 for x in range(data_number)])
weight = np.array([random.gauss(0, 1)*10 +60 for x in range(data_number)])

bmi = weight * height * 0.01

# generate label "is_fat", then store data in a list
is_fat = []
for element in bmi:
    if element > 80:
        is_fat.append(True)
    else:
        is_fat.append(False)

# write a csv file, row by row
with open('data.csv', 'w', encoding="utf8", newline='') as f:
    w = csv.writer(f, delimiter=',')
    for x in range(data_number):
        w.writerow([height[x], weight[x], is_fat[x]])