import sys


# TODO: there must be a more efficient way to do this?

# Given a square matrix, turn it by 90 degrees in anti-clockwise direction
# without using any extra space.

class Matrix:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        #self.rows = [[0] * M] * N  # ERROR: this gives us the SAME row again and again
        self.rows = [[0 for x in range(M)] for x in range(N)] 

    def set_value(self, r, c, value):
        self.rows[r][c] = value

    def get_value(self, r, c):
        return self.rows[r][c]

    def set_row(self, r, value_list):
        self.rows[r] = value_list

    def print_matrix(self):
        for row in self.rows:
            for col_data in row:
                print(col_data, end=' ')
            print()
        print()

    def rotate_counterclockwise(self):
        for r in range(self.N):
            for c in range(self.M):
                print(r, c, self.rows[r][c])
        return

    def rotate_clockwise_simp(self):
        m = Matrix(self.M, self.N)
        for r in range(self.N):
            for c in range(self.M):
                m.set_value(c, self.N - r - 1, self.get_value(r, c))
        return m

    def rotate_counterclockwise_simp(self):
        m = Matrix(self.M, self.N)
        for r in range(self.N):
            for c in range(self.M):
                m.set_value(self.M - c - 1, r, self.get_value(r, c))
        return m


###############################################################################
if __name__ == "__main__":

    m = Matrix(3, 3)
    m.set_row(0, [1, 2, 3])
    m.set_row(1, [4, 5, 6])
    m.set_row(2, [7, 8, 9])

    m = Matrix(4, 3)
    m.set_row(0, [11, 12, 13])
    m.set_row(1, [14, 15, 16])
    m.set_row(2, [17, 18, 19])
    m.set_row(3, [20, 21, 22])

    m.print_matrix()
    m2 = m.rotate_counterclockwise_simp()
    m2.print_matrix()
    m2 = m.rotate_clockwise_simp()
    m2.print_matrix()


