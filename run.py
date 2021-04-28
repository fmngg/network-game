import game
from game import screen_width, screen_height

if __name__ == "__main__":
    g = game.Game(screen_height, screen_width)
    g.run()
