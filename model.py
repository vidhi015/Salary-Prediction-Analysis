import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

dataset=pd.read_csv('C:\\Users\\KESHW\\OneDrive\\Desktop\\DS Prac\\DS Prac\\Data\\hiring.csv')
print(dataset)
dataset['experience'].fillna(0,inplace=True)
dataset['test_score'].fillna(dataset['test_score'].mean(),inplace=True)

x=dataset.iloc[:,:3]

#convert word to integer value
def convert_to_int(word):
    word_dict={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0,0:0}
    return word_dict[word]

x['experience']=x['experience'].apply(lambda x: convert_to_int(x))
y=dataset.iloc[:,-1]

#splitting the dataset into training and test set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x,y)

pickle.dump(regressor,open('model.pkl','wb'))