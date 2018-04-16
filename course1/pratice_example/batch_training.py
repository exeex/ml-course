from data_loader import data_loader
import model


def batch_training(batch_size=100, batch_num=10):
    m = model.LearningMachine()

    for batch_idx in range(0, (batch_num - 1)*batch_size, batch_size):
        (train_x, train_y) = data_loader(start_line=batch_idx, end_line=(batch_idx + batch_size))
        m.train(train_x, train_y)

    (test_x, test_y) = data_loader(start_line=(batch_num - 1) * batch_size, end_line=batch_num * batch_size)
    test_metrices = m.evaluate(test_x, test_y)
    print("test_auc:", test_metrices['auc'])


if __name__ == '__main__':
    batch_training()
