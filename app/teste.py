with open('app\\archives\\exemplos_in.txt', 'r') as f :
    i = f.readlines()
    i = [m.strip() for m in i]
    lista = i.sort()
    pass
    with open('app\\archives\\exemplos_in.txt', 'w') as f :
        for n in i:
            f.write(n +'\n')
        

