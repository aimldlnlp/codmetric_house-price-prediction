import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load housing data from CSV file.
    """
    df = pd.read_csv(file_path)
    return df