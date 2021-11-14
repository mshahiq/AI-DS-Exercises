import pandas as pd
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix, accuracy_score
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline

# Load dataset
attributes = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety','target']
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', header=None, index_col=False, names=attributes)

# Preparing the data
df = df.replace(['vhigh', 'high', 'med', 'low', 'small', 'big'], [4, 3, 2, 1, 1, 3])
X, y = df.iloc[:,:-1], df.target
X.persons = X.persons.replace('more',5)
X.doors = X.doors.replace('5more',5)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# PCA

pca = PCA()
classifier = RandomForestClassifier()
pipe = make_pipeline(pca, classifier)
#print(pipe.get_params().keys())
parameters = {'pca__n_components':[1,2,3,4,5,6],'randomforestclassifier__criterion':('gini', 'entropy')}
clf = GridSearchCV(pipe, parameters)
clf.fit(X_train, y_train)
best_parameters = clf.best_params_ # we see best parameters are criterion='entropy', max_depth=None, min_samples_split=2, n_estimators=100, PCA: n_components=6
print(best_parameters)
predictions = clf.predict(X_test)
cv_result_train = cross_val_score(clf, X_train, y_train, cv=5, n_jobs=-1, scoring="accuracy")
acc_score = accuracy_score(y_test, predictions)
print(cv_result_train.mean())
print(acc_score)