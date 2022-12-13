import random

alpha_num=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

def function_3(qty) :
    random.shuffle(alpha_num)
    code=alpha_num[0:qty]
    print(''.join(code)) 
        
value=int(input("Enter a number to generate a code. Max : 36 \n"))
function_3(value)
    