import random


class Hat:
    houses = ["Griffondor", "Slytherin"]

    @classmethod
    def guess(cls, name):
        return random.choice(cls.houses)


print(Hat.guess("Henry"))
