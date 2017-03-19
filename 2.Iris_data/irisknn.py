import pandas as pd 
import random
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors

df = pd.read_csv('irisdata.csv', names = ['sl','sw','pl','pw','cl'])
#print df.head()
#Since we have same species of data together therefore we need to shuffle the data. I the next line of code I am doing that.
df = df.sample(frac=1).reset_index(drop=True)
#print df.head()
#Now I am changing the dataset into numerical form.

df.loc[(df["cl"] == "Iris-setosa"),'cl']=0
df.loc[(df["cl"] == "Iris-versicolor"),'cl']=1
df.loc[(df["cl"] == "Iris-virginica"),'cl']=2
y = np.array(df['cl'], dtype = np.int64)
X = np.array(df.drop(['cl'], 1))

X_train,X_test,y_train,y_test = cross_validation.train_test_split(X, y, test_size=0.25)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print accuracy

#For prediction it is good to pass the array insteead of directly passing the list.
predict = np.array([4.4,2.9,1.4,0.2])
# To avoid warning issues we need to reshape this list.
predict = predict.reshape(1,-1)
prediction = clf.predict(predict)

# Predict on a given dataset to predict the values.
print "Prediction result on one sample of given dataset",prediction


# Plot of how our accuracy is varying with number of neighbors.
accu = []
for k in range(1,40):
	clf = neighbors.KNeighborsClassifier(n_neighbors=k)
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	accu.append(accuracy)
k_range = range(1,40)
import matplotlib.pyplot as plt 
fig = plt.figure()
plt.plot(k_range,accu)
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.show()
