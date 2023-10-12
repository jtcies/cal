from game import Game


def main():
    print("Let's play some ball!")
    g = Game()
    g.play_game(n_innings=3)
    print("And that's the ball game")


if __name__ == "__main__":
    main()
