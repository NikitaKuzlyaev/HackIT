import itertools


class Ember:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self):
        return Ember(self.y, self.x)

    def __add__(self, other):
        return Ember(self.x, self.y + other.y)


def combine(e1: Ember, e2: Ember) -> list[Ember]:
    res = []

    for p1 in [e1, e1.rotate()]:
        for p2 in [e2, e2.rotate()]:
            if p1.x == p2.x:
                res.append(p1 + p2)

    return res


def solve():
    x1, y1, x2, y2, x3, y3 = map(int, input().split())

    embers = [Ember(x1, y1), Ember(x2, y2), Ember(x3, y3)]

    for order in itertools.permutations([0, 1, 2]):

        for e in combine(embers[order[0]], embers[order[1]]):
            if combine(e, embers[order[2]]):
                return True

    return False


if __name__ == "__main__":
    if solve():
        print("Sorry")
    else:
        print("Me")
