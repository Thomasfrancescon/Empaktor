def decompresser(texteCompresse, dico):
    dicoinverse = {v: k for (k, v) in dico.items()}
    limite = max(len(k) for k in dicoinverse.keys())    
    fileExploration = [("", texteCompresse)]
    l = 1
    while l >= 1:
        fait, textcompresse = fileExploration.pop(0)
        l -= 1
        if textcompresse == "":
            return fait
        i = 0
        bits = ""
        for bit in textcompresse:
            bits += bit
            i += 1
            if i > limite:
                break
            elif bits in dicoinverse:
                fileExploration.append((fait + dicoinverse[bits], textcompresse[i:]))
                l += 1
    return ""

texteCompresse = 