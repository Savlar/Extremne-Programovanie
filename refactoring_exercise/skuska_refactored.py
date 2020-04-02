# extreme programming refactoring exercise


class Robot:

    def __init__(self, file_name):
        with open(file_name, 'r') as file:
            self.board = [list(x) for x in file.read().split('\n')[:-1]]
        self.row = -1
        self.col = -1
        self.direction = -1
        self.moved = -1
        self.standing_on_dirty = False

    def move(self, lst, start):
        cleaned = 0
        self.moved = 0
        for i in range(start, len(lst)):
            if lst[i] == 'X':
                break
            if lst[i] == '2':
                cleaned += 1
                lst[i] = '1'
            else:
                if lst[i] == '1':
                    cleaned += 1
                lst[i] = 'o'
            self.moved += 1
        return cleaned

    def go_up(self):
        col = [row[self.col] for row in self.board][::-1]
        row = len(self.board) - self.row
        cleaned = self.move(col, row)
        for i in range(1, len(col) + 1):
            self.board[i - 1][self.col] = col[-i]
        self.row -= self.moved
        self.standing_on_dirty = True if self.board[self.row][self.col] == '1' else False
        self.board[self.row][self.col] = '^'
        return cleaned

    def go_down(self):
        col = [row[self.col] for row in self.board]
        cleaned = self.move(col, self.row + 1)
        for i in range(len(col)):
            self.board[i][self.col] = col[i]
        self.row += self.moved
        self.standing_on_dirty = True if self.board[self.row][self.col] == '1' else False
        self.board[self.row][self.col] = 'v'
        return cleaned

    def go_right(self):
        row = self.board[self.row]
        cleaned = self.move(row, self.col + 1)
        self.col += self.moved
        self.standing_on_dirty = True if self.board[self.row][self.col] == '1' else False
        self.board[self.row][self.col] = '>'
        return cleaned

    def go_left(self):
        row = self.board[self.row][::-1]
        col = len(row) - self.col
        cleaned = self.move(row, col)
        for i in range(1, len(row) + 1):
            self.board[self.row][i - 1] = row[-i]
        self.col -= self.moved
        self.standing_on_dirty = True if self.board[self.row][self.col] == '1' else False
        self.board[self.row][self.col] = '<'
        return cleaned

    def start(self, row, col, direction):
        if self.col == -1:
            self.row = row
            self.col = col

        self.direction = direction
        if self.standing_on_dirty:
            self.board[self.row][self.col] = '1'
        else:
            self.board[self.row][self.col] = 'o'
        self.standing_on_dirty = False
        if direction == 0:
            return self.go_up()
        elif direction == 1:
            return self.go_right()
        elif direction == 2:
            return self.go_down()
        else:
            return self.go_left()

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.board)

    def rob(self, povely):
        cleaned = 0
        directions = {'l': {0: 3, 1: 0, 2: 1, 3: 2}, 'p': {0: 1, 1: 2, 2: 3, 3: 0}, 'z': {0: 2, 1: 3, 2: 0, 3: 1}}
        for char in povely:
            cleaned += self.start(self.row, self.col, directions[char][self.direction])
        return cleaned

    def pocet_znecistenych(self):
        dirty = sum([int(x) if x in '12' else 0 for row in self.board for x in row])
        return dirty if not self.standing_on_dirty else dirty + 1


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

    r = Robot('subor1.txt')
    print(r)
    print('pocet znecistenych =', r.pocet_znecistenych())
    print('start(2, 3, 1) vratil', r.start(2, 3, 1))
    print(r)
    print('pocet znecistenych =', r.pocet_znecistenych())
    print("rob('ll') vratil", r.rob('ll'))
    print(r)
    print('pocet znecistenych =', r.pocet_znecistenych())
    print("rob('pzl') vratil", r.rob('pzl'))
    print(r)
    print('pocet znecistenych =', r.pocet_znecistenych())
    print("rob('pp') vratil", r.rob('pp'))
    print(r)
    print('pocet znecistenych =', r.pocet_znecistenych())
