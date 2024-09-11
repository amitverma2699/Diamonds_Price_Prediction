from src.DiamondsPricePrediction.components.data_ingestion import DataIngestion
from src.DiamondsPricePrediction.components.data_transformation import DataTransformation
from src.DiamondsPricePrediction.components.model_trainer import ModelTrainer

import os
import sys
from src.DiamondsPricePrediction.logger import logging
from src.DiamondsPricePrediction.exception import customexception
import pandas as pd

obj=DataIngestion()

train_data_path,test_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()

train_arr,test_arr = data_transformation.initiate_data_transformation(train_data_path,test_data_path)

model_trainer_obj=ModelTrainer()

model_trainer_obj.initate_model_training(train_arr,test_arr)

