class Robot:
    def __init__(self, meno_suboru):
        with open(meno_suboru, 'r') as file:
            content = file.read()
        self.board = []
        self.len_x = 0
        self.len_y = 0
        self.riadok = ''
        self.stlpec = ''
        self.smer = ''
        self.stop = []
        row = []
        for i in range(len(content)):
            if content[i] != '\n':
                row += content[i]
            else:
                self.len_y += 1
                self.board.append(row)
                row = []
        if len(self.board) > 0:
            self.len_x = len(self.board[0])

    def start(self, riadok, stlpec, smer):
        ocistene = 0
        saved = False
        if smer == 0:
            self.board[riadok][stlpec] = '^'
            while riadok >= 0:
                if self.board[riadok][stlpec] == 'X':
                    break
                if self.board[riadok][stlpec] == '2':
                    if riadok - 1 < 0 or self.board[riadok - 1][stlpec] == 'X':
                        self.stop.append([riadok, stlpec])
                        saved = True
                    ocistene += 1
                    self.board[riadok][stlpec] = '1'
                elif self.board[riadok][stlpec] == '1':
                    ocistene += 1
                    self.board[riadok][stlpec] = 'o'
                else:
                    self.board[riadok][stlpec] = 'o'
                if not saved:
                    if [riadok, stlpec] in self.stop:
                        self.board[riadok][stlpec] = '1'
                        self.stop = []
                riadok -= 1
            riadok += 1
            self.board[riadok][stlpec] = '^'
        elif smer == 1:
            self.board[riadok][stlpec] = '>'
            while stlpec < self.len_x:
                if self.board[riadok][stlpec] == 'X':
                    break
                if self.board[riadok][stlpec] == '2':
                    if stlpec + 1 == self.len_x or self.board[riadok][stlpec + 1] == 'X':
                        saved = True
                        self.stop.append([riadok, stlpec])
                    ocistene += 1
                    self.board[riadok][stlpec] = '1'
                elif self.board[riadok][stlpec] == '1':
                    ocistene += 1
                    self.board[riadok][stlpec] = 'o'
                else:
                    self.board[riadok][stlpec] = 'o'
                if not saved:
                    if [riadok, stlpec] in self.stop:
                        self.board[riadok][stlpec] = '1'
                        self.stop = []
                stlpec += 1
            stlpec -= 1
            self.board[riadok][stlpec] = '>'
        elif smer == 2:
            self.board[riadok][stlpec] = 'v'
            while riadok < self.len_y:
                if self.board[riadok][stlpec] == 'X':
                    break
                if self.board[riadok][stlpec] == '2':
                    if riadok + 1 == self.len_y or self.board[riadok + 1][stlpec] == 'X':
                        saved = True
                        self.stop.append([riadok, stlpec])
                    ocistene += 1
                    self.board[riadok][stlpec] = '1'
                elif self.board[riadok][stlpec] == '1':
                    ocistene += 1
                    self.board[riadok][stlpec] = 'o'
                else:
                    self.board[riadok][stlpec] = 'o'
                if not saved:
                    if [riadok, stlpec] in self.stop:
                        self.board[riadok][stlpec] = '1'
                        self.stop = []
                riadok += 1
            riadok -= 1
            self.board[riadok][stlpec] = 'v'
        else:
            self.board[riadok][stlpec] = '<'
            while stlpec >= 0:
                if self.board[riadok][stlpec] == 'X':
                    break
                if self.board[riadok][stlpec] == '2':
                    if stlpec - 1 < 0 or self.board[riadok][stlpec - 1] == 'X':
                        saved = True
                        self.stop.append([riadok, stlpec])
                    ocistene += 1
                    self.board[riadok][stlpec] = '1'
                elif self.board[riadok][stlpec] == '1':
                    ocistene += 1
                    self.board[riadok][stlpec] = 'o'
                else:
                    self.board[riadok][stlpec] = 'o'
                if not saved:
                    if [riadok, stlpec] in self.stop:
                        self.board[riadok][stlpec] = '1'
                        self.stop = []
                stlpec -= 1
            stlpec += 1
            self.board[riadok][stlpec] = '<'

        self.riadok = riadok
        self.stlpec = stlpec
        self.smer = smer
        return ocistene

    def __str__(self):
        board = ''
        for i in range(self.len_y):
            for j in range(self.len_x):
                board += self.board[i][j]
                if j == self.len_x - 1:
                    board += '\n'
        board = board[:-1]
        return board

    def rob(self, povely):
        ocistene = 0
        for i in range(len(povely)):
            if povely[i] == 'l':
                if self.smer == 0:
                    ocistene += self.start(self.riadok, self.stlpec, 3)
                elif self.smer == 1:
                    ocistene += self.start(self.riadok, self.stlpec, 0)
                elif self.smer == 2:
                    ocistene += self.start(self.riadok, self.stlpec, 1)
                elif self.smer == 3:
                    ocistene += self.start(self.riadok, self.stlpec, 2)
                else:
                    pass
            elif povely[i] == 'p':
                if self.smer == 0:
                    ocistene += self.start(self.riadok, self.stlpec, 1)
                elif self.smer == 1:
                    ocistene += self.start(self.riadok, self.stlpec, 2)
                elif self.smer == 2:
                    ocistene += self.start(self.riadok, self.stlpec, 3)
                elif self.smer == 3:
                    ocistene += self.start(self.riadok, self.stlpec, 0)
                else:
                    pass
            elif povely[i] == 'z':
                if self.smer == 0:
                    ocistene += self.start(self.riadok, self.stlpec, 2)
                elif self.smer == 1:
                    ocistene += self.start(self.riadok, self.stlpec, 3)
                elif self.smer == 2:
                    ocistene += self.start(self.riadok, self.stlpec, 0)
                elif self.smer == 3:
                    ocistene += self.start(self.riadok, self.stlpec, 1)
                else:
                    pass
            else:
                pass
        return ocistene

    def pocet_znecistenych(self):
        znecistene = 0
        for i in range(self.len_y):
            for j in range(self.len_x):
                if self.board[i][j] == '2':
                    znecistene += 2
                elif self.board[i][j] == '1':
                    znecistene += 1
                if [i, j] in self.stop:
                    znecistene += 1
        return znecistene


