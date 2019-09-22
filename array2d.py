class Array2D:
    def __init__(self, rows, cols):
        self.__data = []
        self.__row = rows
        self.__col = cols
        for row in range(rows):
            tmp = []
        for col in range(cols):
            tmp.append(None)


self.__data.append(tmp)


def to_string(self):
    print(self.__data)


def get_num_rows(self):
    return self.__row


def get_num_cols(self):
    return self.__col


def clearing(self, value):
    for row in range(self.__row):
        for col in range(self.col):
            self.__data[row][col] = value


def set_item(self, r, c, valor):
    if (r >= 0 and r < self.row) and (c >= 0 and c < self.col):
        self.__[r][c] = valor


def main():
    main()