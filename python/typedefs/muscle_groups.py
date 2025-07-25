from enum import IntFlag

class MuscleGroups(IntFlag):
    BICEPS = 1 << 0
    TRICEPS = 1 << 1
    DELTOIDS = 1 << 2
    CHEST = 1 << 3
    UPPER_TRAPS = 1 << 4
    MID_TRAPS = 1 << 5
    LOWER_TRAPS = 1 << 6
    RHOMBOIDS = 1 << 7
    LATS = 1 << 8
    RECTUS_ABDOMINUS = 1 << 9
    OBLIQUES = 1 << 10
    GLUTES = 1 << 11
    QUADS = 1 << 12
    HAMSTRINGS = 1 << 13
    CALVES = 1 << 14
    FOREARMS = 1 << 15