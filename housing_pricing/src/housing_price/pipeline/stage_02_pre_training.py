from housing_price.config.configuration import ConfigurationManager
from housing_price.components.data_pretrain import DataPretrain






class DataPretrainingPipeline:
    def __init__(self) -> None:
        pass 
        
    def main():
        config=ConfigurationManager()
    
        data_pretrain_config=config.get_pretrain_config()
        data_pretrain=DataPretrain(config=data_pretrain_config)
        data_pretrain.pretrain_data()