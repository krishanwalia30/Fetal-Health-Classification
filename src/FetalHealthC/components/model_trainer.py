from pathlib import Path
from sklearn.svm import SVC
import pandas as pd
from FetalHealthC.entity import ModelTrainerConfig
from FetalHealthC.logging import logger

from FetalHealthC.utils.common import save_object

class ModelTrainer:
    def __init__(
            self,
            config: ModelTrainerConfig
            ):
        self.config = config
    
    def initiate_model_training(self):
        # Fetching the training data
        data = pd.read_csv(self.config.train_path)
        logger.info("Training Dataset has been fetched.")

        # Splitting the data 
        x_train = data.drop(columns=['fetal_health'], axis=1)
        y_train = data['fetal_health']
        logger.info("Training Dataset has been splitted.")

        # Training the model
        svc_model = SVC(C=80,degree=40)
        svc_model.fit(x_train, y_train)
        logger.info("Model has been trained.")
        
        # Saving the model
        save_object(Path(self.config.model_path), svc_model)
        logger.info("Model has been saved.")
