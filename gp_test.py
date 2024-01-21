class Individual:
    """
    Represents an individual in the population - tree of nodes,
    which corresponds to a program in the language.
    """

    def __init__(self):
        self.genome = []


class GPTest:

    def __init__(self, no_generations: int, population_size: int, tournament_size: int,
                 mutation_rate: float, crossover_rate: float):
        self.no_generations = no_generations
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

        self.population = []

    def _create_random_population(self):
        for i in range(self.population_size):
            self.population.append(Individual())