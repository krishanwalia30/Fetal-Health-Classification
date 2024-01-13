from FetalHealthC.logging import logger
from FetalHealthC.pipeline.stage_01_data_ingestion import DataIngestionTraniningPipeline
from FetalHealthC.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from FetalHealthC.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from FetalHealthC.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = DataIngestionTraniningPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n x=========================x \n\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n x=========================x \n\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Transformation Stage'
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n x=========================x \n\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Model Trainer Stage'
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n x=========================x \n\n")

except Exception as e:
    logger.exception(e)
    raise e