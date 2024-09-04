from Matrix import Matrix
import pytest

@pytest.fixture
def matrix_one() -> Matrix:
    first_matrix = Matrix([[0, 1],[0, 2]])
    return first_matrix

@pytest.fixture
def matrix_two() -> Matrix:
    second_matrix = Matrix([[0, 1],[0, 2]])
    return second_matrix

@pytest.fixture
def add_result(matrix_one: Matrix, matrix_two: Matrix) -> Matrix:
    result_m = Matrix([[0, 2],[0, 4]])
    return result_m

@pytest.fixture
def str_matrix(matrix_one: Matrix) -> str:
    str_result = str(matrix_one)
    return str_result

@pytest.fixture
def str_matrix_method_result(matrix_one: Matrix) -> str:
    str_result = matrix_one.__str__()
    return str_result


