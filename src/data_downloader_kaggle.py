import os
import argparse
import kaggle
import logging

def parse_arguments():
    parser = argparse.ArgumentParser(description="Download COVID-19 dataset from Kaggle.")
    parser.add_argument('--data_path', type=str, help='Path to download the data')
    parser.add_argument('--destination_folder', type=str, help='Destination folder name')
    parser.add_argument('--kaggle_repo', type=str, default='arashnic/covid19-case-surveillance-public-use-dataset', help='Kaggle repository')
    return parser.parse_args()

def configure_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

def download_kaggle_dataset(  
    data_path: str = None,
    destination_folder: str = None, 
    kaggle_repo: str = None
) -> None:
    """
    Downloads the a dataset from Kaggle and extracts it to the specified directory.
    Args:
        data_path (str, optional): The directory where the dataset should be downloaded.
                                        If not provided, defaults to '../data/raw' relative to the script location.
        destination_folder (str, optional): The folder name where the dataset should be extracted.
                                            If not provided, defaults to the kaggle_repo name with '/' replaced by '_'.
        kaggle_repo (str, optional): The Kaggle repository identifier for the dataset.
                                     Defaults to 'arashnic/covid19-case-surveillance-public-use-dataset' in parse_arguments().
    Notes:
        - Ensure that the Kaggle API is properly configured with your credentials before running this function.
    """
    
    logger = configure_logging()
    
    # Check if kaggle_repo is defined
    if not kaggle_repo:
        raise ValueError("The 'kaggle_repo' parameter is required and cannot be None or empty.")
    
    # Determine the base directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Set default download path if not provided
    if data_path is None:
        data_path = os.path.join(base_dir, "..", "data", "raw")
    os.makedirs(data_path, exist_ok=True)
    
    # Set default destination folder if not provided
    if destination_folder is None:
        destination_folder = kaggle_repo.replace("/", "_")
    
    # Define the path where the data will be downloaded
    destination_path = os.path.join(data_path, destination_folder)
    
    # Check if the data has already been downloaded and not empty
    if os.path.exists(destination_path) and os.listdir(destination_path):
        logger.info(f"Dataset already exists at {destination_path}. Skipping download.")
        return
    
    # Use the Kaggle API to download the dataset
    try:
        logger.info("Downloading COVID-19 dataset from Kaggle...")
        kaggle.api.dataset_download_files(
            kaggle_repo,
            path=destination_path,
            unzip=True
        )
        logger.info(f"Dataset successfully downloaded and extracted to {destination_path}.")
    except kaggle.rest.ApiException as api_error:
        logger.error(f"An API error occurred while downloading the dataset: {api_error}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    args = parse_arguments()
    download_kaggle_dataset(args.data_path, args.destination_folder, args.kaggle_repo)
