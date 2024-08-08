from housing_price.config.configuration import ConfigurationManager
from housing_price.components.predict import Predict




class PredictPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self,data_frame):
        config=ConfigurationManager()
        predict_config=config.get_predict_config()
        predict=Predict(predict_config)
        x=predict.predict(data_frame)
        return x

