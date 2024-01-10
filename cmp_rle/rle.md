# Run-Length Encoding

## Codage

**Paramètres reçu** :
```
Data est de type str (chaine de caractère) va permettre de le coder 
 ```
**Retour** :
```
12W1B12W3B24W1B est une chaine de caractère
```
**Description** : 
```
Le codage de RLE est un algorithme de compression de données transformants une chaine de caractères en renvoyent le nombre de même lettres à la suite.
```
**Prototype** :
```
encode_rle(data str) :
    boucle de la longueur de data :
        compte le nombre d'élément d'affiler puis ajouter le nombre d'élément et l'élément dans une variable de text
    return text
```
**Exemple d'utilisation** :
```
from rle import encode_rle, decode_rle

# Exemple 1
data = "AAABBBCCD"
encoded_data = encode_rle(data)
decoded_data = decode_rle(encoded_data)
print("Exemple 1:")
print("Données d'origine:", data)
print("Données encodées:", encoded_data)
```

## Décodage
**Paramètres reçu** :
```
Encoded_data est de type str (chaine de caractère) va permettre de le décoder 
```
**Retour** :
```
WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB est une chaine de caractère
```
**Description** : 
```
Le codage de RLE est un algorithme de compression de données transformants le nombre de même lettres à la suite en renvoyent une chaine de caractères.
```
**Prototype** :
```
decode_rle(encoded_data str) :
    boucle de la longueur de encoded_data :
        multiplie le nombre qu'il y a devant l'élément par l'élément et l'ajoute dans une variable de text
    return text
```
**Exemple d'utilisation** :
```
from rle import encode_rle, decode_rle

# Exemple 1
data = "AAABBBCCD"
encoded_data = encode_rle(data)
decoded_data = decode_rle(encoded_data)
print("Exemple 1:")
print("Données d'origine:", data)
print("Données encodées:", encoded_data)
print("Données décodées:", decoded_data)
print()
```
