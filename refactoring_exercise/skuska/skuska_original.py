class Zahradka:
    def __init__(self, meno_suboru):
        def pridaj(v1, v2, o=''):
            try:
                self.g[v1][v2] = o
            except KeyError:
                self.g[v1] = {v2:o}
        with open(meno_suboru, 'r') as file:
            z = [_.split() for _ in file.read().splitlines()]
        self.g = {}
        self.o = set()
        for _ in z:
            if len(_) == 2:
                pridaj(_[0], _[1])
                pridaj(_[1], _[0])
            elif len(_) == 3:
                self.o.add(_[1])
                pridaj(_[0], _[2], _[1])
                pridaj(_[2], _[0], _[1])

    def vrcholy(self):
        return set(self.g.keys())

    def hrana(self, v1, v2):
        try:
            return self.g[v1][v2]
        except KeyError:
            return None

    def typy_ovocia(self):
        return self.o

    def backtracking(self, v, hrany, z, prejdene):
        if prejdene >= self.o:
            self.riesenie = z.copy()
            return
        else:
            for _ in self.g[v]:
                if not {(v, _), (_, v)} <= hrany and (self.hrana(_, v) == '' or self.hrana(_, v) not in prejdene) and not self.riesenie:
                    self.backtracking(_, hrany | {(v, _), (_, v)}, z + [_], prejdene | {self.hrana(_, v)})

    def start(self, v1):
        self.riesenie = []
        self.backtracking(v1, set(), [v1], set())
        return self.riesenie

if __name__ == '__main__':
    z = Zahradka('subor1.txt')
    for v1, v2 in ('3','2'), ('2','3'), ('5','4'), ('2','6'), ('5','1'):
        print(f'hrana({v1!r}, {v2!r}) = {z.hrana(v1, v2)!r}')
    print('typy ovocia =', z.typy_ovocia())
    for v1 in sorted(z.vrcholy()):
        print(f'trasa z {v1!r}:', z.start(v1))
