import pandas as pd

class FillMeanPreprocessor:
    def __init__(self, columns_to_fill=None):
        if columns_to_fill is None:
            columns_to_fill = ["height", "weight"]
        self.columns_to_fill = columns_to_fill

    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fill NaN values in selected columns with their mean."""
        filled_df = df.copy()
        for col in self.columns_to_fill:
            if col in filled_df.columns:
                filled_df[col] = filled_df[col].fillna(filled_df[col].mean())
        return filled_df
