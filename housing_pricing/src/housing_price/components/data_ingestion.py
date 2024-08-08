from housing_price.entity import DataIngestionConfig
import os 
import zipfile






class DataIngestion:
   def __init__(self, config:DataIngestionConfig) :
      self.config= config

   def extract_file(self):
      print(self.config)
      if  os.path.exists(self.config.local_data_file):
         
         
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)

      