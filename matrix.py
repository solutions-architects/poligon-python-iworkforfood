from typing import Self

class Matrix:
    """
    Matrix class

    Represents a mathematical matrix

    """

    def __init__(self: Self, columns: list[list[int | float]]) -> None:
        """init method"""
        for current_column in columns:
            if len(current_column) != len(columns[0]):
                raise Exception("Size mismatch")

        self.matrix = columns

        self.size = (
            len(self.matrix[0]),
            len(self.matrix)
        )


    def __add__(self: Self, added_matrix: Self) -> Self:
        """add method"""
        columns_of_added_matrix = added_matrix.matrix
        new_matrix = []

        if len(columns_of_added_matrix) != len(self.matrix):
            raise Exception("Size mismatch")

        for first_matrix, second_matrix in zip(columns_of_added_matrix, self.matrix):
            if len(first_matrix) != len(second_matrix):
                raise Exception("Size mismatch")
            new_matrix.append(
                [
                    y + x for y, x in zip(first_matrix, second_matrix)
                ]
            )

        return Matrix(new_matrix)

    def __iadd__(self, other: Self) -> Self:
        """iadd method"""
        return self.__add__(other)

    def get_matrix(self) -> list[list[int | float]]:
        """Method for getting matrix representation as an array"""
        return self.matrix

    def __str__(self: Self) -> str:
        """Str method."""
        return str(self.matrix)

