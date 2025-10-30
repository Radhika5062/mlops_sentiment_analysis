import os
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from src.utils.main_utils import read_yaml
from src.constant.training_pipeline import SCHEMA_FILE_PATH, PARAMS_FILE_PATH, ORIGINAL_DATA_PATH
from sklearn.model_selection import train_test_split
import sys
import pandas as pd
from src.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info("Entered init method in DataIngestion class")
            self.data_ingestion_config = data_ingestion_config
            self._schema_config = read_yaml(SCHEMA_FILE_PATH)
            self.params_config = read_yaml(PARAMS_FILE_PATH)
        except Exception as e:
            logging.error(f"Error occurred - {e}")
            raise CustomException(e, sys)
    
    def perform_train_test_split_and_save_data(self, df, test_size):
        '''
            This function performs train test split and then stores the data separately
        '''
        try:
            train_data, test_data = train_test_split(df, 
                                                    test_size = test_size, 
                                                    random_state = 42,
                                                    stratify=df.get('category'))
            # Create directories if they do not exist
            train_dir = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(train_dir, exist_ok=True)
            logging.info("Directory to store the test and train data has been created")
            train_data.to_csv(self.data_ingestion_config.training_file_path, index = False, header = True)
            test_data.to_csv(self.data_ingestion_config.testing_file_path, index = False, header = True)
            logging.info("Train and test csv have been created")
        except Exception as e:
            logging.errror(f"Error occured in perform_train_test_split_and_save_data method of DataIngestionclass - {e}")
            raise CustomException(e, sys)
    

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
            try:
                logging.info("Entered the initiate_data_ingestion method of DataIngestion class")
                # Load parametes from the param.yaml file 
                
                logging.info(f'Printing params - {self.params_config}')
                test_size = self.params_config['data_ingestion']['test_size']
                logging.info(f"test_size = {test_size}")
                # Load data
                df = pd.read_csv(ORIGINAL_DATA_PATH)

                logging.info(f'Shape = {df.shape}')

                # Perform train test split
                self.perform_train_test_split_and_save_data(df, test_size)
                
                # Return the artifact
                data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                                test_file_path=self.data_ingestion_config.testing_file_path)
                return data_ingestion_artifact
            except Exception as e:
                logging.error("Error occurred in main function of DataIngestion class - {e}")
                raise CustomException(e, sys)
            
    
def main():
    try:
        logging.info("Starting main method in Data Ingestion file")
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)

        logging.info(f'Artifact Directory - {training_pipeline_config.artifact_dir}')
        logging.info(f'Training file path - {data_ingestion_config.training_file_path}')
        logging.info(f'Testing file path: {data_ingestion_config.testing_file_path}')

        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Exiting main from Data Ingestion File")
        return data_ingestion_artifact
    except Exception as e:
        logging.error(f"Error occurred in main function of Data Ingestion - {e}")
        raise CustomException(e, sys)

if __name__ == '__main__':
    main()
    
