import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    
    def test_calculate_bmi(self):
        """Test BMI calculation with height 1.75m and weight 70kg."""
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
    
    def test_calculate_bmr_male(self):
        """Test BMR calculation for male with height 175cm, weight 70kg, and age 25."""
        self.assertAlmostEqual(calculate_bmr(175, 70, 25, 'male'), 1706.69, places=2)
    
    def test_calculate_bmr_female(self):
        """Test BMR calculation for female with height 160cm, weight 60kg, and age 30."""
        self.assertAlmostEqual(calculate_bmr(160, 60, 30, 'female'), 1384.14, places=2)
    
    def test_calculate_bmr_invalid_gender(self):
        """Test BMR with invalid gender input."""
        result = calculate_bmr(170, 70, 25, 'unknown')
        self.assertEqual(result, "Invalid gender")
    
    def test_calculate_bmi_edge_case(self):
        """Test BMI with edge case (BMI over 30, obese)."""
        self.assertAlmostEqual(calculate_bmi(1.70, 90), 31.14, places=2)
    
    def test_calculate_bmr_edge_case(self):
        """Test BMR for older age (60 years old)."""
        self.assertAlmostEqual(calculate_bmr(175, 70, 60, 'male'), 1510.44, places=2)
    
    def test_calculate_bmi_invalid(self):
        """Test BMI with invalid input (height 0)."""
        with self.assertRaises(ZeroDivisionError):
            calculate_bmi(0, 70)  # Zero height should raise an error
    
    def test_calculate_bmr_invalid(self):
        """Test BMR with invalid age (negative value)."""
        result = calculate_bmr(175, 70, -5, 'male')
        self.assertEqual(result, "Invalid age")

if __name__ == '__main__':
    unittest.main()
