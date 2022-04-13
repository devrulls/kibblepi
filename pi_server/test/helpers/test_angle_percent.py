from app.helpers.angle_percent import angle_to_percent


class TestAnglePercent:
    def test_angle_90(self):
        # When
        result = angle_to_percent(90)

        # Then
        assert result == 8.25

    def test_angle_180(self):
        # When
        result = angle_to_percent(180)

        # Then
        assert result == 12.5
