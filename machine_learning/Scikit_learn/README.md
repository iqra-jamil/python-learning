# What Scikit learn is.
scikit-leran is a python library , which provide datasets, ML models,tool to evaluate performance.
# why i need to learn sckit leran ?
Because most ML work start with this library 
1. it provide us alot of ready made algorithms like linear regression, decision trees, SVM, and k nearest neighbors.
2. we do not need to write algorithms from scratch,we can use them just by importing them 
- then we train the algorithm on our data
- ### so the job is :
     - choose the right algrithm according to objective 
     - give it data
     - train it on  our data
     - test its performance
     - 
- Technically:
  • Decision tree, SVM, and K nearest neighbors are algorithms.
  • we train them on our data and then they become models
- like YOLO was an alogorithm then we trained it on ou data in FYP and it became tarined model
3. scikit learn helps us to split the data into training and testing sets
4. scikit learn provide us tools to measure the performance of a model like F1 score, precison,recall,accuracy,confusion matrix
5. It helps us preprocess data by scaling, encoding, and handling features
    - Scaling - is the part of data transformation
        - Data scaling is a technique that brings numerical features to a similar range so that no feature dominates the others. (normalization is the type of it)
    - Encoding - converting Text into numbers
    - handling features- selcting ,creating ,reducing features
so they are the samller techinuqes come under those main preprocessing techinique we already studied data cleaning, data transformation ,dimensionality reduction 

### Note - scikit learn is important even if we use pytorch and tensorflow later , pytorch and tensorflow used for deep learning and scikit leran is used for many traditional ML tasks

# deep leraning vs traditional ML
- traditional ML works on structured data like Home prediction , deep learning works on image,text ,voice data
- Traditional machine learning uses models like Decision Trees and SVM, deep learning use Neural networks like CNN and YOLO
- traditional ML needs manual feature engineering (learns pattrens manually) while deep learning learns pattrens automatically 


# what is dataset : 
a collection of a an example data model learns from
# what is features :
features are input information that model use to  learn pattrens like in waste images corner,edges,objects,shapes etc 
# what is labels :
lebels are the outputs or categories that the model must predict, such as plastic, paper, or glass.
# Tarining and Testing :
 - Training dataset is the set from which model learn
 - Testing dataset is the part of dataset on which we chek model's performance whether the model learns properly or not
# The machine learning pipeline :
 - already studied in detail
 - dataset -> split -> Training -> make predictions(testing)->chk accuracy(evaluation)
# Prediction :
model's answer for the new data
# Accuracy :
the percentage of Predictions that model got correct 
# model 
A program that learn pattrens from the given data and make predictions on new/unseen data
# overfitting and underfitting
- Overfitting - when model learns too much and make correct predictions only on seen data
- Underfitting - when model dont leran on both seen and unseen data and make wrong predictions on both seen and unseen data 

### A classifier is a type of model that predicts categories, like spam or not spam


# what is transformer
A transformer in scikit learn is an object that convert data from one form to anotehr before giving it to ML model
it has two steps 
- fit() - learn info from our dataset info liek mean ,S.D, min-value,max-value
- transform() - use that learned value to chnage data into another form
# scalling vs normalization and standardization
- Scaling is the general process of changing the range of data values.(umbrella term)

- Normalization is the process of scaling data to a specific range, usually between 0 and 1.
   
- Standardization is also a type of scalling so that Mean of new dataset is 0 and S.d is 1
 
# standardization and normalization techniques (feature scaling techniques)
-  ## StandardScaler() 
-  standardizes data using mean and standard deviation, making mean = 0 and std = 1.
- that does not convert values into 0 and 1 only. The values can be negative too and greater than 1 too.

- Formula:

(original value − mean) / S.D

- Yeh pehle original data ka mean aur S.D find karta hai, phir un ko formula mein put karta hai.
- mean = 0 and S.D = 1 ka matlab new dataset ka mean aur S.D hai.
- Definition:
transform the data into a new dataset in such a way that the new dataset has mean = 0 and S.D = 1.
-  ## MinMaxScaler() 
- scales data into a fixed range, usually 0 to 1, using minimum and maximum values.
- yeh features yani columns par apply hota h min,max values jo formula main use hoti hain wo b column sy he extarct hoti hain
- use when you want every feature to lie in a fixed range, usually between 0 and 1.
- Formula:
    (new value) = (value − minimum) / (maximum − minimum)
