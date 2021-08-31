class Slangetje():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.alive = True

    def introduce(self):
        print(f"Snake name: {self.name}\nSnake size: {self.size}")
        return

    def grow(self):
        self.size += 1

    def shrink(self):
        self.size -= 1

    def die(self):
        self.alive = False
