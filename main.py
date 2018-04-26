import importlib
import random
import time
from Agent.rat import *
from Maze.maze import *

POPULATION_SIZE = 5
LIFE_SPAN = 20

def crossover(genes1, genes2):
    cutpoint = random.randint(0,LIFE_SPAN-1)
    newDNA = [None] * LIFE_SPAN

    for i in range(0, LIFE_SPAN):
        if i < cutpoint:
            newDNA[i] = genes1[i]
        else:
            newDNA[i] = genes2[i]

    return newDNA


class Population:

    def __init__(self):
        self.pop = []
        self.matingPool = []
        self.bestRat = Rat()
        for i in range(0, POPULATION_SIZE):
            self.pop.append(Rat())

    def evaluate(self):
        mostFit = 0.0
        for rat in self.pop:
            rat.calculateFitness()

            # Find the rat with the highest fitness.
            if rat.fitness > mostFit:
                mostFit = rat.fitness
        print("mostFit: ", mostFit)

        # Normalize the fitness values between 0 and 1
        for rat in self.pop:
            print("Ratfitness preNormalize", rat.fitness)
            rat.fitness = rat.fitness / float(mostFit)
            print("Ratfitness Normalize", rat.fitness)
            # // The most fit rat is obviously going to have a fitness score of
            # one with this looop.

        for rat in self.pop:
            if rat.fitness > self.bestRat.fitness:
                self.bestRat = rat


        self.matingPool = []
        for rat in self.pop:
            amount = int(rat.fitness * 100)
            for i in range(amount):
                self.matingPool.append(rat)

    def naturalSelection(self):
        newPop = [None] * POPULATION_SIZE
        for i in range(0, POPULATION_SIZE):
            parentGenes1 = random.choice(self.matingPool).dna
            parentGenes2 = random.choice(self.matingPool).dna
            childGenes = crossover(parentGenes1, parentGenes2)
            newPop[i] = Rat(childGenes)

        self.pop = newPop
        self.bestRat = Rat()


    def run(self, age):
        for rat in self.pop:
            rat.update(age)
            # rat.display()

def main():

    count = 0

    ratPop = Population()


    for i in range(300):
        # time.sleep(.1)
        ratPop.run(count)
        count += 1
        if count == LIFE_SPAN:
            # ratPop = Population()
            ratPop.evaluate()
            ratPop.bestRat.display()
            ratPop.naturalSelection()
            count = 0

            print("The total lifespan has been reached. Starting a new population")





















if __name__ == '__main__':
    main()
