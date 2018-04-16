import csv
import numpy as np


def data_loader(path="data.csv"):
    """
    How to use:
    from data_loader import data_loader

    (train_x, train_y), (test_x, test_y) = data_loader()

    :param path: csv file path, ex. "data.csv"
    :return: (train_x, train_y), (test_x, test_y)
    """

    x = np.zeros((1000,2))
    y = np.zeros(1000)

    with open(path, 'r', encoding='utf8') as csvfile:
        r = csv.reader(csvfile, delimiter=',')

        for idx, row in enumerate(r):

            try:
                x[idx, 0] = row[0]
                x[idx, 1] = row[1]

                if row[2] == "False":
                    y[idx] = 0
                else:
                    y[idx] = 1
            except IndexError:
                continue


    train_set = x[:800,:], y[:800]
    test_set = x[800:,:], y[800:]
    return train_set, test_set


# (train_x, train_y), (test_x, test_y) = data_loader()
