import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from FetalHealthC.entity import ModelEvaluationConfig
from FetalHealthC.utils.common import load_object 
from FetalHealthC.logging import logger
import yaml
 
class ModelEvaluation:
    def __init__(self, model_evaluation_config: ModelEvaluationConfig):
        self.config = model_evaluation_config

    def initiate_model_evaluation(self):
        # Fetching the test dataset
        data = pd.read_csv(self.config.test_path)
        logger.info("Test Dataset has been loaded successfully")

        # Spliting the data into x, y
        LABEL_COLUMN = 'fetal_health'
        x = data.drop(columns=LABEL_COLUMN)
        y = data[LABEL_COLUMN]
        logger.info("Data has been splitted successfully")

        # Fetching the model
        model = load_object(self.config.model_path)
        logger.info("Model has been loaded successfully")

        # Evaluating the model
        y_pred = model.predict(x)
        accuracy = accuracy_score(y, y_pred)
        cm = confusion_matrix(y, y_pred)
        logger.info(f"Accuracy score for model {accuracy}")
        logger.info(f"Confusion matrix for model {cm}")
        logger.info("Model evaluation has been completed successfully")

        # Writing the accuracy in the metrics yaml file
        content = dict()
        content['accuracy'] = str(accuracy)
        content['confusion_matrix'] = str(cm)

        with open(self.config.metrics_file_path, 'w') as f:
            yaml.dump(content,f)
        logger.info(f"{self.config.metrics_file_path} file is saved.")        