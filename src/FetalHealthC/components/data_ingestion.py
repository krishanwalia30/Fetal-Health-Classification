import os
import urllib.request as request
import zipfile
from FetalHealthC.entity import DataIngestionConfig
from FetalHealthC.logging import logger


class DataIngestion:
    def __init__(
            self,
            data_ingestion_config: DataIngestionConfig
            ):
        self.config = data_ingestion_config
    
    def download_file(self):
        
        if os.path.exists(self.config.local_data_file):
            logger.info(f"File already exists: {self.config.local_data_file}")
            
        else :
            filename, headers = request.urlretrieve(
                url= self.config.source_URL,
                filename = self.config.local_data_file
            )

            logger.info(f"File downloaded: {filename} with the following \n {headers}")

    def extract_zip_file(self):
        """
        zip_file_path:str
        Extracts the zip file into the data directory
        Function returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  