from Matrix import Matrix
import pytest

@pytest.fixture
def matrix_one():
    first_matrix = Matrix([[0, 1],[0, 2]])
    return first_matrix

@pytest.fixture
def matrix_two():
    first_matrix = Matrix([[0, 1],[0, 2]])
    return first_matrix

@pytest.fixture
def add_result():
    f_m = Matrix([[0, 1],[0, 2]])
    s_m = Matrix([[0, 1],[0, 2]])
    result_m = Matrix([[0, 2],[0, 4]])
    return [f_m, s_m, result_m]



