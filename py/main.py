from game import Game
from assets import Base
import pygame

N_INNINGS = 3
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


# pygame setup
def main():
    g = Game(n_innings=N_INNINGS)
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    font = pygame.font.SysFont(None, 24)

    # Initializing Color
    base_color = (0, 255, 0)
    occupied_base = (255, 0, 0)

    third = Base(surface, base_color, occupied_base, 3)
    second = Base(surface, base_color, occupied_base, 2)
    first = Base(surface, base_color, occupied_base, 1)
    home = Base(surface, base_color, occupied_base, 4)

    pygame.display.flip()

    while running:
        ## render game status
        third.update_base(g.game_status["bases"][2])
        second.update_base(g.game_status["bases"][1])
        first.update_base(g.game_status["bases"][0])

        surface.fill(pygame.Color("black"), (200, 0, 400, 400))
        result = font.render(g.game_status["last_hit"], True, (0, 0, 255))
        inning_number = font.render(str(g.game_status["inning"]), True, (0, 0, 255))
        away_runs = font.render(str(g.game_status["away_runs"]), True, (0, 0, 255))
        home_runs = font.render(str(g.game_status["home_runs"]), True, (0, 0, 255))
        outs = font.render(str(g.game_status["inning_outs"]), True, (0, 0, 255))
        surface.blit(result, (200, 30))
        surface.blit(outs, (200, 60))
        surface.blit(inning_number, (200, 90))
        surface.blit(away_runs, (200, 120))
        surface.blit(home_runs, (200, 150))

        pygame.display.flip()

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
                g.new_inning()

        clock.tick(60)  # limits FPS to 60


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
