import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
from src.preprocessor_dropna import DropNaPreprocessor
from src.preprocessor_fillmean import FillMeanPreprocessor

class TestPreprocessors(unittest.TestCase):
    def test_dropna_removes_rows(self):
        df = pd.DataFrame({
            "age": [25, None],
            "gender": ["M", None],
            "ethnicity": ["A", "B"]
        })
        dropper = DropNaPreprocessor()
        result = dropper.process(df)
        self.assertEqual(len(result), 1)

    def test_fillna_replaces_with_mean(self):
        df = pd.DataFrame({
            "height": [1.70, None, 1.80],
            "weight": [70, 80, None]
        })
        filler = FillMeanPreprocessor()
        result = filler.process(df)
        self.assertFalse(result.isna().any().any())

if __name__ == "__main__":
    unittest.main()
