# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:54:01 2019

@author: johan
"""

import pickle
from flask import Flask, request
import numpy as np
import pandas as pd

with open('C:/Users/johan/Desktop/ds/adn/api/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)


@app.route('/predict',methods=['POST'])   
def predict():
    
    prediction = model.predict([[np.array(['Land Size', 'Fodder', 'Fodder Type', 'Cow Shed', 'Water Collection',
       'Vet Assistace', 'AI Services', 'Dairy Cows', 'Lactations'])]])
    return str(prediction)

def predict_milk_data():
   
    input_data = pd.read_csv(request.files.get('C:/Users/johan/Desktop/ds/adn/Milk Baseline Data.csv'))
    prediction = model.predict(input_data)
    return str(list(prediction))

if __name__ == '__main__':
    app.run()