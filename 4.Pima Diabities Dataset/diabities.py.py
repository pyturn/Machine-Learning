import pandas as pd 
import numpy as np 
url='https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data';
'''
 Number of times pregnant (preg)
Plasma glucose concentration a 2 hours in an oral glucose tolerance test (plas)
Diastolic blood pressure in mm Hg (pres)
Triceps skin fold thickness in mm (skin)
2-Hour serum insulin in mu U/ml (insu)
Body mass index measured as weight in kg/(height in m)^2 (mass)
Diabetes pedigree function (pedi)
Age in years (age)'''
col_names = ['no_preg','plasma_glucose_concn','bp','skin_fold_thick','serum_insulin','bmi','pedigree_func','age_years','class_var']
pima=pd.read_csv(url, header=None, names=col_names)
print pima.head(50)
print pima.describe()

#Diabetes Pedigree Function, pedi. It provides some data on diabetes mellitus history in relatives and the genetic relationship of those
#relatives to the patient. This measure of genetic influence gave us an idea of the hereditary risk one might have with the onset
#of diabetes mellitus.
import matplotlib.pyplot as plt 
fig = plt.figure()
plt.scatter(pima["age_years"],pima["class_var"],label="class_var",color = 'k')
plt.xlabel('Age')
plt.ylabel('Positive or Negative')
plt.show()
#"From this we infer that age is not affecting whether the patient is diabetic or not"
plt.scatter(pima["no_preg"],pima["class_var"],label="class_var",color = 'k')
plt.xlabel('No. of times pregnant')
plt.ylabel('Positive or Negative 0-Positive and 1_Negative')
plt.show()
#"From this we infer that No of times woman is pregnant is not affecting whether the patient is diabetic or not"
plt.scatter(pima["plasma_glucose_concn"],pima["class_var"],label="class_var",color = 'k')
plt.xlabel("Plasma Glucose Conc'n")
plt.ylabel('Positive or Negative 0-Positive and 1_Negative')
plt.show()
#"From this we infer that Plasma_Glucose_Conc'n is affecting whether the patient is diabetic or not"
plt.scatter(pima["bp"],pima["class_var"],label="class_var",color = 'k')
plt.xlabel("BP")
plt.ylabel('Positive or Negative 0-Positive and 1_Negative')
plt.show()
#"From this we infer that bp is affecting whether the patient is diabetic or not"
plt.scatter(pima["skin_fold_thick"],pima["class_var"],label="class_var",color = 'k')
plt.xlabel("Skin_Fold_Thickness")
plt.ylabel('Positive or Negative 0-Positive and 1_Negative')
plt.show()
#"From this we infer that skin_fold_thickness is affecting whether the patient is diabetic or not"
plt.scatter(pima["serum_insulin"],pima["class_var"],label="class_var",color = 'k')
plt.xlabel("Serum_Insulin")
plt.ylabel('Positive or Negative 0-Positive and 1_Negative')
plt.show()
#"From this we infer that Serum_Insulin is affecting whether the patient is diabetic or not"
plt.scatter(pima["bmi"],pima["class_var"],label="class_var",color = 'k')
plt.xlabel("BMI")
plt.ylabel('Positive or Negative 0-Positive and 1_Negative')
plt.show()
#"From this we infer that BMI is affecting whether the patient is diabetic or not"
plt.scatter(pima["pedigree_func"],pima["class_var"],label="class_var",color = 'k')
plt.xlabel("Pedigree_Function")
plt.ylabel('Positive or Negative 0-Positive and 1_Negative')
plt.show()
#"From this we infer that Pedigree is affecting whether the patient is diabetic or not"


from sklearn.cross_validation import train_test_split

temp = ['plasma_glucose_concn','bp','skin_fold_thick','serum_insulin','bmi','pedigree_func']
temp1 = ['no_preg','plasma_glucose_concn','bp','skin_fold_thick','serum_insulin','bmi','pedigree_func','age_years']
x=pima[temp]
y=pima.class_var

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
from sklearn.linear_model import LogisticRegression
clf=LogisticRegression()
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
acurracy = clf.score(x_test,y_test)
print acurracy

x=pima[temp1]
y=pima.class_var

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
from sklearn.linear_model import LogisticRegression
clf=LogisticRegression()
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
acurracy = clf.score(x_test,y_test)
print acurracy