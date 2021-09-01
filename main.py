from slangetje import Slangetje
from playground import Playground

if __name__ == "__main__":
    slang = Slangetje("Snake")
    slang.shrink(0)
    slang.update_status()
    garden = Playground("Garden", 30, 30, slang)
    garden.update_status()
    print("done")
