class DNAWordTree():
    def __init__(self, n):
        self.__n = n
        self.__state = ['A']*(n)

    def current_word(self, i):
        return self.__state[0:i]

    def next_vertex(self, i):
        if i < self.__n - 1:
            self.__state[i + 1] = 'A'
            return i + 1
        else:
            for j in range(self.__n - 1, -1, -1):
                if self.__state[j] != 'T':
                    self.__state[j] = inc_dna(self.__state[j])
                    return j
        return -1

    def bypass_move(self, i):
        for j in range(i, -1, -1):
            if self.__state[j] != 'T':
                self.__state[j] = inc_dna(self.__state[j])
                return j
        return -1


def inc_dna(dna):
    new_dna = ''
    if dna == 'A':
        new_dna = 'C'
    elif dna == 'C':
        new_dna = 'G'
    elif dna == 'G':
        new_dna = 'T'
    return new_dna

if __name__ == '__main__':
    s = DNAWordTree(4)
    i = 0
    while i!=-1:
        i = s.next_vertex(i)
        print(s.current_word())