## what machine learning actually is and how it is different from traditional programming?
- Traditional programming means that we write all the instructions ourselves. The computer only follows those instructions.

       -  Input + Rules → Output

- Machine learning is different because, instead of giving every rule manually, we give the computer a lot of data. The computer learns patterns from that data and uses them to make predictions.

       -  Input + Output → Rules
       
- For example, in traditional programming, we would have to write rules to identify spam emails. In machine learning, we train a model using thousands of spam and non spam emails, and the model learns how to classify new emails on its own.

## few basic terms:
### Dataset: 
A collection of data we use to train & test Machine learning model . for example we have iamges of plastic,glass,paper waste in a folder
### Features:
An input information model use to learn pattrens.for example in house price preditcion we have fetures like 
size of house,number of rooms,location of house
### lebles:
jo corect answers hoty hain data k sath associate/attach hoy hoy,
like aik image main agr plastic bottel h to us ka label ho ga plastic 
### Training data: 
the part of dataset jis par model ko teach kia jata h ,model isi part of dataset par pattrens learn krta h 
### Testing data:
the part of dataset we use to chk how well the model is performing on unseen data
### model:
the trained machine learning program that learn the pattrens, store the pattrens and use them to make predictions on a new data
### predictions:
the output produced by model for the new data based on the pattrens it learned 
## the complete workflow
- Collect Data:collect teh raw data to train the model
- Clean Data : remove erors or in appropriate data from the dataset so that it can be used effectively.
- Train model: Train the model on that data
- Test model: Evaluete model's preformance on an unseen data ,it will be labeld data we wil keep it seprate from training data before training model,we will use it after training to chk how well model is performaing on an unseen data
- make predictions : use the trained model to predict new images ,it will not be labled , it will be completly fresh

### in case we have train,test, validation folders
- Train:The model learns patterns from this data.
- Test: we use it to chk performace of model after training. 
- Val: we use it to chk performace of model during taring for ex : it will chk how well model learned after an epoch.

## The three main types of machine learning:
- ### Supervised learning:
In supervised learning, the model is trained using labeled data, meaning the correct answers are already available. The model learns the relationship between the input and output and then predicts outputs for new data. For example, predicting whether waste is plastic, paper, or glass.
   -  What problem it solves:
        - output predict krta hai,labeled data sy
   -  Real life examples
        - Email spam detection, house price prediction, waste classification.
   - Common algorithms
       - will see them later

- ### UnSupervised learning:
In unsupervised learning, the model is trained using unlabeled data, meaning the correct answers are not provided. The model tries to find hidden patterns or groups in the data by itself. For example, grouping customers with similar shopping behavior.
   - What problem it solves:
       - hidden groups ya hidden pattrens ko learn krta h unlabeled data sy
   - Real life examples
      - A news website automatically groups similar articles into categories.
      - A photo gallery groups similar faces or images without being told who the people are.
   - Common algorithms
       - will see them later
- ### Reinforcement learning:
In reinforcement learning, the model learns by interacting with an environment and receiving rewards or penalties for its actions. Its goal is to maximize the reward over time. For example, training a robot or a game playing AI.
    
 -  What problem it solves:
    - lerans best action by getting reward or panelties based on its actions
 -  Real life examples
    - Self driving cars, robots, game playing AI.
 - Common algorithms
    - will see them later



## how models actually learn from data.
Summary: A model learn from the data by adjusting/chainging the weights to reduce prediction error
- we give data to the model
- model makes a guess
- model compare its predictions with actual answers
- model calculate the error
      - model measure how far its prediction is from the actual answers thats call error.
- change its weights to reduce the error (Adjust itslef)
      - The internal numerical settings/numbers model change to reduce the error is called weight
- repeat itself thousands of time 
     - model will keep reapeting the process till it will not make correct predictions

## What Is CNN(Convolutional Neural Network) And Its Types??
- Yeh aik Deep learning model h jo k images ko process krny k liy Design kia gia h 
- A CNN learn the pattrens by passing an image through its few main layers
LAYERS:(CAPFc)
  1. Convolutional LAyer
  - This layers looks for the simple pattren in an image like edges,corners,colors, lines
  2. Activation Layer
  - This layer decide wihc info is important & should be pass to the nxt layer
  3. Pooling Layes
  - this layer reduce the data size and keep only the important info
  4. Fully Connected Layer
  - this layer use that important info and make final predictions
A CNN usually has many convolution and pooling layers stacked together. The early layers learn simple features like edges, while deeper layers learn complex features like the shape of a bottle or a piece of paper.

