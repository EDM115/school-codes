ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for ... in message :
        if lettre in ALPHABET :
            indice = ( ... )%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = ...
    return resultat
