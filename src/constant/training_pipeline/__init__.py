import os

TARGET_COLUMN = 'category'
PIPELINE_NAME = 'sentiment_analysis'
ARTIFACT_DIR = 'artifact'

ORIGINAL_DATA_PATH = 'notebooks\dataset.csv'
PARAMS_FILE_PATH = 'params.yaml'

SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

FILE_NAME = "sentiment.csv"

TRAIN_FILE_NAME:str = 'train.csv'
TEST_FILE_NAME:str = 'test.csv'

# Data ingestuib related constants
DATA_INGESTION_COLLECTION_NAME:str = 'sentiment_analysis'
DATA_INGESTION_DIR_NAME:str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR:str = 'feature_store'
DATA_INGESTON_INGESTED_DIR:str = 'ingested'
