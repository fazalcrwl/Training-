from housing_price.logging import logger 
from housing_price.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from housing_price.pipeline.stage_02_pre_training import DataPretrainingPipeline
from housing_price.pipeline.stage_03_Training import TrainingPipeline


STAGE_NAME= "Data Ingestion stage"
try:
    logger.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
     raise e



STAGE_NAME= "Data Pretrain stage"
try:
    logger.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
    data_pretraining=DataPretrainingPipeline()
    data_pretraining.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
     raise e




STAGE_NAME= "Data train stage"
try:
    logger.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
    training=TrainingPipeline()
    training.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
     raise e