if __name__ == '__main__':
    r = Robot('subor6.txt')
    print(r)
    print('pocet znecistenych =', r.pocet_znecistenych())
    print('start(2, 3, 1) vratil', r.start(68, 1, 2))
    print(r)
    print('pocet znecistenych =', r.pocet_znecistenych())
    r.rob('pllppllppppllppllppllp')
    print(r)
    print("rob('ll') vratil", r.rob('ll'))
    print(r)
    print('pocet znecistenych =', r.pocet_znecistenych())
    print("rob('pzl') vratil", r.rob('pzl'))
    print(r)
    print('pocet znecistenych =', r.pocet_znecistenych())
    print("rob('pp') vratil", r.rob('pp'))
    print(r)
    print('pocet znecistenych =', r.pocet_znecistenych())

    # r = Robot('subor1.txt')
    # print(r)
    # print('pocet znecistenych =', r.pocet_znecistenych())
    # print('start(2, 3, 1) vratil', r.start(2, 3, 1))
    # print(r)
    # print('pocet znecistenych =', r.pocet_znecistenych())
    # print("rob('ll') vratil", r.rob('ll'))
    # print(r)
    # print('pocet znecistenych =', r.pocet_znecistenych())
    # print("rob('pzl') vratil", r.rob('pzl'))
    # print(r)
    # print('pocet znecistenych =', r.pocet_znecistenych())
    # print("rob('pp') vratil", r.rob('pp'))
    # print(r)
    # print('pocet znecistenych =', r.pocet_znecistenych())