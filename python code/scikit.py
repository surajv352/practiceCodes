# from sklearn import datasets
# iris = datasets.load_iris()
# digits = datasets.load_digits()
# print(digits.target)
# print(digits.images[0])
# print(iris.data,iris.target)
from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
res = clf.fit(X, y)
print(res)