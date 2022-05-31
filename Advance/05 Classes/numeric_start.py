# give objects number-like behavior
import os 
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)

    # TODO: implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # TODO: implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # TODO: implement in-place addition
    def __iadd__(self, other):
        pass


def main():
    # Declare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # TODO: Add two points
    p3 = p1 + p2
    print(p3)
    # TODO: subtract two points
    p4 = p1 - p2
    print(p4)
    # TODO: Perform in-place addition


if __name__ == "__main__":
    main()
