from sklearn.svm import SVC
from mlxtend.plotting import plot_decision_regions
from sklearn import metrics
from data_loader import data_loader
import matplotlib.pyplot as plt


(train_x, train_y), (test_x, test_y) = data_loader()

svm = SVC()
svm.fit(train_x, train_y)

y_pred = svm.predict(test_x)

auc = metrics.accuracy_score(test_y, y_pred)
f1 = metrics.f1_score(test_y, y_pred)

print(auc, f1)

plot_decision_regions(test_x, test_y.astype("int"), clf=svm)
plt.show()