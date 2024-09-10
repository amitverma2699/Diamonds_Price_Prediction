import pandas as pd
import numpy as np
from src.DiamondsPricePrediction.logger import logging
from src.DiamondsPricePrediction.exception import customexception
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
import os
import sys


class DataIngestionConfig:
    raw_data_path :str = os.path.join("Artifacts","raw.csv")
    train_data_path :str = os.path.join("Artifacts","raw.csv")
    test_data_path :str = os.path.join("Artifacts","raw.csv")

class DataIngestion():
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")

        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv")))

            logging.info("Load the dataset")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Save the Raw data in Artifact folder")

            logging.info("Perform train test split")
            train_data,test_data=train_test_split(data,test_size=0.25)

            logging.info("train test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("Data ingestion part completed")



        except Exception as e:
            logging.info("exception during occured at data ingestion stage")
            raise customexception(e,sys)