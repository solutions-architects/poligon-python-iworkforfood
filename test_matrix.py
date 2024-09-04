from Matrix import Matrix

def test_add_method(add_result: Matrix, matrix_one: Matrix, matrix_two: Matrix):
    assert (matrix_one + matrix_two).get_matrix() == add_result.get_matrix()

def test_str_method(str_matrix: str, str_matrix_method_result: str):
    assert str_matrix == str_matrix_method_result