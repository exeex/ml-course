import matplotlib.pyplot as plt
import numpy as np


def plot_data(train_x, train_y):

    data = np.column_stack((train_x[:, 0], train_x[:, 1], train_y))

    print(data)

    for row in data:
        height = row[0]
        weight = row[1]
        is_fat = row[2]
        # print(is_fat)
        if is_fat == 1.0:
            plt.scatter(height, weight, c="red")
        else:
            plt.scatter(height, weight, c="blue")

def plot_line(w1,w2,w3):
    w = np.linspace(40, 80)
    h = -w2 / w1 * w - w3 / w1
    plt.plot(h, w)

if __name__ =="__main__":

    from data_loader import data_loader
    (train_x, train_y), (test_x, test_y) = data_loader()
    plot_data(train_x,train_y)
    plt.show()