def climbingStaircase(n, k):
    rs = Staircase().climb(n, k)
    return sorted(rs)


class Staircase:
    def __init__(self):
        self.mem = dict()

    def climb(self, n, k):
        print(f"climbingStaircase({n}, {k})")
        if n == 1:
            return [[1]]
        elif n == 0:
            return [[]]
        rs = []
        for i in range(n-1, max(n-k, 0)-1, -1):
            if i in self.mem:
                paths = self.mem[i]
            else:
                paths = climbingStaircase(i, k)
                self.mem[i] = paths
            for path in paths:
                print(f"i={i}, n={n}, path={path}, append={[n-i]}")
                rs.append(path + [n-i])
        print(f"climbing({n}), return rs={rs}")
        print(f"mem={self.mem}")
        return rs


print(climbingStaircase(4, 2))
