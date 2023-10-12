from inning import Inning


class Game:
    """
    This class handles game level logic. Games are initialized with a game_status
    that includes inning, home and away runs.
    When a new inning starts, the game_status inning is incremented by 0.5.
    The number of runs scored in the inning is added to the game_status
    runs (away if inning is .0, home if .5)
    """

    def __init__(self):
        self.game_status = {"inning": 0.0, "home_runs": 0, "away_runs": 0}

    def play_game(self, n_innings):
        for i in range(n_innings * 2):
            self.game_status["inning"] += 0.5
            i = Inning()
            i.play_inning()
            if self.game_status["inning"] % 1 != 0:
                self.game_status["away_runs"] += i.status["runs"]
            else:
                self.game_status["home_runs"] += i.status["runs"]
            print(self.game_status)
            print(
                f"""
            and that's the end of the {self.game_status["inning"]} inning
            the current score is away {self.game_status["away_runs"]}
            home {self.game_status["home_runs"]}
            """
            )
