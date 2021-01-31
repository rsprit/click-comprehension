

class VSummary:

    def __init__(self, base):
        self.base = base

    def protein(self, *ids, pmin, pmax):
        print(f"protein: {self.base},{ids},{pmin},{pmax}")

    def species(self, *ids, opt1, opt2):
        print(f"species: {self.base},{ids},{opt1},{opt2}")
