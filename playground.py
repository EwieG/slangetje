class Playground():
    def __init__(self, name, x_size, y_size, snake):
        self.name = name
        self.x_size = x_size
        self.y_size = y_size
        self.check_size()
        self.snake = snake

    def check_size(self):
        # adjust sizes if smaller than 24 x 24
        min_size = 24
        if self.x_size < min_size:
            self.x_size = min_size

        if self.y_size < min_size:
            self.y_size = min_size

    # print playground status
    def update_status(self):
        print(f"Playground name: {self.name}")
        print(f"Playground x size: {self.x_size}, y size: {self.y_size}")
