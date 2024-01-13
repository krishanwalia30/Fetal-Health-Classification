from FetalHealthC.logging import logger
from FetalHealthC.components.model_trainer import ModelTrainer
from FetalHealthC.config.configuration import ConfigurationManager


class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass 

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.initiate_model_training()

if __name__ == __name__:
    try:
        STAGE_NAME = 'Model Trainer Stage'

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        model_trainer = ModelTrainerTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n x=========================x \n\n")

    except Exception as e:
        logger.exception(e)
        raise e