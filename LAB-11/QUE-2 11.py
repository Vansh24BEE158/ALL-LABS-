print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


class Matrix:
    def __init__(self, matrix):
      
        self.matrix = matrix

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __mul__(self, other):
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return Matrix(result)

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def display(self):
        for row in self.matrix:
            print(row)

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]]) 

print("Matrix 1:")
matrix1.display()

print("\nMatrix 2:")
matrix2.display()

print("\nMatrix 1 + Matrix 2:")
add_result = matrix1 + matrix2
add_result.display()

print("\nMatrix 1 * Matrix 2:")
mul_result = matrix1 * matrix2
mul_result.display()

print("\nTranspose of Matrix 1:")
transpose_result = matrix1.transpose()
transpose_result.display()
