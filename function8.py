import random

def decrypt(crypt):
    decrypt=lambda crypt : "-".join([chr(int(elt)+65) for elt in crypt.split("-")])
    print(decrypt(crypt))
    
decrypt("0-11-14")
