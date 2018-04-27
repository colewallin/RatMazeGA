# import random
#
# # A simple representation of a Rat
#
# MAZE_SIZE = 50
# # LIFE_SPAN = 30
#
#
# def randomGeneticSequnce():
#     dna = []
#     for i in range(LIFE_SPAN):
#         dna.append(random.randint(0, 1))
#     return dna
#
# # class DNA:
# #     def __init__(self):
# #         self.genes = []
# #         f or i in range(LIFE_SPAN):
# #             self.genes.append(random.randint(0, 1))
#
# class Rat:
#
#     def __init__(self, dna=None):
#         if dna == None:
#             self.dna = randomGeneticSequnce()
#         else:
#             self.dna = dna
#
#         self.position = MAZE_SIZE/2
#         self.fitness = 0.0
#         self.ateTheCheese = False
#
#     def update(self, age):
#         if self.position == MAZE_SIZE:
#             self.ateTheCheese = True
#
#         # Don't keep moving the rat if it has reached the cheese
#         if not self.ateTheCheese:
#             if self.dna[age]:
#                 self.moveRight()
#             else:
#                 self.moveLeft()
#
#     def display(self):
#         for val in range(1, MAZE_SIZE+1):
#             if val == self.position:
#                 print(' R ', end='')
#             elif val == 1:
#                 print(' O ', end='')
#             elif val == MAZE_SIZE:
#                 print(' C ', end='')
#             else:
#                 print(' = ', end='')
#         print()
#         self.printDNA()
#         print("Fitness Score of: ", self.fitness)
#
#     def calculateFitness(self):
#         distanceFromGoal = MAZE_SIZE - self.position
#
#
#         # If you got the cheese, double the top fitness (1/1)
#         if self.ateTheCheese:
#             self.fitness = 1/0.5
#         else:
#             self.fitness = 1/distanceFromGoal
#
#
#
#     def getDNA(self):
#         return self.dna
#
#     def printDNA(self):
#         for val in self.dna:
#             print(val, end="")
#         print()
#
#
#     def moveLeft(self):
#         self.position -= 1
#
#     def moveRight(self):
#         self.position += 1
