import numpy as np

def get_nb_poids(nb_capteur, format_reseau):

    ret = 0

    ret += nb_capteur * format_reseau[0]

    for i in range(0, len(format_reseau)-1):
        ret += format_reseau[i] * format_reseau[i+1]

    return ret

# A CHANGER
def get_score(valeur_capteur):

    return   valeur_capteur


def getEliteIndice(score, number_elite):

    return np.argpartition(score,-number_elite)[-number_elite:]


if __name__ == "__main__":

    # Entrees
    nb_capteur = 5
    nb_action = 3
    max_distance = 10
    nb_population = 50
    nb_elite = 20
    nb_generation = 50
    taux_mutation = 0.01
    max_valeur_mutation = 2                     #intervalle [ - max_valeur_mutation : max_valeur_mutation]
    format_reseau = [2, 3, nb_action]

    nb_poids = get_nb_poids(nb_capteur, format_reseau)

    print("nombre de poids :", nb_poids)

    # Generation de la population initiale
    population = np.random.rand(nb_population, nb_poids) * 10 - 5
    # population = np.random.randn(nb_population, nb_poids)
    # print(population)
    # print("population initiale :", population.shape)


    for i in range(0, nb_generation):


        # evaluation
        score = np.empty(shape=nb_population)
        for indice, individu in enumerate(population, 0):
            # score[indice] = get_score(individu)           # return score de la voiture
            score[indice] = get_score(indice)               # tmp pour test

        # print(score)

        # Selection des meilleurs
        eliteIndices = getEliteIndice(score, nb_elite)

        elites = np.empty(shape=(nb_elite, nb_poids) )
        i = 0
        for indice, individu in enumerate(population, 0):
            if indice in eliteIndices:
                elites[i] = individu
                i += 1

        # print("------------")
        # print(elites)

        # Croisement
        new_generation = np.empty( shape=(nb_population, nb_poids) )
        np.random.shuffle(elites)
        i, j = 0, 0
        counter_elites = 0

        while i < nb_population:
            for j in range(0, nb_poids):
                random_number = np.random.randint(0, high=2)
                if random_number == 0:
                    new_generation[i][j] = elites[counter_elites][j]
                else:
                    new_generation[i][j] = elites[counter_elites + 1][j]
            i += 1
            counter_elites += 1
            counter_elites = counter_elites % (nb_elite - 1)


        # Mutation
        for individu in new_generation:
            for gene in individu:
                if np.random.random_sample() < taux_mutation:
                    gene +=  np.random.random_sample() * (2 * max_valeur_mutation) - max_valeur_mutation

        population = new_generation
        print( population )


