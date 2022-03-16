from app import add


class TestAddition:
    def test_add_10_and_3_returns_13(self):
        # When
        result = add(10, 3)

        # Then
        assert result == 13
