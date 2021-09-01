class Game():
    def __init__(self, name, playground):
        self.name = name
        self.lives = 3
        self.playground = playground

    def play(self):
        print("playing")

    def update_status(self):
        print("-----\nGame status\n-----")
        print(f"Game name: {self.name}")
        print(f"Game lives: {self.lives}")
        print("-----\nPlayground status\n-----")
        self.playground.update_status()
        print("-----\nSnake status\n-----")
        self.playground.snake.update_status()
