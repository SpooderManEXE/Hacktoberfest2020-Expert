import numpy as np
import pandas as pd
import tensorflow as tf

#tf.__version__

dataset = pd.read_csv('Churn_Modelling.csv')
x = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values

# Encoding categorical data
# Label Encoding the "Gender" column
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
x[:, 2] = le.fit_transform(x[:, 2])

# One Hot Encoding the "Geography" column
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
print(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

ann = tf.keras.models.Sequential() #creates our sequential ann

#input layer will have all the features of x

# Adding the input layer and the first hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Adding the second hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Adding the output layer
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Compiling the ANN

#optimizer = change the weights by checking the value of loss function during training, many types
#loss = for checking how wrong the predictions are, acting as a guide to the optimizer, many types 👇
#binary_crossentropy -> for binary results
#categorical_crossentropy -> for non-binary results #the the activation of output should be 'softmax'
#metrics = for checking the precision, accuracy, many types

ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# Training the ANN on the Training set
#batch_size for working in and compairing all the batches, 
#epochs -> indicates the number of passes of the entire training dataset, 
#if the batch size is the whole training dataset then the number of epochs is the number of iterations
ann.fit(x_train, y_train, batch_size = 32, epochs = 100)

#0.5 = threshold
print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])) > 0.5)

y_pred = ann.predict(x_test)
y_pred = (y_pred > 0.5)
print(y_pred)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)