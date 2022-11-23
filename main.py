# Troy Tural 404
# TP2: Jeu de devinette
import random

Quit = 'n'
min = 0
max = 100

#Lorsqu'on va commercer le jeu, l'ordi va nous demander si on veut choisir une valeur minimale et maximale
def choix_bornes():
    global min
    global max
    min = int(input('borne maximale'))
    max = int(input('borne minimale'))

#si on ne decide pas de choisir des bornes, l`ordi va prendre un nombrre aleatiore de 0 à 100 à nous faire deviner
while Quit == 'n':
    # cette lingne va faire en sorte que l`ordi va deviner un nombre au hasard de 0 à 1000
    x = random.randint (0, 1000)
    choix = input('Voulez-vous choisir des valeurs?')
    if choix == 'non':
        min = 0
        max = 100
    else:
        choix_bornes()


    # cette ligne va faire en sorte que l`ordi va deviner un nombre au hasard entre les deux nombres choisis
    x = random.randint (min, max)
    nb_essai = 0
    print ("Devinez le nombre entre 0 et 1000")
    print ("Devinez le nombre entre 'min' et 'max")
    # Le str(1001) va assuer que le nombre choisi par l`ordi ne va pas depasser 1000
    essai = str (1001)
    while int (essai) != x:
        essai = input ("Entrez votre essai")
        # Chaque fois qu`on ne devine pas le bon nombre, le code va prendre en note le nombre d`essais deviner jusqu`au moment qu`on devine le nombre mystère
        nb_essai += 1
        # Si le nombre qu`on a deviner est plus petit que le nombre mystère, l`écran affichera que notre nombre est plus petit que celui a deviner
        if int (essai) > x:
            print (essai, '>', "Le nombre choisi!")
            ##Si le nombre qu`on a deviner est plus grand que le nombre mystère, l`écran affichera que notre nombre est plus grand que celui a deviner
        if int (essai) < x:
            print (essai, '<', "Le nombre choisi")
    # cette ligne va apparaite quand on devine le nombre mystère en nous indiquant le nombre d`essais que ca a pris pour le trouver
    print ("Bravo! Tu a trouvé le nombre dans", nb_essai, "essais!")
    # Apres qu`on trove le nombre mystère, le console va nous demander si on veu qitter le jeu. Si on clique n, le jeu va reccomencer. Si on clique y, le jeu(code) va se terminer
    Quit = input ("Voulez-vous quitter? y/n")
# cette phrase va appaitre lorsqu`on decide de quitter le jeu
print ("Merci d`avoir jouer!")
