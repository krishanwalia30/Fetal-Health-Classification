import os
from FetalHealthC.entity import DataValidationConfig
from FetalHealthC.logging import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_files_exists(self) -> bool:
        try:
            # Check if all the files in the required_files list are there or not in the data_path 
            # Create a file in the status_file place and then write the status there in the file

            validation_status = None

            all_files = os.listdir(self.config.data_path)
            for file in all_files:
                if file not in self.config.required_files:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
            
            logger.info(f"Data Validation Status: {validation_status}")
            return validation_status

        
        except Exception as e:
            raise e