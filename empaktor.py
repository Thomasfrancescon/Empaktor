import sys
import tarfile
import os
from burrows_wheeler import transform_bwt, inverse_bwt
from rle import encode_rle, decode_rle
from huffman import compress_data


def decompresser(texteCompresse, dico):
    dicoinverse = {v: k for (k, v) in dico.items()}     # Crée un dictionnaire inverse
    limite = max(len(k) for k in dicoinverse.keys())    # longueur maximal des clef du dictionnaire
    rendu = [("", texteCompresse)]                      # liste pour stocker les information
    l = 1
    while l >= 1:               # explore et décompresse le texte
        fait, textcompresse = rendu.pop(0)
        l -= 1
        if textcompresse == "":     # continu tant qu'il y a des informations dans texteCompresse
            return fait
        i = 0
        bits = ""
        for bit in textcompresse:   # si on a atteint la limite de la taille des bits à vérifier, arrête la boucle
            bits += bit
            i += 1
            if i > limite:  # si on a atteint la limite de la taille des bits à vérifier, arrête la boucle
                break
            elif bits in dicoinverse:   # si le bit est présent dans le dictionnaire alors on regarde à qu'elle lettre il correspond et on l'ajoute
                rendu.append((fait + dicoinverse[bits], textcompresse[i:]))
                l += 1
    return ""


if sys.argv[2] == "--compress":     # for the compression
    if len(sys.argv) > 4:
        with tarfile.open(sys.argv[1], "w:gz") as tar:  # create the archive with the name in the commande
            for i in range(4, len(sys.argv)):
                file_path = (f"./exemple/{sys.argv[i]}")        # select the files to compress
                with open(file_path, "r") as file:              # read the file read the files to compress
                    data = file.read()
                    if sys.argv[3] == "burrows_wheeler":        # select the algorithm to modify the files
                        transformed_data = transform_bwt(data)
                        with open(sys.argv[i], "w") as filename:       # create a temporary file to stock the transformed data
                            filename.write(str(transformed_data[1]))
                            filename.write(transformed_data[0])
                        tar.add(sys.argv[i], arcname=os.path.basename(sys.argv[i]))     # add the data to the archive
                        os.remove(sys.argv[i])      # remove the temporary file
                    elif sys.argv[3] == "rle":
                        transformed_data = encode_rle(data)
                        with open(sys.argv[i], "w") as filename:    # read the file transform the data create a temporary file and add to the archive remove the temporary file
                            filename.write(transformed_data)
                        tar.add(sys.argv[i], arcname=os.path.basename(sys.argv[i]))
                        os.remove(sys.argv[i])
                    elif sys.argv[3] == "huffman":
                        texteCompresse = compress_data(data)
                        with open(sys.argv[i], "w") as filename:    # read the file transform the data create a temporary file and add to the archive remove the temporary file
                            filename.write(str(texteCompresse))
                        tar.add(sys.argv[i], arcname=os.path.basename(sys.argv[i]))
                        os.remove(sys.argv[i])
                    elif sys.argv[3] != "burrows_wheeler" or sys.argv[3] != "rle" or sys.argv[3] != "huffman":
                        print("use rle, burrows_wheeler or huffman")
                        break
    else:
        print("no file selected")
elif sys.argv[1] == "--extract":
    pass
else:
    print("use --compress")


if sys.argv[1] == "--extract":
    rm = ".tar.gz"      
    result = sys.argv[3].replace(rm, "")    
    os.mkdir(result)                                # create a folder with the name of the archive without the "tar.gz"
    file_to_extract = tarfile.open(sys.argv[3])
    file_to_extract.extractall(f"./{result}")
    file_to_extract.close                           # extract all files into the created folder
    entries = os.listdir(result)
    if sys.argv[2] == "burrows_wheeler":
        for i in range(len(entries)):
            file_to_change = entries[i]
            file2 = open(f"{result}/{entries[i]}", "r")
            content = file2.read()                          # read the file and put the data into a variable
            file2.close
            transformed_data = ""
            key = ""
            for i in range(len(content)):
                if content[i].isdigit() and i == 0:            # separe the key and the data
                    key = key + content[i]
                elif content[i].isdigit():
                    key = key + content[i]
                else:
                    transformed_data = transformed_data + content[i]
            original_data = inverse_bwt(transformed_data, int(key))
            file3 = open(f"{result}/{file_to_change}", "w")         # modify the extracted files to put the original data
            file3.write(original_data)
    elif sys.argv[2] == "rle":
        for i in range(len(entries)):
            file2 = open(f"{result}/{entries[i]}", "r")
            content = file2.read()
            original_data = decode_rle(content)
            file3 = open(f"{result}/{entries[i]}", "w")
            file3.write(original_data)
    elif sys.argv[2] == "huffman":
        for i in range(len(entries)):
            file2 = open(f"{result}/{entries[i]}", "r") # read the data in the file
            content = file2.read()
            pos1 = content.find("{")    # to recover the dico
            pos2 = content.find("}")
            pos2=pos2 + len("}")
            dico = (content[pos1:pos2])
            dicoRetourne = eval(dico)
            pos3 = content.find("'")
            pos4 = content.find(",")
            pos4 = pos4 + len(",")      
            ata = (content[pos3:pos4])
            rm = "'"
            ata2 = ata.replace(rm, "")
            rm2 = ","
            texteCompresse = ata2.replace(rm2, "")  # separate the dictionary and the binary code
            original_data = decompresser(texteCompresse, dicoRetourne)  # find the original data
            file3 = open(f"{result}/{entries[i]}", "w")
            file3.write(str(original_data))     # write the original data into the file
    elif sys.argv[2] != "bwt" or sys.argv[2] != "rle" or sys.argv[2] != "huffman":
        print("use rle or bwt or huffman")
elif sys.argv[2] == "--compress":
    pass
else:
    print("or use --extract")
