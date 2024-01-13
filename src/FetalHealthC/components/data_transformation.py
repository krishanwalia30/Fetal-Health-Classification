import os
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from FetalHealthC.entity import DataTransformationConfig
from FetalHealthC.logging import logger

from FetalHealthC.utils.common import save_object

class DataTransformation:
    def __init__(
            self,
            data_transformation_config: DataTransformationConfig
            ):
        self.config = data_transformation_config
    
    def save_datasets(self,train_dataset:pd.DataFrame, test_dataset:pd.DataFrame):

        train_dataset.to_csv(Path(self.config.train_path),index=False)
        test_dataset.to_csv(Path(self.config.test_path),index=False)
        logger.info(f"Datasets saved at {self.config.train_path} and {self.config.test_path}")      

    def initate_data_transformation(self):
        # Fetching the dataset
        df = pd.read_csv(os.path.join(self.config.data_path, "fetal_health.csv"))
        logger.info(f"Dataset has been fetched")

        # Spliting the dataset 
        x = df.drop(columns=['fetal_health'], axis=1)
        y = df['fetal_health']
        x_train, x_test, y_train,y_test = train_test_split(x, y, random_state=42, test_size=0.2)
        logger.info(f"Dataset splitted")

        # Preprocessing the dataset 
        std = StandardScaler()
        x_train =std.fit_transform(x_train)
        x_test = std.transform(x_test)
        logger.info(f"Dataset preprocessed")

        # Saving the preprocessor file
        save_object(Path(self.config.preprocessor_path), std)
        logger.info(f"Preprocessor saved at {self.config.preprocessor_path}")

        # Combining both the output and the input features in the numpy array
        train_arr = np.c_[x_train, np.array(y_train)]
        test_arr = np.c_[x_test, np.array(y_test)]
        logger.info(f"Numpy arrays combined")

        # Converting the numpy arrays to the pandas dataframe
        train_df = pd.DataFrame(train_arr, columns= list(df.columns))
        test_df = pd.DataFrame(test_arr, columns= list(df.columns))
        logger.info(f"Pandas Dataframe created for both train and test np arrays")

        # Saving the dataframe to respective files
        self.save_datasets(train_df, test_df)

