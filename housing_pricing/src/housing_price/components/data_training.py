import pickle 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , mean_squared_error,r2_score
from housing_price.entity import DatatrainingConfig


class Datatrain:
   def __init__(self, config:DatatrainingConfig) :
      self.config= config
   def training_load(self):
      # Load the data from the pickle file in the specified directory
        with open(self.config.pretrainn_data, 'rb') as f:
           data = pickle.load(f)

        # Extract the variables
        x_train = data['x_train']
        x_test = data['x_test']
        y_train = data['y_train']
        y_test = data['y_test']
        model=LinearRegression()
        model.fit(x_train,y_train)
        preds=model.predict(x_test)
        meansqrd=mean_squared_error(y_test,preds)
        meanabs=mean_absolute_error(y_test,preds)
        rscore=r2_score(y_test,preds)
        print("mean_squarred Error:",meansqrd)
        print("mean_abs_error",meanabs)
        print("r2_score",r2_score(y_test,preds))
         
        with open(self.config.model_save, 'wb') as f:
            pickle.dump(model, f)



    

    
