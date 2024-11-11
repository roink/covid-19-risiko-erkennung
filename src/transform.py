# transform.py

import os
from src.load_covid19 import load_covid19
import pandas as pd

# Use __file__ to get the directory of the current script
current_dir = os.path.dirname(__file__)

def clean_covid19():
    df = load_covid19()
    
    # Specify column types and map Boolean variables
    bool_columns = ['PNEUMONIA', 'PREGNANT', 'DIABETES', 'COPD', 'ASTHMA', 'INMSUPR', 
                    'HIPERTENSION', 'CARDIOVASCULAR', 'RENAL_CHRONIC', 'OTHER_DISEASE', 'OBESITY', 'TOBACCO', 
                    'INTUBED', 'ICU']

    missing_values = [97, 98, 99]

    # Convert Boolean columns to 'bool' and map values (Yes -> 1, No -> 0)
    for col in bool_columns:
        df[col] = df[col].map({1: 1, 2: 0}).astype('boolean')
    df.replace({col: missing_values for col in bool_columns if col in df.columns}, pd.NA, inplace=True)

    # df['SEX'] = df['SEX'].map({1: 'female', 2: 'male'})
    df.replace('SEX', pd.NA, inplace=True)
    df['SEX'] = df['SEX'].astype('category')

    # df['PATIENT_TYPE'] = df['PATIENT_TYPE'].map({1: 'athome', 2: 'hospitalization'})
    # df.replace('PATIENT_TYPE', pd.NA, inplace=True)
    # df['PATIENT_TYPE'] = df['PATIENT_TYPE'].astype('category')

    # DATE_DIED column alive value is '9999-99-99'
    df.DATE_DIED = df.DATE_DIED.apply(lambda x: 0 if x == "9999-99-99" else 1)

    # Replace DATE_DIED with DIED (True if actual date, False otherwise)
    df['DIED'] = df['DATE_DIED'].astype('boolean')

    # Drop the original DATE_DIED column
    df.drop('DATE_DIED', axis=1, inplace=True)
    
    # --------------------------------------
    # Fix missing values RC, CK
    
    # Scale the age column using normalization
    # This technique preserves the distribution and shifts values to a 0 to 1 scale
    df['AGE'] = (df['AGE'] - df['AGE'].min()) / (df['AGE'].max() - df['AGE'].min())

    # male cannot be pregnant
    df.loc[df.SEX == 'male', 'PREGNANT'] = False
    # zuhause kann nicht beatmet werde & intubiert werden
    df.loc[df.PATIENT_TYPE==1,'ICU']=False
    df.loc[df.PATIENT_TYPE==1,'INTUBED']=False
    
    # Drop rows with NaN values
    df.dropna(axis=0, inplace=True)
    
    # --------------------------------------





    
    # Define the file path and ensure the directory exists
    file_dir = os.path.join(os.path.dirname(current_dir), "data", "interim")
    os.makedirs(file_dir, exist_ok=True)  # Create directory if it doesn't exist
       
    file_path = os.path.join(file_dir, "covid-data-clean.csv")
    print('Saving clean dataset to: ' + file_path)
    
    # Save the cleaned dataframe to CSV
    df.to_csv(file_path, index=False)  # Exclude index when saving
    
    print('Saved')
