import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    
    def test_calculate_bmi(self):
        """Test BMI calculation with height 1.75m and weight 70kg."""
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
    
    def test_calculate_bmi_edge_case(self):
        """Test BMI with edge case (BMI over 30, obese)."""
        self.assertAlmostEqual(calculate_bmi(1.70, 90), 31.14, places=2)
      
    def test_calculate_bmi_invalid(self):
        """Test BMI with invalid input (height 0)."""
        with self.assertRaises(ZeroDivisionError):
            calculate_bmi(0, 70)  # Zero height should raise an error
    
    def test_calculate_bmr_male(self):
        # Test for male BMR calculation
        self.assertAlmostEqual(calculate_bmr(175, 70, 25, 'male'), 1706.69, places=2)

    def test_calculate_bmr_female(self):
        # Test for female BMR calculation
        self.assertAlmostEqual(calculate_bmr(160, 60, 30, 'female'), 1384.14, places=2)

    def test_calculate_bmr_edge_case(self):
        # Test for an edge case for an older age
        self.assertAlmostEqual(calculate_bmr(175, 70, 60, 'male'), 1510.44, places=2)
        
    def test_calculate_bmr_invalid(self):
        # Test for invalid age input
        self.assertEqual(calculate_bmr(175, 70, -5, 'male'), "Invalid age")

if __name__ == '__main__':
    unittest.main()
