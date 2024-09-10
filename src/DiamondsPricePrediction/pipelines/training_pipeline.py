from src.DiamondsPricePrediction.components.data_ingestion import DataIngestion


import os
import sys
from src.DiamondsPricePrediction.logger import logging
from src.DiamondsPricePrediction.exception import customexception
import pandas as pd

obj=DataIngestion()

obj.initiate_data_ingestion()