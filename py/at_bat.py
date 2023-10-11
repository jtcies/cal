import random


class atBat:
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
        return self.status

    def ground_out(self):
        print("Grounder to second!")
        self.status["outs"] += 1
        return self.status

    def takeAtBat(self):
        roll = random.uniform(0, 1)
        if roll >= 0.9:
            print("It's a line drive into the gap!")
            self.basic_hit(2)
        if roll >= 0.5:
            print("It's a bloop to shallow left")
            self.basic_hit(1)
        else:
            self.ground_out()
