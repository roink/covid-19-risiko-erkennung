# directories_files.R
# Defines project directories and file paths using the 'here' package for robust path management.

# Load the 'here' package
library(here)

## Directories ----
dirs <- list()

# Project root directory (automatically detected by here::here())
dirs$project <- here()

# Subdirectories within the project
dirs$notebooks <- here("notebooks")           # R Markdown notebooks and scripts

dirs$data <- here("data")                 # Main data directory
dirs$data_raw <- here("data", "raw")          # Raw, unprocessed data (e.g., downloaded Kaggle data)
dirs$data_interim <- here("data", "interim")    # Intermediate data transformations, not yet fully processed
dirs$data_processed <- here("data", "processed") # Final, processed data ready for analysis/modeling

dirs$data_modeling_kaggle <- here("data", "interim", "covid19-dataset", "modeldata") # modeling data

dirs$trends <- here("data", "raw", "Trends")      # Directory for Google Trends data (if used)

# Create directories if they don't exist ----

## Create subdirectories within 'data' and other top-level directories
#if (!dir.exists(dirs$data_raw)) dir.create(dirs$data_raw, recursive = TRUE)      # Raw data
#if (!dir.exists(dirs$data_interim)) dir.create(dirs$data_interim, recursive = TRUE) # Interim data
#if (!dir.exists(dirs$data_processed)) dir.create(dirs$data_processed, recursive = TRUE) # Processed data

if (!dir.exists(dirs$trends)) dir.create(dirs$trends, recursive = TRUE)          # Trends data (inside raw data)
if (!dir.exists(dirname(dirs$data_modeling_kaggle))) {
  dir.create(dirname(dirs$data_modeling_kaggle), recursive = TRUE)
}


## Files ----
files <- list()

# File paths for Kaggle Covid19 dataset
files$kaggle_raw <- here("data", "raw", 'covid19-dataset', 'Covid Data.csv') # Raw Kaggle CSV file
files$kaggle_interim <- here("data", "interim", 'covid19-dataset', 'kaggle_covid_data_R.qs') 
files$kaggle_processed <- here("data", "processed", 'covid19-dataset', 'kaggle_covid_data_R.qs')
files$kaggle_model_data <- here("data", "interim", 'covid19-dataset', 'kaggle_covid_data_modeling_R.qs') 



files$gtrends_raw <- file.path(dirs$trends, 'data_trends_covid19_mx_raw.qs')
files$gtrends_interim <- file.path(dirs$trends, 'data_trends_covid19_mx_interim.qs')
