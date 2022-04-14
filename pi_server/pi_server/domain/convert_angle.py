MIN_SERVO_ANGLE = 4
MAX_SERVO_ANGLE = 12.5


def convert_angle_to_servo_rotation(angle: int) -> float:
    if not 0 <= angle <= 180:
        return False

    servo_rotation = MIN_SERVO_ANGLE + ((MAX_SERVO_ANGLE - MIN_SERVO_ANGLE) / 180) * angle
    return servo_rotation
