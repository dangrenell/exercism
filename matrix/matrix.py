class Matrix:
    def __init__(self, matrix_string):
        row_list = matrix_string.split('\n')
        self.matrix_representation = [elem.split(' ') for elem in row_list]

    def row(self, index):
        index -= 1
        row_list = self.matrix_representation[index]
        return list(map(int, row_list))

    def column(self, index):
        index -= 1
        return [int(elem[index]) for elem in self.matrix_representation]
