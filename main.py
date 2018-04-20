import importlib
import random
from Agent.rat import *
from Maze.maze import *

POPULATION_SIZE = 1
LIFE_SPAN = 8

def run(population, age):
    for rat in population.pop:
        rat.update(age)
        rat.display()

class Population:

    def __init__(self):
        self.pop = []
        for i in range(0, POPULATION_SIZE):
            self.pop.append(Rat())

def main():

    count = 0
    print("This is the main")
    # r = Rat(randomGeneticSequnce())
    # r.display()
    # print(randomGeneticSequnce())


    # population = []
    # for i in range(0, POPULATION_SIZE):
    #     population.append(Rat())

    ratPop = Population()


    for i in range(15):
        run(ratPop, count)
        count += 1
        if count == LIFE_SPAN:
            ratPop = Population()
            count = 0
            print("The total lifespan has been reached. Starting a new population")




if __name__ == '__main__':
    main()
