import pandas as pd
from sklearn import preprocessing,tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay,f1_score
import matplotlib.pyplot as plt
# ---------------------loading dataset------------------
my_data=pd.read_csv(r"C:\Users\decent\OneDrive\Desktop\python-learning\machine_learning\Scikit_learn\Iris.csv") 

print(my_data.to_string())
# preprocessing 
## ------------------------- data cleaning --------------
print(my_data.isnull().sum()) # counting missing values per column
print(my_data.duplicated().to_string()) # checking duplicates
drop_column=my_data.drop(columns=["Id"]) # removing useless column #dimensionality reduction 
print(drop_column)
my_new=drop_column.iloc[:,:-1] # take all the columns and all the rows except last column 
print(my_new)
print(my_new.columns)
# --------------- standardization-------------
scaler=preprocessing.StandardScaler().fit(my_new)
my_scaler=scaler.transform(my_new)
print(my_scaler)
# normalization
norm_scaler=preprocessing.MinMaxScaler().fit(my_new)
mynorm_scaler=norm_scaler.transform(my_new)
print(mynorm_scaler)
# ------------ other two normalization techniuqes --------
#norm_scaler=preprocessing.normalize(my_new)
# print(norm_scaler)
# norm_scaler=preprocessing.Normalizer().fit(my_new)
# mynorm_scaler=norm_scaler.transform(my_new)
# print(mynorm_scaler)

#------------- split the dataset into test/train--------
X=drop_column.drop(columns=["Species"])
y=my_data["Species"]

X_train,X_test,y_train,y_test=train_test_split(X,y , train_size=0.8,test_size=0.2 ,shuffle=True,random_state=42,stratify=y)
print("My X train",X_train.to_string())
print("My y train",y_train.to_string())
print("My X test",X_test.to_string())
print("My y test",y_test.to_string())
# ------------------------create classifier-------------------------
classifier= tree.DecisionTreeClassifier()
# ------------------------train classifier-------------------------
classifier.fit(X_train,y_train)
#--------------------------make predictions----------------------
my_prediction=classifier.predict(X_test)
print(my_prediction)
#--------------------------check Accuracy----------------------
my_accuracy=accuracy_score(y_test,my_prediction)

print("my Accuracy............",my_accuracy)
#multiply accuracy with 100 to get percentage 

#--------------------------check tarin & test Accuracy----------------------
test_accuracy=classifier.score(X_test ,y_test)
train_accuracy = classifier.score(X_train,y_train)
print("test accuracy",test_accuracy)
print("train accuracy",train_accuracy)
# ---------------------------- Confusion matrix-------------------------------
cm=confusion_matrix(y_test,my_prediction)                          
print(cm)
disp=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=classifier.classes_)
disp.plot()
plt.show()
f1=f1_score(y_test,my_prediction,average="weighted")
print(f1)