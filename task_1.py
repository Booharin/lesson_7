class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        my_string_1 = ""
        my_string_2 = ""
        for i in self.matrix_list:
            my_string_1 += " ".join(map(str, i[0:2]))
            my_string_1 += "  "
            my_string_2 += " ".join(map(str, i[-2:]))
            my_string_2 += "  "
        return f"{my_string_1}\n{my_string_2}"

    def __add__(self, other):
        return Matrix(self.matrix_list + other.matrix_list)


matrix = Matrix([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
matrix_2 = Matrix([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(matrix + matrix_2)

# sorry there was little time