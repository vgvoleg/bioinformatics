class DNAIterator():
    def __init__(self, n):
        self.__n = n
        self.__state = ['A']*(n-1) + ['-1'] # bc first next should ret "AAA"
        self.__final_state = ['T']*n

    def next(self):
        index_to_update = self.__n - 1
        while index_to_update != -1:
            curr_dna = self.__state[index_to_update]
            if curr_dna != 'T':
                if curr_dna == 'A':
                    new_dna = 'C'
                elif curr_dna == 'C':
                    new_dna = 'G'
                elif curr_dna == 'G':
                    new_dna = 'T'
                else:
                    new_dna = 'A'

                self.__state[index_to_update] = new_dna
                return self.__state
            self.__state[index_to_update] = 'A'
            index_to_update -= 1

    def has_next(self):
        return self.__state != self.__final_state
