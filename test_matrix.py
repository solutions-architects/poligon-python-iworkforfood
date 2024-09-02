def test_matrix_operations(add_result, sub_result, mul_matrx_result, mul_numb_result, transpose_result):
    assert (add_result[0] + add_result[1]).get_matrix() == add_result[2].get_matrix()
    assert (sub_result[0] - sub_result[1]).get_matrix() == sub_result[2].get_matrix()
    assert (mul_matrx_result[0] * mul_matrx_result[1]).get_matrix() == mul_matrx_result[2].get_matrix()
    assert (mul_numb_result[0] * mul_numb_result[1]).get_matrix() == mul_numb_result[2].get_matrix()
    assert (transpose_result[0].transpose()).get_matrix() == transpose_result[1].get_matrix()

