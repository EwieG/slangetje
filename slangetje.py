class Slangetje():
    def __init__(self, name):
        self.name = name
        self.size = 8
        self.alive = True

    # grow (default 1)
    def grow(self, growSize=1):
        self.size += growSize

    # shrink (default 1)
    def shrink(self, shrinkSize=1):
        self.size -= shrinkSize

    def die(self):
        self.alive = False  # snake dies

    # print status
    def update_status(self):
        print(f"Snake name: {self.name}")
        print(f"Snake size: {self.size}")
        print(f"Snake life status: {'Alive' if self.alive else 'Death'}")
