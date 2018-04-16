from data_loader import data_loader
import random
import numpy as np


class LearningMachine():
    def __init__(self):
        self.w1 = random.gauss(0, 1)
        self.w2 = random.gauss(0, 1)
        self.w3 = random.gauss(0, 1)*10-100

    def train(self, train_x, train_y):

        auc_old = self.evaluate(train_x, train_y)

        old_w1 = self.w1
        old_w2 = self.w2
        old_w3 = self.w3

        self.w1 = random.gauss(0, 1)
        self.w2 = random.gauss(0, 1)
        self.w3 = random.gauss(0, 1)*10-100

        auc_new = self.evaluate(train_x, train_y)

        if auc_old > auc_new:
            self.w1 = old_w1
            self.w2 = old_w2
            self.w3 = old_w3
            print("auc:", auc_old)
        else:
            print("auc:", auc_new)

    def predict(self, x):
        height = x[0]
        weight = x[1]
        score = height * self.w1 + weight * self.w2 + self.w3

        if score > 0:
            return True
        else:
            return False
        pass

    def evaluate(self, test_x, test_y):
        correct_counter = 0
        total_case = test_x.shape[0]

        for idx in range(total_case):
            x_pred = self.predict(test_x[idx, :])
            if (x_pred is True) and test_y[idx] == 1.:
                # print("correct")
                correct_counter += 1
            if (x_pred is False) and test_y[idx] == 0.:
                # print("correct")
                correct_counter += 1
            else:
                # print("not correct")
                pass

        auc = correct_counter / total_case
        return auc


(train_x, train_y), (test_x, test_y) = data_loader()

m = LearningMachine()

for x in range(100):
    m.train(train_x, train_y)

test_auc = m.evaluate(test_x, test_y)

print("test_auc:", test_auc)


from plot_perceptron import plot_data, plot_line, plt
plot_data(train_x,train_y)
plot_line(m.w1, m.w2, m.w3)
plt.show()







