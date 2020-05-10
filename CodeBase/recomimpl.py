# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:38:19 2020

@author: anand
Recommendation System - to recommend the alternative food items which has 
similar nutritional values
1. Preprocessing of data for feature selection
2. Using scikit a python library to apply recommender system for the dataset
"""

import numpy as np
import pandas as pd
import os

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.externals import joblib

datafile= pd.read_excel("sr28abxl\ABBREV.xlsx")

features=['Energ_Kcal',
          'Lipid_Tot_(g)',
          'FA_Sat_(g)',
          'Cholestrl_(mg)',
          'Sodium_(mg)',
          'Carbohydrt_(g)',
          'Fiber_TD_(g)',
          'Sugar_Tot_(g)',
          'Protein_(g)',
          'Vit_D_µg',
          'Calcium_(mg)',
          'Iron_(mg)',
          'Potassium_(mg)']

attributes = datafile[features]
attributes = attributes.dropna()
dataset = attributes

scaled = StandardScaler()
dataset_scaled = scaled.fit_transform(attributes)

dataset["Itemname"] = datafile["Shrt_Desc"]
dataset["NDB_No"] = datafile["NDB_No"]
dataset = dataset.dropna()

dataset.to_csv("Preprocessed_dataset.csv")
np.savetxt("Scaled_dataset.csv", dataset_scaled, delimiter=",")

#Building the model

recommendations = NearestNeighbors(n_neighbors=100, algorithm='auto').fit(dataset_scaled)

item_indices = recommendations.kneighbors(dataset_scaled)[1]

filename = 'finalized_model.sav'

joblib.dump(item_indices, filename)





