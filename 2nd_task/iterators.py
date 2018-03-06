class NMerIterator():
    def __init__(self, n, max_index):
        self.__n = n
        self.__max_index = max_index
        self.__state = [0]*(n-1) + [-1]
        self.__final_state = [max_index]*n

    def next(self):
        index_to_update = self.__n - 1
        while index_to_update != -1:
            if self.__state[index_to_update] != self.__max_index:
                self.__state[index_to_update] += 1
                return self.__state
            self.__state[index_to_update] = 0
            index_to_update -= 1

    def has_next(self):
        return self.__state != self.__final_state