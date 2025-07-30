from enum import IntFlag, auto

class AutoIntFlag(IntFlag):
    def _generate_next_value_(name, start, count, last_values):
        return 1 << count

class MuscleGroups(AutoIntFlag):
    FOREARMS = auto()
    BICEPS = auto()
    TRICEPS = auto()

    CHEST_UPPER = auto()
    CHEST_LOWER = auto()

    DELTOIDS_FRONT = auto()
    DELTOIDS_MIDDLE = auto()
    DELTOIDS_REAR = auto()
    TRAPS_UPPER = auto()

    NECK = auto()

    TRAPS_MIDDLE = auto()
    TRAPS_LOWER = auto()
    RHOMBOIDS = auto()
    LATS = auto()

    ERECTOR_SPINAE = auto()
    SERRATUS_ANTERIOR = auto()
    ABS = auto()
    OBLIQUES = auto()

    GLUTE_MNAXIMUS = auto()
    GLUTE_MEDIUS = auto()
    GLUTES_MINIMUS = auto()
    HIP_ADDUCTORS = auto()
    HIP_ABDUCTORS = auto()

    QUADS = auto()
    HAMSTRINGS = auto()
    CALVES = auto()
    OTHER = auto()

    ARMS = FOREARMS | BICEPS | TRICEPS
    ARMS_UPPER = BICEPS | TRICEPS
    CHEST = CHEST_UPPER | CHEST_LOWER
    SHOULDERS = DELTOIDS_FRONT | DELTOIDS_MIDDLE | DELTOIDS_REAR | TRAPS_UPPER
    BACK_UPPER = TRAPS_UPPER | TRAPS_MIDDLE | TRAPS_LOWER | RHOMBOIDS | LATS
    CORE = ABS | OBLIQUES | SERRATUS_ANTERIOR
    GLUTES = GLUTE_MNAXIMUS | GLUTE_MEDIUS | GLUTES_MINIMUS
    LEGS = GLUTES | HIP_ADDUCTORS | HIP_ABDUCTORS | QUADS | HAMSTRINGS | CALVES
    POSTERIOR_CHAIN = BACK_UPPER | ERECTOR_SPINAE | GLUTES | HAMSTRINGS