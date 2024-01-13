from FetalHealthC.logging import logger
import os
import pandas as pd
from FetalHealthC.utils.common import load_object


class PredictionPipeline:

    def __init__(self, filename):
        self.filename = filename

    def load_model(self):
        model = load_object(os.path.join("artifacts","model_trainer", "model.pkl"))
        return model
    

    def load_preprocessor(self):
        preprocessor = load_object(os.path.join("artifacts","data_transformation", "preprocessor.pkl"))
        return preprocessor
    
    def load_data(self):
        data = pd.read_csv(self.filename)
        return data
    
    def predict(self):

        # Fetching the data
        data = self.load_data()
        logger.info("Data loaded Successfully")

        # Fetching the model
        model = self.load_model()
        logger.info("Model loaded Successfully")

        # Fetching the preprocessor
        preprocessor = self.load_preprocessor()
        logger.info("Preprocessor loaded Successfully")

        # transforming the data
        data = preprocessor.transform(data)
        logger.info("Data transformed Successfully")

        # predicting the data
        predictions = model.predict(data)
        logger.info("Data predicted Successfully")

        return predictions