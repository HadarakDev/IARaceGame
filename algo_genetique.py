import numpy as np
import sys
from utils import *
from predict import *


def get_nb_poids(nb_capteur, format_reseau):

    ret = 0

    ret += nb_capteur * format_reseau[0]

    for i in range(0, len(format_reseau)-1):
        ret += format_reseau[i] * format_reseau[i+1]

    return ret


def get_score(individu, format_reseau, nb_poids):

    poids_reseau = individu.tolist()


    while True:
        # Get sensors information
        next_input_must_be("START turn")
        string_sensors = input()
        other_information = input()
        next_input_must_be("STOP turn")

        sensors = getSensorsFromString(string_sensors)
        isCrash, score = parse_other_information(other_information)
        print(isCrash, score, file=sys.stderr)

        # Send decision
        print("START action")
        if isCrash:
            print("RESTART")
            print("RESTART", file=sys.stderr)
            print("STOP action")
            return score
        else:
            result = take_decision(format_reseau, poids_reseau, sensors)
            print(result)
            print("ici", result, file=sys.stderr)
            print("STOP action")


def print_params_dispacher():
    next_input_must_be("START player")
    player = int(input())
    next_input_must_be("STOP player")

    next_input_must_be("START settings")
    line = input()
    while line != "STOP settings":
        line = input()


def getEliteIndice(score, number_elite):

    return np.argpartition(score,-number_elite)[-number_elite:]


if __name__ == "__main__":

    # Entrees
    nb_capteur = 5
    nb_population = 20
    nb_elite = 5
    nb_generation = 500
    taux_mutation = 0.3
    max_valeur_mutation = 0.1                     # intervalle [ - max_valeur_mutation : max_valeur_mutation]
    max_valeur_initialisation = 1                # intervalle [ - max_valeur_mutation : max_valeur_mutation]
    format_reseau = [5, 10, 5, 3]
    nb_poids = 137


    # Passer intro du jeu
    print_params_dispacher()
    with open("result.txt", "w") as file:
        file.write("")


    # Generation de la population initiale
    population = np.random.rand(nb_population, nb_poids) * max_valeur_mutation - max_valeur_mutation



    for i in range(0, nb_generation):

        print("Nombre epoch :", i + 1, file=sys.stderr)


        # evaluation
        score = np.empty(shape=nb_population)
        for indice, individu in enumerate(population, 0):
            print("epoch : %s, individu n°%s" % (i + 1, indice), file=sys.stderr)


            score[indice] = get_score(individu, format_reseau, nb_poids)           # return score de la voiture

        # Selection des meilleurs
        eliteIndices = getEliteIndice(score, nb_elite)

        elites = np.empty(shape=(nb_elite, nb_poids))
        h = 0
        for indice, individu in enumerate(population, 0):
            if indice in eliteIndices:
                elites[h] = individu
                h += 1

        # Croisement
        new_generation = np.empty(shape=(nb_population, nb_poids))
        np.random.shuffle(elites)
        h, j = 0, 0
        counter_elites = 0

        while h < nb_population:
            for j in range(0, nb_poids):
                random_number = np.random.randint(0, high=2)
                if random_number == 0:
                    new_generation[h][j] = elites[counter_elites][j]
                else:
                    new_generation[h][j] = elites[counter_elites + 1][j]
            h += 1
            counter_elites += 1
            counter_elites = counter_elites % (nb_elite - 1)

         #save
        with open("result.txt", "a") as file:
            file.write("\n\nGENERATION : %s \n" % i)
            for individu, sonScore in zip(population, score):
                for poids in individu:
                    file.write("%s;" % poids)
                file.write("\nscore : %s\n\n" % sonScore)


        # Mutation
        for individu in new_generation:
            for gene in individu:
                if np.random.random_sample() < taux_mutation:
                    gene += np.random.random_sample() * (2 * max_valeur_mutation) - max_valeur_mutation

        population = new_generation






