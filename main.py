# Troy Tural 404
# TP2: Jeu de devinette

import random

Quit = 'n'
while Quit == 'n':
    # cette lingne va faire en sorte que l`ordi va deviner un nombre au hasard de 0 à 1000
    x = random.randint (0, 1000)
    nb_essai = 0
    print ("Devinez le nombre entre 0 et 1000")
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
