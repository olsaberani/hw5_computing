import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self):
        """Load dataset and return as pandas DataFrame."""
        data = pd.read_csv(self.file_path)
        return data

    def split_data(self, test_size=0.2, random_state=42):
        """Split the data into train and test DataFrames."""
        data = self.load_data()
        train_df, test_df = train_test_split(data, test_size=test_size, random_state=random_state)
        return train_df, test_df


