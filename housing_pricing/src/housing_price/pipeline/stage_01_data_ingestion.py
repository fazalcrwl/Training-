from housing_price.entity import DataIngestionConfig
from housing_price.config.configuration import ConfigurationManager
from housing_price.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass 
        
    def main():
        config=ConfigurationManager()
    
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.extract_file()
        