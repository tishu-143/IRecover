import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def predictTheSeverity(requestData):
    ## import the dataset
    data = pd.read_csv('Covid_Dataset.csv')

    ## loading the data
    X = data.iloc[ : , : -1].values
    Y = data.iloc[ : , -1].values

    ## data preprocessing

    ######### replace yes with 1 and no with 0
    X_df = pd.DataFrame(X, columns = ['Breathing Problem', 'Fever', 'Dry Cough', 'Sore throat',
       'Running Nose', 'Asthma', 'Chronic Lung Disease', 'Headache',
       'Heart Disease', 'Diabetes', 'Hyper Tension', 'Fatigue ',
       'Gastrointestinal ', 'Abroad travel', 'Contact with COVID Patient',
       'Attended Large Gathering', 'Visited Public Exposed Places',
       'Family working in Public Exposed Places', 'Wearing Masks',
       'Sanitization from Market'])
    X_df.replace(('Yes', 'No'), (1, 0), inplace = True)
    X = X_df

    ########### Label encoding Y 

    from sklearn.preprocessing import LabelEncoder
    encoded_data = LabelEncoder()
    Y = encoded_data.fit_transform(Y)


    ################# split the data into train and test

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state = 1)

    ############### train the model
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    lr = LogisticRegression(solver='lbfgs')
    lr.fit(X_train, Y_train)


    ################# predict the output
    
    test_data = pd.json_normalize(requestData)
    return lr.predict(test_data)

