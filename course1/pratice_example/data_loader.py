import csv
import numpy as np


def data_loader(path="data.csv",start_line=0,end_line=100):
    x = np.zeros((2, 100))
    y = np.zeros(100)

    with open(path,'r',encoding='utf8') as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        rows = [row for idx, row in enumerate(r) if idx in range(start_line, end_line)]

        for idx, row in enumerate(rows):
            try:
                x[0, idx] = row[0]
                x[1, idx] = row[1]

                if row[2] == "False":
                    y[idx] = 0
                else:
                    y[idx] = 1
            except IndexError:
                continue

    data_set = x, y
    return data_set
