import pandas as pd
from abc import ABC, abstractmethod

class FeatureTransformer(ABC):
    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


class BMIFeature(FeatureTransformer):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df.copy()
        if "height" in result.columns and "weight" in result.columns:
            result["BMI"] = result["weight"] / ((result["height"] / 100) ** 2)
        return result


class AgeGroupFeature(FeatureTransformer):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df.copy()
        if "age" in result.columns:
            result["age_group"] = pd.cut(
                result["age"],
                bins=[0, 18, 35, 50, 65, 120],
                labels=["child", "young_adult", "adult", "middle_age", "senior"]
            )
        return result

