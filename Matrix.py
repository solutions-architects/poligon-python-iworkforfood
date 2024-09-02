class Matrix:
    def __init__(self, columns):
        for _ in columns:
            if len(_) != len(columns[0]):
                raise Exception("Size mismatch")
        self.matrix = columns
        self.size = (len(self.matrix[0]), len(self.matrix))


    def __add__(self, columns):
        columns_list = columns.matrix
        new_matx = []
        if len(columns_list) != len(self.matrix):
            raise Exception("Size mismatch")
        for f_matx, s_matx in zip(columns_list, self.matrix):
            if len(f_matx) != len(s_matx):
                raise Exception("Size mismatch")
            new_matx.append([y + x for y, x in zip(f_matx, s_matx)])
        return Matrix(new_matx)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, columns):
        columns_list = columns.matrix
        new_matx = []
        if len(columns_list) != len(self.matrix):
            raise Exception("Size mismatch")
        for f_matx, s_matx in zip(self.matrix, columns_list):
            if len(f_matx) != len(s_matx):
                raise Exception("Size mismatch")
            new_matx.append([y - x for y, x in zip(f_matx, s_matx)])
        return Matrix(new_matx)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, columns):
        if isinstance(columns, int) or isinstance(columns, float):
            columns_list = [[columns if x == y else 0 for x in range(len(self.matrix[0]))] for y in range(len(self.matrix))]
        else:
            columns_list = columns.matrix
        new_matx = []
        if (len(self.matrix[0]) != len(columns_list)):
            raise Exception("Size mismatch")

        for fm_number in range(len(self.matrix)):
            pos_number = []
            for sm_number in range(len(columns_list[0])):
                pos_number.append(sum([x * y for x, y in zip(self.matrix[fm_number], [z[sm_number] for z in columns_list])]))
            new_matx.append(pos_number)
            print(new_matx)
        return Matrix(new_matx)

    def __imul__(self, other):
        return self.__mul__(other)

    def get_matrix(self):
        return self.matrix

    def transpose(self):
        new_m = [[y[x] for y in self.matrix] for x in range(len(self.matrix))]
        return Matrix(new_m)

'''
new_m = Matrix([[0, 1],[0, 2]])
old_m = Matrix([[0, 1],[0, 2]])

no_m = new_m + old_m
no_p = new_m - old_m
no_mu = new_m * old_m
print(new_m.get_matrix())
mul_num = new_m * 4
tr_m = new_m.transpose()

print(no_m.get_matrix(), no_p.get_matrix(), no_mu.get_matrix(), "|", mul_num.get_matrix(), "|", tr_m.get_matrix(), tr_m.size)
'''
