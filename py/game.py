import random


class Game:
    """
    This class handles game level logic. Games are initialized with a game_status
    that includes inning, home and away runs.
    When a new inning starts, the game_status inning is incremented by 0.5.
    The number of runs scored in the inning is added to the game_status
    runs (away if inning is .0, home if .5)
    """

    def __init__(self, n_innings):
        self.game_status = {
            "inning": 0.0,
            "home_runs": 0,
            "away_runs": 0,
            "bases": [False, False, False],
            "inning_outs": 0,
            "inning_runs": 0,
            "last_hit": None,
        }
        self.n_innings = n_innings

    def basic_hit(self, n_bases):
        # list with true for batter and false for any bases behind him
        if n_bases > 1:
            batter = [False for i in range(n_bases - 1)] + [True]
        else:
            batter = [True]
        # append to front of existing bases list
        new_bases = batter + self.game_status["bases"]
        # pop the crossed plate bases and sum any with runners
        crossed_plate = [new_bases.pop() for i in range(n_bases)]
        self.game_status["bases"] = new_bases
        if self.game_status["inning"] % 1 == 0:
            self.game_status["away_runs"] += sum(crossed_plate)
        else:
            self.game_status["home_runs"] += sum(crossed_plate)

    def new_inning(self):
        self.game_status["inning"] += 0.5
        self.game_status["inning_outs"] = 0
        self.game_status["inning_runs"] = 0
        self.game_status["bases"] = [False, False, False]

    def out(self):
        self.game_status["inning_outs"] += 1

    def take_at_bat(self):
        roll = random.normalvariate(0, 1)
        if roll >= 2:
            self.basic_hit(4)
            self.game_status["last_hit"] = "Home run!"
        elif roll >= 1.8:
            self.basic_hit(3)
            self.game_status["last_hit"] = "Triple"
        elif roll >= 1.0:
            self.basic_hit(2)
            self.game_status["last_hit"] = "Double"
        elif roll >= 0.0:
            self.basic_hit(1)
            self.game_status["last_hit"] = "Single"
        else:
            self.out()
            self.game_status["last_hit"] = "Out"
