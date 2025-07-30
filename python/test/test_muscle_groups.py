import unittest
from collections import Counter
from python.typedefs.muscle_groups import MuscleGroups

class TestMuscleGroups(unittest.TestCase):
    def test_for_collisions(self):
        value_list = [m for m in MuscleGroups.__members__.values()]

        duplicates = [item for item, count in Counter(value_list).items() if count > 1]

        self.assertCountEqual(duplicates, [])


if __name__ == "__main__":
    unittest.main()