from data_loader import data_loader
import random


class LearningMachine():
    def __init__(self, w1=random.gauss(0, 1), w2=random.gauss(0, 1), w3=random.gauss(0, 1)):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

    def train(self, train_x, train_y):
        old_mse = self.loss(train_x, train_y)

        old_w1 = self.w1
        old_w2 = self.w2
        old_w3 = self.w3

        self.w1 = random.gauss(0, 1)
        self.w2 = random.gauss(0, 1)
        self.w3 = random.gauss(0, 1)

        new_mse = self.loss(train_x, train_y)

        if old_mse < new_mse:
            self.w1 = old_w1
            self.w2 = old_w2
            self.w3 = old_w3
            print("mse:", old_mse)
        else:
            print("mse:", new_mse)

    def predict(self, x):
        height = x[0]
        weight = x[1]
        score = height * self.w1 + weight * self.w2 + self.w3

        if score > 0:
            return True
        else:
            return False

    def evaluate(self, test_x, test_y):
        tp = 0
        tn = 0
        fp = 0
        fn = 0

        for idx in range(test_x.shape[1]):
            x_pred = self.predict(test_x[:, idx])

            if x_pred is True:
                if test_y[idx] == 1.:
                    tp += 1
                elif test_y[idx] == 0.:
                    fp += 1
            if x_pred is False:
                if test_y[idx] == 0.:
                    tn += 1
                elif test_y[idx] == 1.:
                    fn += 1

        auc = (tp + tn) / (tp + tn + fp + fn)
        try:
            precision = tp / (tp + fp)
            recall = tp / (tp + fn)
            f1 = 2 * precision * recall / (precision + recall)
        except ZeroDivisionError:
            precision, recall, f1 = 0, 0, 0

        metrices = {'auc': auc, 'prec': precision, 'recall': recall, 'f1': f1}
        return metrices

    def loss(self, test_x, test_y):
        square_sum = 0
        for idx in range(test_x.shape[1]):
            x_pred = self.predict(test_x[:, idx])

            if x_pred is True:
                square_sum += (1. - test_y[idx]) ** 2
            elif x_pred is False:
                square_sum += (0. - test_y[idx]) ** 2

        return 0.5 * square_sum / test_x.shape[1]
