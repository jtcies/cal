import random


class atBat:
    """
    This class handles a single at bat. It takes an an argument the inning status.
    A hit will move the runners forward on the bases, and any that cross the plate
    (move beyond the first three elements of the bases list) are added to the
    inning runs score. An out increments the inning outs by one.
    Inning status is returned.
    """

    def __init__(self, status):
        self.status = status

    def basic_hit(self, n_bases):
        # list with true for batter and false for any bases behind him
        if n_bases > 1:
            batter = [False for i in range(n_bases - 1)] + [True]
        else:
            batter = [True]
        # append to front of existing bases list
        new_bases = batter + self.status["bases"]
        # pop the crossed plate bases and sum any with runners
        crossed_plate = [new_bases.pop() for i in range(n_bases)]
        self.status["runs"] += sum(crossed_plate)
        self.status["bases"] = new_bases

    def out(self):
        print("Grounder to second")
        self.status["outs"] += 1

    def take_at_bat(self):
        roll = random.normalvariate(0, 1)
        if roll >= 2:
            print("Home run!!!")
            self.basic_hit(4)
        elif roll >= 1.8:
            print("Triple")
            self.basic_hit(3)
        elif roll >= 1.0:
            print("Double")
            self.basic_hit(2)
        elif roll >= 0.0:
            print("It's a bloop to shallow left")
            self.basic_hit(1)
        else:
            self.out()

        return self.status
