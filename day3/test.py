import os
import traceback

# 247

def main():
    script_dir = os.path.dirname(__file__)
    data_file = os.path.join(script_dir, "data.txt")

    f = None
    try:
        f = open(data_file, "r")
        lines = f.readlines()
        tlines = list(map(trimNewline, lines))
        testSlopes(tlines)
    except Exception as e:
        traceback.print_exc()
    finally:
        f.close()

def trimNewline(line):
    return line.rstrip('\n')

def isTree(vec, lines):
    x = vec.x % len(lines[0])
    return lines[vec.y-1][x-1] == "#"

def testSlopes(lines):
    treeProduct = 1
    slopes = [Vec(1, 1), Vec(3, 1), Vec(5, 1), Vec(7, 1), Vec(1, 2)]
    for slope in slopes:
        treeProduct *= countTrees(lines, slope)

    print(f"Got a tree product of {treeProduct}")

def countTrees(lines, slope):
    print("Testing slop {slope}")
    pos = Vec(1, 1)
    trees = 0

    while(pos.y <= len(lines)):
        if isTree(pos, lines):
            trees += 1
        pos += slope

    print(f"Got {trees} trees for slope {slope}")
    return trees

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Vec(self.x + o.x, self.y + o.y)

    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        return self

    def __str__(self):
        return f"Vec({self.x}, {self.y})"

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise Exception(f"Index {index} is not valid for {self}")


if __name__ == "__main__":
    main()
