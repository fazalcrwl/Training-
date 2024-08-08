


import pickle
from housing_price.entity import PredictConfig










class Predict():
     def __init__(self, config:PredictConfig) :
      self.config= config

     def predict(self,dataframe):
        with open(self.config.model_save, 'rb') as f:
           model = pickle.load(f)

        x=model.predict(dataframe)
        return x
