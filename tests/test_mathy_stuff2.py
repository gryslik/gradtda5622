def test_divide_negative_numbers() -> None:
    """
    Test that divide returns the correct result when given a positive and
    a negative number.
    """
    assert divide(5, -2) == -2.5
    assert divide(-2, 5) == -0.4
