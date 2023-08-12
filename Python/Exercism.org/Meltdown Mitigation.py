
def is_criticality_balanced(temperature, neutrons_emitted):
    if (temperature < 800) and (neutrons_emitted > 500):
        if ((temperature * neutrons_emitted) < 500000):
            return True
        else:
            return False
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    PERCENTAGE = (generated_power / theoretical_max_power) * 100
    if (PERCENTAGE >= 80):
        return 'green'
    elif (80 > PERCENTAGE >= 60):
        return 'orange'
    elif (60 > PERCENTAGE >= 30):
        return 'red'
    elif (30 > PERCENTAGE):
        return 'black'


def fail_safe(temp, neutrons_per_second, threshold):
    HEAT = (temp * neutrons_per_second)
    if HEAT < (0.9 * threshold):
        return 'LOW'
    elif (HEAT < (1.1 * threshold)):
        return 'NORMAL'
    else:
        return 'DANGER'
