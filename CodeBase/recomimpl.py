#Load the packages
import numpy as np
import pandas as pd
import os
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
#from sklearn.externals import joblib

#Reading the dataset
datafile= pd.read_excel("sr28abxl\ABBREV.xlsx")

#Extraction of features 
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

#Filtering only the 'Features' columns from the dataset
attributes = datafile[features]

#Drop missing values
attributes = attributes.dropna()
dataset = attributes

#Scaling the cleaned data
scaled = StandardScaler()
dataset_scaled = scaled.fit_transform(attributes)

dataset["Itemname"] = datafile["Shrt_Desc"]
dataset["NDB_No"] = datafile["NDB_No"]
dataset = dataset.dropna()

#Saving Preprocessed data
dataset.to_csv("Preprocessed_dataset.csv")
np.savetxt("Scaled_dataset.csv", dataset_scaled, delimiter=",")

#Building the model using K-NN with K = 100
recommendations = NearestNeighbors(n_neighbors=100, algorithm='auto').fit(dataset_scaled)

#Euclidian Distance Calculation
distances,item_indices = recommendations.kneighbors(dataset_scaled)

#Save to file
filename = 'finalized_model.sav'
distance_file='finalized_model_dist.sav'
joblib.dump(item_indices, filename)
joblib.dump(distances, distance_file)
