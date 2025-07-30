from enum import IntFlag

class WorkTypes(IntFlag):
    DURATION = 1 << 0 # seconds
    DISTANCE = 1 << 1 # meters
    RESISTANCE = 1 << 2 # kg/resistance band color
    REPS = 1 << 3 # count