from matrix import Matrix
import pytest

@pytest.fixture
def matrix_one() -> Matrix:
    """Fixture to create a first ``Matrix`` instance."""
    first_matrix = Matrix([[0, 1],[0, 2]])
    return first_matrix

@pytest.fixture
def matrix_two() -> Matrix:
    """Fixture to create a second ``Matrix`` instance."""
    second_matrix = Matrix([[0, 1],[0, 2]])
    return second_matrix

@pytest.fixture
def add_result(matrix_one: Matrix, matrix_two: Matrix) -> Matrix:
    """
    Fixture to create a result ``Matrix``

    This matrix is the result of addition of the first and second matrices

    """
    result_m = Matrix([[0, 2],[0, 4]])
    return result_m

@pytest.fixture
def str_matrix(matrix_one: Matrix) -> str:
    """Fixture to determine string representation of the first matrix."""
    str_result = str(matrix_one)
    return str_result

@pytest.fixture
def str_matrix_method_result(matrix_one: Matrix) -> str:
    """Fixture to determine the result of using of th __str__ method."""
    str_result = matrix_one.__str__()
    return str_result


