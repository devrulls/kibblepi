from pi_server.domain.convert_angle import convert_angle_to_servo_rotation


class TestConvertAngle:
    def test_angle_90_should_return_8_25(self):
        # Given
        angle = 90

        # When
        servo_rotation = convert_angle_to_servo_rotation(angle)

        # Then
        assert servo_rotation == 8.25
