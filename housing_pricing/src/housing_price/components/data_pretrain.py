import pandas  as pd 
from sklearn.model_selection import train_test_split
import pickle 
from housing_price.entity import DataPretrainingConfig


class DataPretrain:
   def __init__(self, config:DataPretrainingConfig) :
      self.config= config

   def pretrain_data(self):
      df=pd.read_csv(self.config.unzip_dir)
      X=df.drop('id',axis=1)
      X=X.drop('date',axis=1)
      Y=X['price']
      X=X.drop('price',axis=1)
      xtrain,xtest,ytrain,ytest=train_test_split(X,Y,test_size=0.2,random_state=42)

      

        # Assuming x_train, x_test, y_train, y_test are already defined

        # Create a dictionary to store the data
      data = {
            'x_train': xtrain,
            'x_test': xtest,
            'y_train': ytrain,
            'y_test': ytest
        }

        # Save the dictionary to a pickle file
      with open(self.config.pretrainn_data, 'wb') as f:
            pickle.dump(data, f)

