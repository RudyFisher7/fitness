from enum import IntFlag

class WorkTypes(IntFlag):
    DURATION = 1 << 0 # seconds
    DISTANCE = 1 << 1 # meters
    REPS_AND_RESISTANCE = 1 << 2 # count and kg/resistance band color