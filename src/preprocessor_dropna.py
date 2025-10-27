import pandas as pd

class DropNaPreprocessor:
    def __init__(self, columns_to_check=None):
        if columns_to_check is None:
            columns_to_check = ["age", "gender", "ethnicity"]
        self.columns_to_check = columns_to_check

    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove rows with NaN values in specific columns."""
        cleaned_df = df.dropna(subset=self.columns_to_check)
        return cleaned_df

