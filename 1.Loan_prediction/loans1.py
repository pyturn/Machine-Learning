import pandas as pd
import numpy as np
import sys
from scipy.stats import mode
from sklearn import preprocessing,cross_validation
from sklearn.linear_model import LogisticRegression
print sys.version
data = pd.read_csv('train_u6lujuX_CVtuZ9i.csv')
test = pd.read_csv('test_Y3wMUE5_7gLdaTN.csv')
#print data["Loan_Status"]



data.loc[(data["Gender"] == "Male"),'Gender']=1
data.loc[(data["Gender"] == "Female"),'Gender']=0
test.loc[(test["Gender"] == "Male"),'Gender']=1
test.loc[(test["Gender"] == "Female"),'Gender']=0


data.loc[(data["Married"] == "Yes"),'Married']=1
data.loc[(data["Married"] == "No"),'Married']=0
test.loc[(test["Married"] == "Yes"),'Married']=1
test.loc[(test["Married"] == "No"),'Married']=0

data.loc[(data["Education"] == "Graduate"),'Education']=1
data.loc[(data["Education"] == "Not Graduate"),'Education']=0
test.loc[(test["Education"] == "Graduate"),'Education']=1
test.loc[(test["Education"] == "Not Graduate"),'Education']=0

data.loc[(data["Self_Employed"] == "No"),'Self_Employed']=1
data.loc[(data["Self_Employed"] == "Yes"),'Self_Employed']=0
test.loc[(test["Self_Employed"] == "No"),'Self_Employed']=1
test.loc[(test["Self_Employed"] == "Yes"),'Self_Employed']=0


data.loc[(data["Property_Area"] == "Rural"),'Property_Area']=1
data.loc[(data["Property_Area"] == "Semiurban"),'Property_Area']=2
data.loc[(data["Property_Area"] == "Urban"),'Property_Area']=3
test.loc[(test["Property_Area"] == "Rural"),'Property_Area']=1
test.loc[(test["Property_Area"] == "Semiurban"),'Property_Area']=2
test.loc[(test["Property_Area"] == "Urban"),'Property_Area']=3

data.loc[(data["Loan_Status"] == "Y"),'Loan_Status']=1
data.loc[(data["Loan_Status"] == "N"),'Loan_Status']=0


data.loc[data['Dependents']=="3+",'Dependents']=5
test.loc[test['Dependents']=="3+",'Dependents']=5

#print data

print "Loan Status with respect to Gender and Self_Employed"
impute0_grps = data.pivot_table(values=["Loan_Status"],index = ["Gender","Self_Employed"], aggfunc = np.sum ,margins = True)
print impute0_grps

print "Loan Status with respect to Self_Employed"
impute1_grps = data.pivot_table(values=["Loan_Status"],index = ["Self_Employed"], aggfunc = np.sum ,margins = True)
print impute1_grps

print "Loan Status with respect to Education"
impute2_grps = data.pivot_table(values=["Loan_Status"],index = ["Education"], aggfunc = np.sum ,margins = True)
print impute2_grps

print "Loan Status with respect to Applicant Income"
impute3_grps = data.pivot_table(values=["ApplicantIncome"],index = ["Loan_Status"], aggfunc = np.mean )
print impute3_grps

print "Loan Status with respect to CoApplicant Income"
impute4_grps = data.pivot_table(values=["CoapplicantIncome"],index = ["Loan_Status"], aggfunc = np.mean )
print impute4_grps

print "Loan Status with respect to Property_Area"
impute4_grps = data.pivot_table(values=["Loan_Status"],index = ["Property_Area"], aggfunc = np.sum )
print impute4_grps




print "                Now our program is finding the missing values                   "

def num_missing(x):
	return sum(x.isnull())

#print data.apply(num_missing, axis=0)
#print test.apply(num_missing, axis=0)


data['Gender'].fillna(mode(data['Gender']).mode[0],inplace = True)
data['Married'].fillna(mode(data['Married']).mode[0],inplace = True)
data['Dependents'].fillna(mode(data['Dependents']).mode[0],inplace = True)
data['Education'].fillna(mode(data['Education']).mode[0],inplace = True)
data['LoanAmount'].fillna(mode(data['LoanAmount']).mode[0],inplace = True)
data['Loan_Amount_Term'].fillna(mode(data['Loan_Amount_Term']).mode[0],inplace = True)
data['Credit_History'].fillna(mode(data['Credit_History']).mode[0],inplace = True)
data['Self_Employed'].fillna(mode(data['Self_Employed']).mode[0],inplace = True)

test['Gender'].fillna(mode(test['Gender']).mode[0],inplace = True)
test['Married'].fillna(mode(test['Married']).mode[0],inplace = True)
test['Dependents'].fillna(mode(test['Dependents']).mode[0],inplace = True)
test['Education'].fillna(mode(test['Education']).mode[0],inplace = True)
test['LoanAmount'].fillna(mode(test['LoanAmount']).mode[0],inplace = True)
test['Loan_Amount_Term'].fillna(mode(test['Loan_Amount_Term']).mode[0],inplace = True)
test['Credit_History'].fillna(mode(test['Credit_History']).mode[0],inplace = True)
test['Self_Employed'].fillna(mode(test['Self_Employed']).mode[0],inplace = True)

print data.apply(num_missing, axis=0)
print test.apply(num_missing, axis =0)
#print data
'''print "Loan Status with respect to Gender Married and Self_Employed"
impute4_grps = data.pivot_table(values=["LoanAmount"],index = ["Gender","Married","Self_Employed"], aggfunc = np.mean)'''

y1 = data['Loan_Status']
data = data.drop('Loan_Status',1)
data = data.drop('Loan_ID',1)

X = np.array(data, dtype = np.float64)
y = np.array(y1, dtype = np.float64)

test_ID = test['Loan_ID']
test = test.drop('Loan_ID',1)
test_predict = np.array(test, dtype = np.float64)
X = preprocessing.scale(X)
print X

test_predict = preprocessing.scale(test_predict)
print test_predict

print len(X)
print len(test_predict)


X_train,X_test,y_train,y_test = cross_validation.train_test_split(X, y, test_size=0.2)
log=LogisticRegression(penalty='l2',C=1)
log.fit(X_train,y_train)
accuracy = log.score(X_test,y_test)
print accuracy
y2 = log.predict(test_predict)
print y2

test_ID=pd.DataFrame(test_ID,columns=['Loan_ID'])
y2=pd.DataFrame(y2,columns=['Loan_Status'])
y2.loc[y2['Loan_Status']==1,'Loan_Status']='Y'
y2.loc[y2['Loan_Status']==0,'Loan_Status']='N'

output= pd.DataFrame( data={"Loan_ID": test_ID["Loan_ID"], "Loan_Status":y2.Loan_Status} )
output.to_csv("Sample_Submission_ZAuTl8O_FK3zQHh (1).csv", index=False,quoting=3)