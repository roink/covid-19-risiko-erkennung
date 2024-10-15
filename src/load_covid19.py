# load_covid19.py

import os
from src.data_downloader import download_covid19_dataset
import pandas as pd

# Use __file__ to get the directory of the current script
current_dir = os.path.dirname(__file__)

def load_covid19():
    download_covid19_dataset()  
    
    file_path = os.path.join(os.path.dirname(current_dir), "data", "raw", "covid19-dataset", "Covid Data.csv")
    df = pd.read_csv(file_path)
    
    return df

def load_clean_covid19():
    from src.transform import clean_covid19
    clean_covid19()

    file_path = os.path.join(os.path.dirname(current_dir), "data", "interim", "covid-data-clean.csv")
    print(f"Loading clean dataset from: {file_path}")  # Debugging output
    df = pd.read_csv(file_path, low_memory=False)
    
    bool_columns = ['PNEUMONIA', 'PREGNANT', 'DIABETES', 'COPD', 'ASTHMA', 'INMSUPR', 
                    'HIPERTENSION', 'CARDIOVASCULAR', 'RENAL_CHRONIC', 'OTHER_DISEASE', 'OBESITY', 'TOBACCO', 
                    'INTUBED', 'ICU', 'DIED']
    
    for col in bool_columns:
        df[col] = df[col].map({1: True, 0: False, pd.NA: pd.NA}).astype('boolean')
    
    df['PATIENT_TYPE'] = df['PATIENT_TYPE'].astype('category')
    df['SEX'] = df['SEX'].astype('category')
    
    return df

