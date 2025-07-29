import unittest
import python.onboarding.math as m


class TestMath(unittest.TestCase):
    def test_add_ints(self):
        self.assertEqual(m.add(4, 4), 8)
        self.assertEqual(m.add(0, 0), 0)
        self.assertEqual(m.add(100, 0), 100)
        self.assertNotEqual(m.add(1, 1), 1)
        self.assertNotEqual(m.add(1, 1), 3)
    
    def test_add_floats(self):
        self.assertAlmostEqual(m.add(4.4, 4.4), 8.8, 8)
        self.assertAlmostEqual(m.add(0.0, 0.0), 0.0, 8)
        self.assertAlmostEqual(m.add(4.00000009, 0.0), 4.00000009, 8)
        self.assertNotAlmostEqual(m.add(1.0, 0.00000001), 1.0, 8)
        self.assertNotAlmostEqual(m.add(1.0, 0.00000001), 1.00000002, 8)


# Runs unittest.main() if this module/file was invoked directly, not imported.
if __name__ == "__main__":
    unittest.main()