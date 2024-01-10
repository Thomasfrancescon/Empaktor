# empaktor

**Commandes à utiliser**
```
python3 empaktor.py nom_archive.tar.gz --compression nom_algorithme fichier1 fichier2 fichier3 ...
python3 empaktor.py --extract nom_algorithme nom_archive.tar.gz
```
**Exemple d'utilisation**
```
python3 empaktor.py monarchive.tar.gz --compress burrows_wheeler fichier.txt fichier1.txt fichier2.txt
python3 empaktor.py --extract bwt monarchive.tar.gz
```

**Description**
```
Ce programme est diviser en deux partie:
    -La première est la compression (--compress) et permet de selectionner des fichier et de les modifiers avec un "rle" un "burrows wheeler" ou un     "huffman". puis ils sont ajouté à une archive avec le nom choisi par l'utilisateur
    -La deuxième est la décompression (--extract) et permet de décompresser une archive en spécifiant l'algorithme pour la décompression. Il creer un dossier du même nom que l'archive sans le "tar.gz" avec les fichiers décompressé dedans
```

**Attention**
```
les fichiers que vous souhaiter compresser doivent être creer dans un dossier exemple
```

**Prototype**
```
Algorithme de compression:
    regarde si la compression est demandé
        regarde si des fichiers sont selectionnés
            creer une archive avec le nom que l'utilisateur a choisi
            sélectionne les fichier un par un pour les modifier
            selection de l'algorithme (bwt, huffman, rle)
            dans chaque algorithme un fichier est crée contenant la data du fichier modifié par un algorithme de compression puis est ajouté à l'archive avant d'être supprimé
            si aucun des trois algorithme est sélectionner message d'erreur
        si pas de fichier selectionné message d'errreur
    si compress pas utilisé message d'erreur

Algorithme de décompression:
    regarde si la décompression est demandé
        creer un dossier avec comme nom l'archive sans le tar.gz
        selection de l'algorithme pour la décompression (rle, bwt, huffman)
            inverse la transformation avec l'algorithme sélectionné
            creer un fichier dans le dossier qui a été creé et y insert la data originale
        si aucun des trois algorithme est sélectionner message d'erreur
    message d'erreur utiliser --extract
```