from FetalHealthC.logging import logger
from FetalHealthC.pipeline.stage_01_data_ingestion import DataIngestionTraniningPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = DataIngestionTraniningPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n x=========================x \n\n")

except Exception as e:
    logger.exception(e)
    raise e