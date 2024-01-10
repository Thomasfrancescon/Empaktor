def compte(tab): # permet de savoir combien de fois l'élément à été affiché dans la chaine de caractère
    tableau = []
    autre = []
    for i in tab: # prends chaque élément de tab
        if i in tableau: # si élément est dans le tableau
            index = tableau.index(i) + 1
            tableau[index] = tableau[index] + 1
        else:
            tableau.append(i)
            tableau.append(1)
    for i in range(0,len(tableau),2):
        autre.append((tableau[i+1],tableau[i]))
    return autre

def creerArbre(lettres):# permet de créer un arbre
    l = len(lettres)
    while l >= 2: # tant que la longueur de lettres est plus grand ou égal
        # on définie les deux premier noeuds
        petitnoeud = (0, lettres[0])
        grandnoeud = (1, lettres[1])
        for i in range(2, l):
            if lettres[i][0] <= petitnoeud[1][0]: # si élément est plus petit que le petitnoeud on dit que le petitnoeud devient le grandnoeud et que l'élément devient le petitnoeud
                grandnoeud = petitnoeud
                petitnoeud = (i, lettres[i])
            elif lettres[i][0] <= grandnoeud[1][0]:  # si élément est plus petit que le grandnoeud on dit que l'élément devient le grandnoeud
                grandnoeud = (i, lettres[i])
        nouveauNoeud = (
            petitnoeud[1][0] + grandnoeud[1][0],
            lettres[petitnoeud[0]],
            lettres[grandnoeud[0]]
        ) 
        lettres[petitnoeud[0]] = nouveauNoeud
        lettres.pop(grandnoeud[0])
        l -= 1
    return lettres[0]

def creerDico(arbre): # va permettre d'associer des bits avec un élément donc la création de la clé pour crypter et décrypter la chaine de caractère
    textarbre = [("", arbre)]
    dico = {}
    l = 1
    while l >= 1:
        bits, tuple = textarbre.pop(0)  
        l -= 1
        if len(tuple) == 2: # si la longuer du tuple est de 2 ( le premier contient le nombre d'apparition dans la chaine de caractère et le deuxième contient l'élément de la chaine de caractère ) alors on associe l'élément de la chaine de caractère au bits
            dico[tuple[1]] = bits
        elif len(tuple) == 3:  # si la longuer du tuple est de 3 alors la première partie du tuple va ajouter 0 au bits et la deuxième partie du tuple va ajouter 1 au bits
            textarbre.append((bits + "0", tuple[1]))
            textarbre.append((bits + "1", tuple[2]))
            l += 2
    return dico


def compress_data(data): # permet de crypter la chaine de caractère en bits
    lettres = compte(data)
    arbre = creerArbre(lettres)
    dico = creerDico(arbre)
    texteCompresse = ""
    for i in data: # pour chaque élément de data on ajoute la valeur en bits de l'élément dans une chaine de caractère
        texteCompresse += str(dico[i])
    return texteCompresse, dico

# Exemple 1
#data = "aabbbccdddd"
#compressed_data = compress_data(data)[0]
#print("Données compressées:", compressed_data)
