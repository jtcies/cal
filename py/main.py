from game import Game
from assets import Base
import pygame

N_INNINGS = 3
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


# pygame setup
def main():
    g = Game(n_innings=N_INNINGS)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # Initializing surface
    surface = pygame.display.set_mode((400, 300))

    # Initializing Color
    base_color = (0, 255, 0)

    third = Base(surface, base_color, 3)
    second = Base(surface, base_color, 2)
    first = Base(surface, base_color, 1)
    home = Base(surface, base_color, 4)

    pygame.display.flip()

    while running:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if g.game_status["inning"] > g.n_innings:
                print(
                    "And that's the ball game",
                    "The final score is the current score is",
                    f"""away {g.game_status["away_runs"]}""",
                    f"""home {g.game_status["home_runs"]}""",
                )
                running = False
            elif g.game_status["inning_outs"] < 3:
                g.take_at_bat()
            else:
                if g.game_status["inning"] % 1 == 0:
                    g.game_status["away_runs"] += g.game_status["inning_runs"]
                else:
                    g.game_status["home_runs"] += g.game_status["inning_runs"]
                print(g.game_status)
                print(
                    f"""and that's the end of the {g.game_status["inning"]} inning""",
                    "the current score is",
                    f"""away {g.game_status["away_runs"]}""",
                    f"""home {g.game_status["home_runs"]}""",
                )

                g.new_inning()

        print(g.game_status["bases"])
        third.update_base(g.game_status["bases"][2])
        second.update_base(g.game_status["bases"][1])
        first.update_base(g.game_status["bases"][0])
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
