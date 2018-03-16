class StartIndexesTree():
    def __init__(self, n, max_index):
        self.__n = n
        self.__max_index = max_index
        self.__state = [0]*(n)

    def current_indexes(self):
        return self.__state

    def next_vertex(self, i):
        if i < self.__n - 1:
            self.__state[i + 1] = 0
            return i + 1
        else:
            for j in range(self.__n - 1, -1, -1):
                if self.__state[j] < self.__max_index:
                    self.__state[j] += 1
                    return j
        return -1

    def bypass_move(self, i):
        for j in range(i, -1, -1):
            if self.__state[j] < self.__max_index:
                self.__state[j] += 1
                return j
        return -1

