import re
import unittest
from erotima1 import compute

class TestComputeFunction(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(compute("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(2,3)"), 6)
        self.assertEqual(compute("ΑΒΓΠΟΛΛΑΠΛΑΣΙΑΣΕ(5,4)XYZ"), 20)
        self.assertEqual(compute("123ΠΟΛΛΑΠΛΑΣΙΑΣΕ(7,8)456"), 56)
        self.assertEqual(compute("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(9,10)ΠΟΛΛΑΠΛΑΣΙΑΣΕ(2,2)"), 90 + 4)
        self.assertEqual(compute("Χωρίς πολλαπλασιασμούς"), 0)
    
    def test_with_file(self):
        with open("test_multiplications1.txt", "r", encoding="utf-8") as file:
            data = file.read().strip()
        matches = re.findall(r"ΠΟΛΛΑΠΛΑΣΙΑΣΕ\((\d{2}), (\d{2})\)", data)
        result = compute(data)
        print("Sum:", result)
        self.assertEqual(compute(data), 1035105)

if __name__ == "__main__":
    unittest.main()
 