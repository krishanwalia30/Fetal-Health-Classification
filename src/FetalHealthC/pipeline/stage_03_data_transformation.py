from FetalHealthC.logging import logger
from FetalHealthC.components.data_transformation import DataTransformation
from FetalHealthC.config.configuration import ConfigurationManager


class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass 

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.initate_data_transformation()

if __name__ == "__main__":
    STAGE_NAME = 'Data Transformation Stage'

    try:

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        data_validation = DataTransformationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n x=========================x \n\n")

    except Exception as e:
        logger.exception(e)
        raise e