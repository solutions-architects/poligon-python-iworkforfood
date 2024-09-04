from Matrix import Matrix

if __name__ == "__main__":

    first_matrix = Matrix([[0, 1],[0, 2]])
    print("String representation of the first marix", first_matrix.__str__())
    second_matrix = Matrix([[0, 1],[0, 2]])
    result_matrix = first_matrix + second_matrix
    print(result_matrix.get_matrix(),
          result_matrix.get_matrix(),
          result_matrix.get_matrix())