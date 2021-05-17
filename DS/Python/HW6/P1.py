class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        result = False
        if self.area > other.area:
            result = True
        return result

    def population_density(self):
        density = 0
        density = self.population/self.area
        return density
