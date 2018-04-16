import csv
import numpy as np

def data_loader(path="data.csv"):
    x = np.zeros((2, 100))
    y = np.zeros((100))

    with open(path,'r',encoding='utf8') as csvfile:
        r = csv.reader(csvfile, delimiter=',')

        for idx, row in enumerate(r):

            try:
                x[0, idx] = row[0]
                x[1, idx] = row[1]

                if row[2] == "False":
                    y[idx] = 0
                else:
                    y[idx] = 1
            except IndexError:
                continue


    train_set = x[:,:80],y[:80]
    test_set = x[:,80:],y[80:]
    return train_set, test_set

data = data_loader()