from enum import IntFlag

class WorkTypes(IntFlag):
    DURATION = 1 << 0
    DISTANCE = 1 << 1
    REPS = 1 << 2
    WEIGHT = 1 << 3
    BAND_COLOR = 1 << 4