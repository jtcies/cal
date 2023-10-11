import random


class atBat:
    def __init__(self, status):
        self.status = status

    def single(self):
        bases = self.status["bases"]
        bases.insert(0, True)
        bases.pop()
        self.status["bases"] = bases
        return self.status

    def ground_out(self):
        self.status["outs"] += 1
        print("Grounder to second!")
        return self.status

    def takeAtBat(self):
        roll = random.uniform(0, 1)
        if roll >= 0.5:
            self.single()
        else:
            self.ground_out()
        print(roll)
