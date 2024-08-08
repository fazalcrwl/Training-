from housing_price.constants import config_file_path,params_file_path
from housing_price.utils.common import read_yaml, create_directories
from housing_price.entity import DataIngestionConfig,DataPretrainingConfig,DatatrainingConfig,PredictConfig


class ConfigurationManager:
    def __init__(self,
                 config_file_path=config_file_path,
                 params_file_path=params_file_path
                 
                 
                 ):
        
        self.config=read_yaml(config_file_path)

        self.params=read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion

        print(config.local_data_file)
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
          
            root_path=config.root_dir,
            source_url=config.source_url,
            local_data_file= config.local_data_file,
            
            unzip_dir=config.unzip_dir
            


        )
        return data_ingestion_config
    
    def get_pretrain_config(self) -> DataPretrainingConfig:
        config=self.config.data_pretraining

        
        create_directories([config.root_dir])

        data_pretrain_config=DataPretrainingConfig(
          
            root_dir=config.root_dir,
            unzip_dir=config.unzip_dir,
            pretrainn_data=config.pretrainn_data
            


        )
        return data_pretrain_config
    
    def get_train_config(self) -> DatatrainingConfig:
        config=self.config.data_training

        
        create_directories([config.root_dir])

        data_train_config=DatatrainingConfig(
          
            root_dir=config.root_dir,
            pretrainn_data=config.pretrainn_data,
            model_save=config.model_save
            


        )
        return data_train_config
    
    
    def get_predict_config(self) -> PredictConfig:
        config=self.config.data_training

        
        create_directories([config.root_dir])

        predict_config=PredictConfig(
          
            root_dir=config.root_dir,
            
            model_save=config.model_save
            


        )
        return predict_config