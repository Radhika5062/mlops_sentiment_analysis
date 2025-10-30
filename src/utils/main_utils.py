import os
import yaml
from src.logger import logging
from src.exception import CustomException
import sys 


def read_yaml(filepath:str) -> dict:
    '''
        Description: This function is used to read yaml files
        Input: YAML file name
        Output: dictionary
    '''
    try:
        logging.info("Entered read_yaml method")
        with open(filepath, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        logging.error(f"Error occurred - {e}")
        raise CustomException(e, sys)

