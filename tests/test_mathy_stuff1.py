from math_stuff.math_utils import divide


def test_divide_positive_numbers() -> None:
    """Test that divide returns the correct result when given two numbers."""
    assert divide(1, 2) == 0.5