- Ye har column ko independently 0 aur 1 ke darmiyan scale karta hai.
- har aik value jo aik column main hoti h us par jab MinMaxScaler() apply hota h us ka anser 0 and 1 k darmian aata h
- ## Normalizer() 
- scales each row independently based on its vector length/magnitude (norm). (It is a transformer.)
- use when the direction of each row matters more than its actual size, such as in text data.
- Formula:
  (new value) = value / vector length
- Yeh pehle har row ka magnitude find karta hai.
- Ye har row ki har value ko us complete row ke magnitude se divide karta hai taake poori row ki length 1 ho jaye.(us ko formula main dalty hain)
- is main magnitude new jo row banti h formula apply krny k baad us ka magnitude 1 bana hota h 
- ## normalize() 
- same normalization as Normalizer(), but used directly as a function instead of a transformer.
# split the dataset into test/train
1. import train_test_split from model_selction (scikit-learn)
2. its paramters
    1. *arrays : yahan wo data aata h jo split krna h like X,y X= features,y= lables
    - X main lables waly column ko drop krna h 
    - y main data main sy specific (species) labels wala column acess krna h
    2. test_size & train_size : kitna data testing ya training k liy use krna h
       - float or int, default=None (ex: 0.2 & 0.8)
       - should be between 0.0 and 1.0 
       - mostly 20% testing ke liye aur 80% training ke liye use kia jata h
    3. random_state:
       - Seed for randomness.
       - Set a number (e.g. 42) → same split every run (reproducible).
       - None → different split each run.
       - matters for reproducibility, so you (and others) get the same results every time.
    4. shuffle: Data ko split se pehle mix karna hai ya nahi True or False
       - matters to avoid biased splits when data is ordered (e.g., sorted by class or date); keep False only for time-series.
    5. stratify : 
       - Keeps class proportions same in train & test sets.
       - stratify=y → if y is 90/10 split, both train/test keep ~90/10.
       - Important for imbalanced classification data.
       - matters to keep class ratios balanced in train/test, critical for imbalanced datasets.
# create classifier
- use DecisionTreeClassifier() from tree(scikit-learn) to create  a clssifier
# train classifier model
use clf.fit(X_train,Y_train) to tarin the model
# make predictions
- use clf.predict(X-test) to predict the classes (use X_test=features)
- q k model features ko daikh kar prediction karta h so, is ko prediction k waqt srf features diy jaty hain labels nai
# check accuracy
- use y_true(label yani y_test) & y_pred (model's predicted results) labels to chek accuarcy of model
- use accuracy_score()
- normalize=False predictions ka number deta h instaed of percent age
-  Accuracy chk karny k liy model k predicted labels and Actual labels ko compare krna hota h k jo model ny labels predict kiy hain wo sai hain ya nai 
- to chk accuracy we need to find test & train accuracy too bcz agr train accuracy bhot ziada ho and test accuracy bhot kam to model overfitting karha hota h (we can chk underfitting too)
## train and test accuracy
- we will use model.score() to chk train & test accuracy
- Model X_test ke features dekh kar labels predict karta hai, phir un predicted labels ko actual labels, yani y_test, se compare kiya jata hai.
- so .score take X_test and y_test both as an argument same for tarin 
## StandardScaler ,fit,transform()
- StandardScler() is a tool /object that provide formula to scale the columns in to a new clumns in a way that new columns (each col) get mean 0 and S.D 1
- fit() - calculate the S.D and mean of orignal /old columns and store them inside a scaler
- transform - apply that formula Standardscaler provided and use S.D and mean stored by fit() to actualy rescale the data  
# confusion_matrix
use sklearn.metrics.confusion_matrix with following parameters

- y_true :Actual labels from the dataset
- y_pred : predicted labels of the model
- * : is k baad jitny parameters hain un ko naam dy kar likhna zruri h 
- labels=None : which classes to include, and in what order.
- sample_weight=None : matlab hai ke by default har sample/row ki importance 1 hoti hai, lekin hum chahein to kuch samples ko zyada weight de sakte hain.
- normalize=None :Normalizes confusion matrix over the true (rows), predicted (columns) conditions or all the population. If None, confusion matrix will not be normalized.
### Normalization" here just means: instead of showing raw counts, divide those counts by some total, so you get fractions instead.
# The basic workflow
- Download dataset (done)
- Load the dataset into  project. (done)
- Apply preprocessing techniques (done)
- split the dataset into test/train (done)
- create classifier (creating the model)
- train classifier model
- make predictions
- check accuracy

