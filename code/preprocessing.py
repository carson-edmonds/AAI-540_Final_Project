import argparse
import os
import requests
import tempfile

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

if __name__ == "__main__":
    base_dir = "/opt/ml/processing"

    train = pd.read_csv(
        f"{base_dir}/train1/train_data.csv",
        header=None)
    
    test = pd.read_csv(
        f"{base_dir}/test1/test_data_with_outcome.csv",
        header=None)
    test = test[:round(len(test)*0.8)]
    
    validation = pd.read_csv(
        f"{base_dir}/val1/validation_data.csv",
        header=None)
    
    prod = test[round(len(test)*0.8):].drop(test.columns[0], axis=1)
    print(test.shape)
    print(prod.shape)


    pd.DataFrame(train).to_csv(f"{base_dir}/train2/train.csv", header=False, index=False)
    pd.DataFrame(validation).to_csv(
        f"{base_dir}/validation2/validation.csv", header=False, index=False
    )
    pd.DataFrame(test).to_csv(f"{base_dir}/test2/test.csv", header=False, index=False)
    pd.DataFrame(prod).to_csv(f"{base_dir}/prod2/prod.csv", header=False, index=False)
