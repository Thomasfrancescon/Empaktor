# Burrows wheeler

**Paramètres reçu** :
```

Data est de type str (chaine de caractère) va permettre de le coder
```
**Retour** :
```

le programme retourne la data modifier et la clef pour retrouver la data original (clef:3, data_modifiée:nnbaaa)
```

**Description** :
```
Le codage de burrows est un algorithme qui permet de réorganiser les lettres pour que les algorithme de compression puissent avoir un meilleur taux de compression
```
**Prototype**
```
Burrows wheeler:
    transform_bwt:
    faire toutes les rotations pour la data
        trouver la clef et la data modifier
        return la clef et la data modifiée
    inverse_bwt:
    sépare les lettres de la data en la mettant dans un tableau
    fait toute les rotations possible en insérant les rotations dans un tableau
    retrouve la data grâce à la clef
    return la data original
```

**Exemple d'utilisation** : 
```
from burrows_wheeler import transform_bwt, inverse_bwt

data = "banana"
transformed_data, key = transform_bwt(data)
original_data = inverse_bwt(transformed_data, key)
print("Example 1:")
print("Original Data:", data)
print("key", key)
print("Burrows-Wheeler Transform:", transformed_data)
print("Inverted Data:", original_data)

la clef sera 3 et la data modifiée sera nnbaaa
```
