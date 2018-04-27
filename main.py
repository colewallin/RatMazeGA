import importlib
import random
import time
# from Agent.rat import *
# from Maze.maze import *

POPULATION_SIZE = 50
LIFE_SPAN = 30
MAX_GENERATIONS = 20
MAZE_SIZE = 50

def crossover(genes1, genes2):
    cutpoint = random.randint(0,LIFE_SPAN-1)
    newDNA = [None] * LIFE_SPAN

    for i in range(0, LIFE_SPAN):
        if i < cutpoint:
            newDNA[i] = genes1[i]
        else:
            newDNA[i] = genes2[i]

    return newDNA

def mutate(genes):
    for i in range(LIFE_SPAN):
        # Approximately one gene will get mutate per genetic sequence
        if random.randint(1, LIFE_SPAN) == 1:
            genes[i] = random.randint(0, 1)


def randomGeneticSequnce():
    dna = []
    for i in range(LIFE_SPAN):
        dna.append(random.randint(0, 1))
    return dna

# class DNA:
#     def __init__(self):
#         self.genes = []
#         f or i in range(LIFE_SPAN):
#             self.genes.append(random.randint(0, 1))

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

        # # Normalize the fitness values between 0 and 1
        # for rat in self.pop:
        #     print("Ratfitness preNormalize", rat.fitness)
        #     rat.fitness = rat.fitness / float(mostFit)
        #     print("Ratfitness Normalize", rat.fitness)
        #     # // The most fit rat is obviously going to have a fitness score of
        #     # one with this looop.

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
            mutate(childGenes)
            newPop[i] = Rat(childGenes)

        self.pop = newPop
        self.bestRat = Rat()


    def run(self, age):
        for rat in self.pop:
            rat.update(age)
            # rat.display()

def main():

    count = 0
    generation =  0
    ratPop = Population()


    while generation < MAX_GENERATIONS:

        ratPop.run(count)
        count += 1
        if count == LIFE_SPAN:
            # ratPop = Population()
            ratPop.evaluate()
            ratPop.bestRat.display()
            ratPop.naturalSelection()
            count = 0
            generation += 1
            time.sleep(.1)
            print("The total lifespan has been reached. Starting a new population")
            print()
            print()


class Rat:

    def __init__(self, dna=None):
        if dna == None:
            self.dna = randomGeneticSequnce()
        else:
            self.dna = dna

        self.position = MAZE_SIZE/2
        self.fitness = 0.0
        self.ateTheCheese = False

    def update(self, age):
        if self.position == MAZE_SIZE:
            self.ateTheCheese = True

        # Don't keep moving the rat if it has reached the cheese
        if not self.ateTheCheese:
            if self.dna[age]:
                self.moveRight()
            else:
                self.moveLeft()

    def display(self):
        for val in range(1, MAZE_SIZE+1):
            if val == self.position:
                print(' R ', end='')
            elif val == 1:
                print(' O ', end='')
            elif val == MAZE_SIZE:
                print(' C ', end='')
            else:
                print(' = ', end='')
        print()
        self.printDNA()
        print("Fitness Score of: ", self.fitness)

    def calculateFitness(self):
        distanceFromGoal = MAZE_SIZE - self.position


        # If you got the cheese, double the top fitness (1/1)
        if self.ateTheCheese:
            self.fitness = 1/0.5
        else:
            self.fitness = 1/distanceFromGoal



    def getDNA(self):
        return self.dna

    def printDNA(self):
        for val in self.dna:
            print(val, end="")
        print()


    def moveLeft(self):
        self.position -= 1

    def moveRight(self):
        self.position += 1




if __name__ == '__main__':
    main()
