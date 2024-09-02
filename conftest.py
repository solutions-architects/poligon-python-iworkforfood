from Matrix import Matrix
import pytest

@pytest.fixture
def add_result():
    f_m = Matrix([[0, 1],[0, 2]])
    s_m = Matrix([[0, 1],[0, 2]])
    result_m = Matrix([[0, 2],[0, 4]])
    return [f_m, s_m, result_m]


@pytest.fixture
def sub_result():
    f_m = Matrix([[0, 1],[0, 2]])
    s_m = Matrix([[0, 1],[0, 2]])
    result_m = Matrix([[0, 0],[0, 0]])
    return [f_m, s_m, result_m]

@pytest.fixture
def mul_matrx_result():
    f_m = Matrix([[0, 1],[0, 2]])
    s_m = Matrix([[0, 1],[0, 2]])
    result_m = Matrix([[0, 2], [0, 4]])
    return [f_m, s_m, result_m]

@pytest.fixture
def mul_numb_result():
    f_m = Matrix([[0, 1],[0, 2]])
    numb = 4
    result_m = Matrix([[0, 4],[0, 8]])
    return [f_m, numb, result_m]

@pytest.fixture
def transpose_result():
    f_m = Matrix([[0, 1],[0, 2]])
    result_m = Matrix([[0, 0],[1, 2]])
    return [f_m, result_m]
