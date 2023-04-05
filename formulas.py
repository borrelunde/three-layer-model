import math

from matter import Matter


# 6.3 Transmission through a fluid layer: Normal incidence

def intensity_transmission_coefficient(
        layer_one: Matter,
        layer_two: Matter,
        layer_three: Matter,
        frequency: float,
        L: float) -> float:
    """
    Calculate three-layer model intensity transmission coefficient.

    :param layer_one:   matter
    :param layer_two:   matter
    :param layer_three: matter
    :param frequency:   frequency in Hertz
    :param L:           layer two length in meters
    :return:            intensity transmission coefficient [-]
    """

    c1 = layer_one.velocity
    c2 = layer_two.velocity
    c3 = layer_three.velocity
    r1 = layer_one.density * c1
    r2 = layer_two.density * c2
    r3 = layer_three.density * c3

    omega = 2 * math.pi * frequency
    k2 = omega / c2  # wave number for layer 2

    return 4 / (2 + (((r3 / r1) + (r1 / r3)) * math.cos(k2 * L) ** 2) + (
            (((r2 ** 2) / (r1 * r3)) + ((r1 * r3) / (r2 ** 2))) * math.sin(k2 * L) ** 2))
