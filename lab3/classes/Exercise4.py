class PointClass:
    def __init__(self, position = [0, 0], moved = [0, 0], distance = 0):
        self.position = position
        self.moved    = moved
        self.distance = distance

    def show(self):
        print(self.position)

    def move(self, x, y):
        self.distance     = (((self.position[0] - x) ** 2) +((self.position[0] - y) ** 2)) ** 0.5
        self.position[0] += x
        self.position[1] += y

    def dist(self):
        print(self.distance)

a = PointClass(position = [1, 1], moved = [0, 0], distance = 0)
a.show()
a.move(x = 2, y = 6)
a.show()
a.dist()