FREEZING_POINT = 0
BOILING_POINT = 100


def state_of_water(temperature):
    if temperature < FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"
