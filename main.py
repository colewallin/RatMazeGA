import importlib
import random
import time
from Agent.rat import *
from Maze.maze import *

POPULATION_SIZE = 1
LIFE_SPAN = 8

def crossover(genes1, genes2):
    cutpoint = random.randint(1,len(genes1))
    newDNA = []

    for i in range(len(genes1)):
        if i < cutpoint:
            newDNA[i] = genes1[i]
        else:
            newDNA[i] = genes2[i]

    return newDNA

def naturalSelection(matingPool, currentPopulation):
    newPop = Population()
    for rat in currentPopulation:
        parentGenes1 = random.choice(matingPool).dna
        parentGenes2 = random.choice(matingPool).dna
        childGenes = crossover(parentGenes1, parentGenes2)
        rat = Rat(childGenes)

class Population:

    def __init__(self):
        self.pop = []
        self.matingPool = []
        for i in range(0, POPULATION_SIZE):
            self.pop.append(Rat())

    def evaluate(self):
        mostFit = 0
        for rat in self.pop:
            rat.calculateFitness()

            # Find the rat with the highest fitness.
            if rat.fitness > mostFit:
                mostFit = rat.fitness

        # Normalize the fitness values between 0 and 1
        for rat in self.pop:
            rat.fitness = rat.fitness / mostFit

        for rat in self.pop:
            amount = rat.fitness * 100
            for i in range(amount):
                self.matingPool.append(rat)

        self.matingPool = []

    def run(self, age):
        for rat in self.pop:
            rat.update(age)
            rat.display()

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


    for i in range(50):
        time.sleep(.1)
        ratPop.run(count)
        count += 1
        if count == LIFE_SPAN:
            ratPop = Population()
            count = 0
            print("The total lifespan has been reached. Starting a new population")




if __name__ == '__main__':
    main()
