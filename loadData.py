from board import *
from pygad import gann
from random import choice
import numpy
import csv
import pygad

# the load function fails if it cannot find it's fitness or callback function, so empty functions are included here


def variation_bonus(solution, solution_idx):
    return None


def fitness_function(solution, solution_idx):
    return None


def callback_generation(ga_instance):
    return None


loaded_ga_instance = pygad.load(filename='control')
graph = loaded_ga_instance.best_solutions_fitness
with open('control.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in list(graph):
        writer.writerow([i])
