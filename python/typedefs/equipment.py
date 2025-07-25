from enum import IntFlag

class Equipment(IntFlag):
    NONE = 0
    BARBELL = 1 << 0
    DUMBBELL = 1 << 1
    RESISTANCE_BAND = 1 << 2
    KETTLEBELL = 1 << 3