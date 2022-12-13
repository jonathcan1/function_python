import random

def crypting(word) :
    crypt=lambda word :"-".join([str(ord(elt)-65) for elt in word.upper()])
    print(crypt(word))

crypting("ALO")