import os

# Define the download function
def download_covid19_dataset(download_path=None):
    """
    Downloads the COVID-19 dataset into the raw data folder if it hasn't been downloaded before.
    """
    
    # Determine the base directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Set default download path if not provided
    if download_path is None:
        download_path = os.path.join(base_dir, "..", "data", "raw")
    
    # Define the path where the data will be downloaded
    destination_path = os.path.join(download_path, "covid19-dataset")
    
    # Check if the data has already been downloaded
    if os.path.exists(destination_path):
        print(f"Dataset already exists at {destination_path}. Skipping download.")
        return

    # Create the download directory if it doesn't exist
    os.makedirs(download_path, exist_ok=True)
    
    # Use the Kaggle API to download the dataset
    try:
        import kaggle
        print("Downloading COVID-19 dataset from Kaggle...")
        kaggle.api.dataset_download_files(
            "meirnizri/covid19-dataset",
            path=destination_path,
            unzip=True
        )
        print(f"Dataset successfully downloaded and extracted to {destination_path}.")
    except Exception as e:
        print(f"An error occurred while downloading the dataset: {e}")


if __name__ == "__main__":
    download_covid19_dataset()

