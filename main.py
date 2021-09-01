from slangetje import Slangetje
from playground import Playground
from game import Game

if __name__ == "__main__":
    # create snake
    slang = Slangetje("Snake")
    slang.shrink()

    # create playground
    garden = Playground("Garden", 30, 30, slang)

    # create game
    game = Game("First", garden)
    game.update_status()

    print("done")
