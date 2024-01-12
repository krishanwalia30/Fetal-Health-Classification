from FetalHealthC.components.data_validation import DataValidation
from FetalHealthC.config.configuration import ConfigurationManager
from FetalHealthC.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):

        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files_exists()
    

if __name__ == "__main__":
    STAGE_NAME = 'Data Validation Stage'

    try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n x=========================x \n\n")

    except Exception as e:
        logger.exception(e)
        raise e