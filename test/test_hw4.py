import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import datetime
from hw4 import (
    count_simba,
    get_day_month_year,
    compute_distance,
    sum_general_int_list,
)

class TestHW4Functions(unittest.TestCase):
    def test_count_simba(self):
        sentences = [
            "Simba and Nala are lions.",
            "I laugh in the face of danger.",
            "Hakuna matata",
            "Timon, Pumba and Simba are friends, but Simba could eat the other two."
        ]
        result = count_simba(sentences)
        self.assertEqual(result, 3)

    def test_get_day_month_year(self):
        dates = [
            datetime.date(2024, 5, 20),
            datetime.date(2025, 1, 1)
        ]
        df = get_day_month_year(dates)
        self.assertListEqual(list(df.columns), ["day", "month", "year"])
        self.assertEqual(df.loc[0, "year"], 2024)
        self.assertEqual(df.loc[1, "month"], 1)

    def test_compute_distance(self):
        pairs = [((41.23, 23.5), (41.5, 23.4))]
        result = compute_distance(pairs)
        self.assertIsInstance(result, list)
        self.assertTrue(result[0] > 0)

    def test_sum_general_int_list(self):
        list_1 = [[2], 3, [[1, 2], 5]]
        list_2 = [[2], 4, 5, [1, [2], [3, 5, [7, 8]], 10], 1]
        result1 = sum_general_int_list(list_1)
        result2 = sum_general_int_list(list_2)
        self.assertEqual(result1, 13)
        self.assertEqual(result2, 48)

if __name__ == "__main__":
    unittest.main()
