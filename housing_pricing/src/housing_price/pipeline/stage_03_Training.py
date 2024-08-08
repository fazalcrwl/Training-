from housing_price.config.configuration import ConfigurationManager
from housing_price.components.data_training import Datatrain






class TrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_train_config=config.get_train_config()
        data_train=Datatrain(data_train_config)
        data_train.training_load()