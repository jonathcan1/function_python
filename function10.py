def initials(name):
    split=name.split(" ")
    split_f=[]
    initial=""
    for name in split:
        split_f+=name.split("-")
    for name in split_f:
        initial+=name[0]
        
    print(initial)

initials("Jean-Baptiste Jean")