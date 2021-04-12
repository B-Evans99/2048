from board import *
from pygad import gann
from random import choice
import numpy
import pygad


def variation_bonus(solution, solution_idx):
    global gann_instance
    control = Control()
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    lastMaxTileLocale = 0
    success = True
    fitness = 0
    while(not control.isGameOver()):
        boardState = control.getInputs()

        # reward if the biggest tile has moved
        maxTile = boardState[0]
        maxTileLocale = lastMaxTileLocale
        for (i, c) in enumerate(boardState):
            if(c > maxTile):
                maxTile = c
                maxTileLocale = i
        if(maxTileLocale != lastMaxTileLocale):
            fitness += 16
        lastMaxTileLocale = maxTileLocale

        if(success):
            data_inputs = numpy.array([boardState])
            prediction = pygad.nn.predict(last_layer=gann_instance.population_networks[solution_idx],
                                          data_inputs=data_inputs,
                                          problem_type="classification")
            success = control.move(directions[prediction[0]])
        else:
            success = control.move(choice(directions))

    fitness += control.getScore()

    return fitness


def callback_generation(ga_instance):
    global gann_instance

    population_matrices = pygad.gann.population_as_matrices(
        population_networks=gann_instance.population_networks, population_vectors=ga_instance.population)
    gann_instance.update_population_trained_weights(
        population_trained_weights=population_matrices)

    print("Generation = {generation}".format(
        generation=ga_instance.generations_completed))
    print("Fitness    = \t\t{fitness}".format(
        fitness=ga_instance.best_solution()[1]))


gann_instance = pygad.gann.GANN(
    num_solutions=50,
    num_neurons_input=16,
    num_neurons_output=4,
    num_neurons_hidden_layers=[12, 8],
    output_activation="softmax"
)
gann_instance.create_population()

population_vectors = pygad.gann.population_as_vectors(
    population_networks=gann_instance.population_networks)


initial_population = population_vectors.copy()

num_parents_mating = 25
num_generations = 10
mutation_percent_genes = 8
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
keep_parents = 10
init_range_low = -2
init_range_high = 5

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       initial_population=initial_population,
                       fitness_func=variation_bonus,
                       mutation_percent_genes=mutation_percent_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       keep_parents=keep_parents,
                       on_generation=callback_generation)

ga_instance.run()
ga_instance.save('variation')
ga_instance.plot_result()
