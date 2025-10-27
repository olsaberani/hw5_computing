import pandas as pd
from sklearn.linear_model import LogisticRegression

class Model:
    def __init__(self, feature_cols: list[str], target_col: str, **hyperparams):
        #private attributes
        self._feature_cols = feature_cols
        self._target_col = target_col
        self._hyperparams = hyperparams

        #public attribute
        self.model = LogisticRegression(**hyperparams)

    def train(self, df: pd.DataFrame) -> None:
        """Train the model using the selected feature and target columns."""
        X = df[self._feature_cols]
        y = df[self._target_col]
        self.model.fit(X, y)

    def predict(self, df: pd.DataFrame) -> pd.Series:
        """Return predicted probabilities for the positive class."""
        X = df[self._feature_cols]
        probs = self.model.predict_proba(X)[:, 1]
        return pd.Series(probs, index=df.index)

