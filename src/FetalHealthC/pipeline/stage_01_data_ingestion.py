from FetalHealthC.components.data_ingestion import DataIngestion
from FetalHealthC.config.configuration import ConfigurationManager
from FetalHealthC.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self)->None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    STAGE_NAME = 'Data Ingestion Stage'

    try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        data_validation = DataIngestionTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n x=========================x \n\n")

    except Exception as e:
        logger.exception(e)
        raise e