def encode_rle(data): #  permet de crypter la chaine de caractère en hexadécimal
    text = ''
    l = 1
    for i in range(len(data)-1):
        if data[i] == data[i+1]: # si l'élément de data est le même que celui d'après alors ajouter 1 a la variable l
            l = l + 1
        if data[i] != data[i+1]: # si l'élément de data est différent que celui d'après alors ajouter la variable l et l'élément et remettre à 1 la variable l
            text = text + "{0}{1}".format(l,data[i])
            l = 1
        if i == len(data)-2: # si l'élément de data est égal a la longueur de data moins deux alors ajouter la variable l et l'élément de l'index d'après
            text = text + "{0}{1}".format(l,data[i+1])
    return text

def decode_rle(encoded_data): #  permet de décrypter l'hexadécimal en chaine de caractère
    text = ''
    number = 0
    exp = 0.1
    for i in range(0,len(encoded_data)):
        if encoded_data[i].isdigit() == True : # si l'élément d'encoded data est un nombre alors multiplie exp par 10 et ajouter l'élément au number fois exp
            exp = int(exp * 10)
            number = int(encoded_data[i]) + number * exp
        elif encoded_data[i].isdigit() == False : # si l'élément d'encoded data n'est pas un nombre alorson multiplie le nombre par l'élément puis l'ajouter au text et remettre number a 0 et exp a 0.1 
            mot = number * encoded_data[i]
            text = text + "{0}".format(mot)
            number = 0
            exp = 0.1
    return text


# data = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
# encoded_data = encode_rle(data)
# decoded_data = decode_rle(encoded_data)
# print("Exemple 1:")
# print("Données d'origine:", data)
# print("Données encodées:", encoded_data)
# print("Données décodées:", decoded_data)

