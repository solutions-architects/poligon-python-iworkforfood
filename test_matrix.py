from matrix import Matrix

def test_add_method(add_result: Matrix, matrix_one: Matrix, matrix_two: Matrix):
    """Function for testing __add__ method."""
    assert matrix_one + matrix_two == add_result

def test_str_method(str_matrix: str, str_matrix_method_result: str):
    """Function for testing __str__ method."""
    assert str_matrix == str_matrix_method_result