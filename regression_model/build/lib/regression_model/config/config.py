import pathlib
import os, sys
import pandas as pd

import regression_model

#pd.options.display.max_rows = 10
#pd.options.display.max_columns = 10


PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TESTING_DATA_FILE = "test.csv"
TRAINING_DATA_FILE = "train.csv"
TARGET = "price"
FEATURES = ['id', 'url', 'region', 'region_url', 'year', 'manufacturer', 'model',
       'condition', 'cylinders', 'fuel', 'odometer', 'title_status',
       'transmission', 'vin', 'drive', 'size', 'type', 'paint_color',
       'image_url', 'description', 'county', 'state', 'lat', 'long',
       'ori_cost_prc']

# variables
vars_to_retain = ['manufacturer', 'year','odometer', 'transmission', 'type', 'ori_cost_prc']


PIPELINE_NAME = 'price_model_pipe'
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
