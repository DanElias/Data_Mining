'''
Model building in scikit-learn (refresher)
Representing text as numerical data
Reading the SMS data
Vectorizing the SMS data
Building a Naive Bayes model
Comparing Naive Bayes with logistic regression
Calculating the "spamminess" of each token
Creating a DataFrame from individual text files

'''

# Model building in Scikit Learn

'''
The iris dataset is a classic and very easy 
multi-class classification dataset.

This data sets consists of 3 different types of irises’ 
(Setosa, Versicolour, and Virginica) petal and sepal length,
stored in a 150x4 numpy.ndarray
The rows being the samples and the columns being: 
Sepal Length, Sepal Width, Petal Length and Petal Width.
The below plot uses the first two features. 

'''

# load the iris dataset as an example
from sklearn.datasets import load_iris
iris = load_iris()

# store the feature matrix (X) and response vector (y)
'''
Dictionary-like object, the interesting attributes are: 
‘data’, the data to learn, ‘target’, the classification labels
'''

X = iris.data
y = iris.target

# check the shapes of X and y
print (X.shape, y.shape) #(150, 4) (150,)

'''
"Features" are also known as predictors, inputs, or attributes. 
The "response" is also known as the target, label, or output.
'''
'''
"Observations" are also known as samples, instances, 
or records.
'''

# examine the first 5 rows of X (including the feature names)
import pandas as pd
pd.DataFrame(X, columns=iris.feature_names).head()

'''
sepal length (cm)	sepal width (cm)	petal length (cm)	petal width (cm)
0	    5.1	              3.5	             1.4	             0.2
1	    4.9	              3.0	             1.4	             0.2
2
3
4
...
'''

# In order to build a model, the features must be numeric, 
# and every observation must have the same features in the same order.

# import the class
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# instantiate the model (with the default parameters)

#K Nearest Neighbors
knn = KNeighborsClassifier()
#Logistic Regression 
lr = LogisticRegression(max_iter=500)
#Support vector classification
svc = SVC()

'''
You need to split data into train and test sets
First two are the features for the training and testing data
The second two are the labels for the training and testing data

A training dataset is a dataset of examples used for learning, 
that is to fit the parameters (e.g., weights) of, 
for example, a classifier

A test dataset is a dataset that is independent of the 
training dataset, but that follows the same probability 
distribution as the training dataset. If a model fit to 
the training dataset also fits the test dataset well, 
minimal overfitting has taken place. A better fitting 
of the training dataset as opposed to the test dataset 
usually points to overfitting.

'''
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

print (X_train.shape) #(112,4)   112 + 38 dan los 150 
print (X_test.shape)  #(38,4)

# fit the model with data (occurs in-place)
knn.fit(X_train, y_train)
lr.fit(X_train, y_train)
svc.fit(X_train, y_train)

# calculate accuracy of class predictions
from sklearn import metrics
print ("training accuracy: {}".format(metrics.accuracy_score(y_train, knn.predict(X_train))))
print ("test accuracy: {}".format(metrics.accuracy_score(y_test, knn.predict(X_test))))

print ("training accuracy: {}".format(metrics.accuracy_score(y_train, lr.predict(X_train))))
print ("test accuracy: {}".format(metrics.accuracy_score(y_test, lr.predict(X_test))))

print ("training accuracy: {}".format(metrics.accuracy_score(y_train, svc.predict(X_train))))
print ("test accuracy: {}".format(metrics.accuracy_score(y_test, svc.predict(X_test))))

# In order to make a prediction, the new observation must 
# have the same features as the training observations, 
# both in number and meaning.

# predict the response for a new observation
print(knn.predict([[3, 5, 4, 2]]))