My waste classification model uses a CNN inside YOLO to understand images.

# few terms i need to know 
### forward Pass
forward pass is the process in which an input/uploaded image passes through all the layers of CNN to make final predictions
### Backpropogation
Backpropagation is the process that tells the model which weights caused the error and how much they should change.
### optimizer/optimization algorithms
The optimizer updates those weights to reduce the error and improve the model's predictions.
### input features
the input features are the info model extract from an image like corners,edges, colors, shapes,texture,lines
### batch of images
A small goup of images that a model process at once during the training
For example, in our project, we used:
batch=4
This means YOLO took 4 images together, made predictions, calculated the error, and updated the weights before moving to the next 4 images.
## Classification versus regression
- classification predict descrete,catagorical labels for ex: spam or not spam ,plastic,glass etc (it predict categories)
- regression predict continuos,numerical values for ex: temprature,house price
## Overfitting vs Underfitting
- Overfitting happens when model memorize Training data too much but perform too poor on unseen/new data
- Underfitting happens when model do not learn enough pattrens from the training data 
 perform poorly on both training and unseen data 
## Epochs :
1 Epoch means the model has seen entire data set once
## Accuracy :
Accuracy tells us what percentage of predictions were correct
## Loss :
loss is a measure of how wrong the model's prediction is compared to the actual answer.

# entire machine learning pipeline from dataset to prediction
a pipeline is simply a step by step process that takes something from the beginning to the final result.
- ## define project objectives 
    - specify Business Problems
    - Company requiremnts
- ## DAta collection 
we can have two types of data
### Primary data
The data you colect yourself for a specific purpose (collected by user)
### secondary data
the data collected by someone else and reused by you (aisa data statistical process ya modifications sy pass ho kar user ko dia jata h)
- ## DAta preprocessing
 - jo data hum ny data collection phase main collect kia hota h wo raw data hota h yani us main inconsistency hoti hai, aor wo proper format main nai hota kuch values missing ho skti hain etc etc is liy hum data collect krny k baad data preprocessing krty hain
 - we can use python libraries like numpy,pandas,and scikit learn libraries for data preprocessing 
 we have three following steps in data preprocessing 
     1. data cleaning
       - filling missing data
       - Smoothing noisy data : noisy data means an unusall values or irrelevent data like temprature of a person recorded as 500 degree C
     2. data Transformation
     Converting the data into a better format for the model
   ### Data Normalization 
   - Data Normailzation is a preprocessing technique we use to resize feature values to a specific scale usally between 0 and 1 
   - It is a feature scaling technique used to transform data into a standard range
   For Example we have 2 columns age and salary in our dataset
   • Age: 20, 25, 30
   • Salary: 50,000, 80,000, 120,000
   - the problem is that salary numerics are more higher than age numerics so the ML model may pay more attention to the salary and ignore age
   - Normalization shorink the values so that they both can come on the similar scale
   - Actual meaning of the data will remain same ,we only change the scale so that both the values can influence the model's performance equally
    3. dimensionality reduction (reducing dimension)
    - for example 3d data ko 2d data main convert krna 
    - Sometimes datasets have too many columns, and many of them are not useful.
    - For example, if a dataset has 100 features/columns, we might keep only the 20 most important ones. This makes training faster and can improve performance.
#### Note so we can call it data analysis after all these 3 steps
- ## data visulaization
   - now we need data visulaization is the graphical representaion of data
   we do viuslization to show relationship between the data or different columns like a column can be X and the other one can be Y
   - we transform data into tables ,pie chart,graph,histogram,bar chart etc 
   - we can use libraries like matplotlib and seaborn for data visulization
   - hum data ko compare krty hain or data k beech main relationship ko find krty hain like X and Y variables k beech mmain

- ## model slection
  - Now wee need to know which algorithm we need to use for the particular data
  - like we have following alogrithms
     1. Linear regression :Use it when you want to predict a continuous number, like house prices or salaries.
     2. Logistic regression : Use it when you want to classify data into categories, like spam or not spam. (its a clssification algo)
     3. random forest : Use it when you need a powerful algorithm for classification or prediction on complex data.
     4. K-means clustering : se it when you want to automatically group similar data without labels.

- ## model building
after selcting algo we use that algo and split our data in to test and train to train the model and then test it and then make predictions and we will keep reapeating the process till the model learn better pattrens 
- ## model deployment
integrate ML model into existing production environment 
means we deploy the model into production env