def angle_to_percent(angle):
    """
    Set function to calculate percent from angle
    :param angle:
    :type angle:
    :return:
    :rtype:
    """
    if angle > 180 or angle < 0:
        return False

    start = 4
    end = 12.5
    ratio = (end - start) / 180  # Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent
