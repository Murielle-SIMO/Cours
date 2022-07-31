import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4

def demander_nombre(nb_min, nb_max):
    #nombre = input("Quel est le nombre magique (entre1 et 10)5")
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max}) ?")
        try:
            nombre_int = int(nombre_str)

           # if not nombre_int == int:
            #    return print("Entre un entier")
        except Exception as error:
            print("ERREUR: Entrer un entier. Réessayez.")

        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Nombre compris entre {nb_min} et {nb_max}. Réessayez")
                nombre_int = 0

    return nombre_int


def trouver_nombre_magique(nb_min, nb_max):

    vies = NB_VIES
    gagne = False
    for i in range(0, NB_VIES):
        vies = NB_VIES - i
        print(f"vous avez {vies} vies")
        nombre = demander_nombre(nb_min, nb_max)

        if nombre > NOMBRE_MAGIQUE:
            print("Le nombre magique est plus petit")

        elif nombre < NOMBRE_MAGIQUE :
            print("le nombre magique est plus grand")

        else:
            print("Bravo, vous avez gagné")
            gagne = True
            break

    if not gagne:
        print(f"vous avez perdu! Le nombre magique était : {NOMBRE_MAGIQUE}.")









#nb_magique = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
nombre_magique = trouver_nombre_magique(NOMBRE_MIN, NOMBRE_MAX)