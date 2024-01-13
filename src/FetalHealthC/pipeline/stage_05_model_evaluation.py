from FetalHealthC.components.model_evaluation import ModelEvaluation
from FetalHealthC.logging import logger
from FetalHealthC.config.configuration import ConfigurationManager


class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass 

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.initiate_model_evaluation()

if __name__ == "__main__":
    try:
        STAGE_NAME = 'Model Evaluation Stage'

        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        model_evaluation = ModelEvaluationTrainingPipeline()
        model_evaluation.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n x=========================x \n\n")

    except Exception as e:
        logger.exception(e)
        raise e