import importlib
import random
import time
import math
# from Agent.rat import *
# from Maze.maze import *

### TODO: print average DNA, Average Starting Position, Average Fitness (factor in the weirdness regarding doubling successful rats having 200% fitness),

# base pop 50
# base lifespan 25
# max gen always 200
# base maze size = 30
# base mutation rate is 1/25

POPULATION_SIZE = 50
LIFE_SPAN = 25
MAX_GENERATIONS = 200
MAZE_SIZE = 30


def binaryToLR(num):
    if num is 1:
        return 'R'
    elif num is 0:
        return 'L'
    else:
        return 'E'

def dnaArrayToString(dna):
    consolidatedDNA = ''.join(map(binaryToLR, dna))
    return consolidatedDNA


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
        if random.randint(1, math.floor(LIFE_SPAN)) == 1:
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
            # rat.calculateFitnessLinear()
            rat.calculateFitnessExpo()

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
    bestRatPerGen = []
    ratPop = Population()

    filename = input("Save results into file:")
    file_object = open(filename, 'w+')

    file_object.write("Population Size,Life Span,Max Generations,Maze Size\n")
    file_object.write(str(POPULATION_SIZE) + ',' +  str(LIFE_SPAN) + ',' + str(MAX_GENERATIONS) + ',' + str(MAZE_SIZE) + '\n')
    file_object.write('\n')
    file_object.write("Current Generation,Best Rat's Starting Position,Best DNA,Best Fitness Score,Best Reached Goal,Average Fitness Score (No Winners),Average Fitness Score(Winner Inclusive),% Pop Reached Goal\n")

    while generation < MAX_GENERATIONS:
        ratPop.run(count) # run the population number of steps until lifespan of a rat, where lifespan is length of DNA sequence.
        count += 1

        # all rats in population have run until the end of their DNA sequence. evaluate the population, and display stats for best rat.
        # following that, perform natural selection on population to create a new population/generation.
        if count == LIFE_SPAN:
            print("Generation ", generation+1)
            # ratPop = Population()
            ratPop.evaluate()
            ratPop.bestRat.display()
            bestRatPerGen.append(ratPop.bestRat)

            numRatsInPopThatAteCheese = 0
            for rat in ratPop.pop:
                if rat.ateTheCheese:
                    numRatsInPopThatAteCheese+=1
            percentPopAteCheese = (numRatsInPopThatAteCheese / len(ratPop.pop)) * 100

            popFitness = 0
            for rat in ratPop.pop:
                popFitness+=rat.fitness

            avgFitness = (popFitness / len(ratPop.pop))

            exclusivePopFitnessAccumulator = 0
            numRatsInExclusivePop = 0
            exclusiveAverageFitness = ''
            allRatsSucceeded = True
            for rat in ratPop.pop:
                if rat.ateTheCheese is False:
                    exclusivePopFitnessAccumulator+=rat.fitness
                    numRatsInExclusivePop+=1
                    allRatsSucceeded = False
            if allRatsSucceeded is True:
                exclusiveAverageFitness = 'N/A'
            else:
                exclusiveAverageFitness = str((exclusivePopFitnessAccumulator/numRatsInExclusivePop))

            file_object.write(str(generation + 1) + ',' + str(ratPop.bestRat.startingPosition) + ',' + dnaArrayToString(ratPop.bestRat.dna) + ',' + str(ratPop.bestRat.fitness) + ',' + str(ratPop.bestRat.ateTheCheese) + ',' + str(exclusiveAverageFitness) + ',' + str(avgFitness) + ',' + str(percentPopAteCheese) + '%' + '\n')

            ratPop.naturalSelection()
            count = 0
            generation += 1
            time.sleep(.1)
            if generation is not MAX_GENERATIONS:
                print("Creating a new generation")
            print()
            print()

    file_object.write('\n')
    gens_until_first_success = 1
    cheese_eaten = False

    for rat in bestRatPerGen:
        if rat.ateTheCheese:
            cheese_eaten = True
            break
        else:
            gens_until_first_success+=1
    if cheese_eaten:
        file_object.write('First generation where best rat ate the cheese: ' + str(gens_until_first_success) + '\n')
    else:
        file_object.write('The cheese was never eaten by the best rat in any generation.\n')
    file_object.close()

class Rat:

    def __init__(self, dna=None):
        if dna == None:
            self.dna = randomGeneticSequnce()
        else:
            self.dna = dna

        self.position = int(MAZE_SIZE/2)
        self.startingPosition = self.position
        self.fitness = 0.0
        self.ateTheCheese = False
        self.fellInTheHole = False

    def update(self, age):
        if self.position == MAZE_SIZE:
            self.ateTheCheese = True

        # Don't keep moving the rat if it has reached the cheese
        if not self.ateTheCheese and not self.fellInTheHole:
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

    def calculateFitnessExpo(self):
        distanceFromGoal = MAZE_SIZE - self.position


        # If you got the cheese, double the top fitness (1/1)
        if self.ateTheCheese:
            self.fitness = 1/0.5
        elif self.fellInTheHole:
            self.fitness = 1/(distanceFromGoal*2)
        else:
            self.fitness = 1/distanceFromGoal

    def calculateFitnessLinear(self):
        self.fitness = self.position / 10.0
        # print(self.fitness)

    def getDNA(self):
        return self.dna

    def printDNA(self):
        for val in self.dna:
            print(val, end="")
        print()


    def moveLeft(self):
        self.position -= 1
        if self.position == MAZE_SIZE:
            self.ateTheCheese = True
        if self.position == 1:
            print("A rat fell in the hole.")
            self.fellInTheHole = True

    def moveRight(self):
        self.position += 1
        if self.position == MAZE_SIZE:
            self.ateTheCheese = True
        if self.position == 1:
            self.fellInTheHole = True




if __name__ == '__main__':
    main()
