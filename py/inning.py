from at_bat import atBat


class Inning:
    """
    The inning has three components: the runners on base, the number of outs,
    and current at bat. The at bat functionality is handled by it's own class.
    Here we loop through at bats and update the bases and outs appropriately.

    Bases is a list of booleans with length 3 (T for runner, F for no runner).
    Outs is an integer. Inning ends when outs > 2.
    """

    def __init__(self):
        self.status = {"bases": [False, False, False], "outs": 0, "runs": 0}

    def play_inning(self):
        while self.status["outs"] < 3:
            a = atBat(self.status)
            a.take_at_bat()
            print(self.status)
