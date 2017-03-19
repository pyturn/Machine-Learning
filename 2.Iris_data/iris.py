import pandas as pd 
import random
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('irisdata.csv', names = ['sl','sw','pl','pw','cl'])
#print df.head()
df = df.sample(frac=1).reset_index(drop=True)
#print df.head()
df.loc[(df["cl"] == "Iris-setosa"),'cl']=0
df.loc[(df["cl"] == "Iris-versicolor"),'cl']=1
df.loc[(df["cl"] == "Iris-virginica"),'cl']=2
y = np.array(df['cl'], dtype = np.int64)
X = np.array(df.drop(['cl'], 1))
X_train,X_test,y_train,y_test = cross_validation.train_test_split(X, y, test_size=0.25)

log=LogisticRegression(penalty='l2',C=1)
log.fit(X_train,y_train)
accuracy = log.score(X_test,y_test)
print accuracy
