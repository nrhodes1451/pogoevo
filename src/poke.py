class poke():
    def __init__(self, species, ivs, level, moveset):
        self.species = species
        self.ivs = ivs
        self.level = level
        self.moveset = moveset
        self.stats = self.calculate_stats(species, ivs, level)

    def calculate_stats(self, species, ivs, level)
        s