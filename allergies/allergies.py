class Allergies:

    allergy_dict = {k: v for k, v in zip(
        'eggs peanuts shellfish strawberries tomatoes chocolate pollen cats'.split(), [2**i for i in range(8)])}

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return 0 != self.allergy_dict[item] & self.score

    @property
    def lst(self):
        return [item for item in self.allergy_dict.keys() if self.allergic_to(item)]
