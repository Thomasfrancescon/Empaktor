# Huffman

**Paramètres reçu** :
```
Data est de type str (chaine de caractère) va permettre de le coder
```
**Retour** :
```
1111000000101001010101 est une chaine de caractère
```
**Description** : 
```
Le codage de Huffman est un algorithme de compression de données transformants une chaine de caractères en binaires.
```
**Prototype** :
```
compress_data(data) :
    boucle pour chaque élément de data :
        ajoute chaque élément de data dans une variable de texteCompresse
    return texteCompresse, dico
```
**Exemple d'utilisation** : 
```
from huffman import compress_data

# Exemple 1
data = "aabbbccdddd"
compressed_data = compress_data(data)
print("Données compressées:", compressed_data)
```
