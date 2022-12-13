import random

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def function_3(qty) :
    random.shuffle(alphabet)
    code=alphabet[0:qty]
    print(''.join(code)) 
        
function_3(500)
    