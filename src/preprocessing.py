from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import pandas as pd

def preprocess_data(df: pd.DataFrame):
    """
    Clean and split the dataset.
    """
    # Drop rows with missing values (or use imputation)
    df = df.dropna()

    # Feature-target split
    X = df.drop("median_house_value", axis=1)
    y = df["median_house_value"]

    # One-hot encoding if needed
    X = pd.get_dummies(X)

    return train_test_split(X, y, test_size=0.2, random_state=42)
