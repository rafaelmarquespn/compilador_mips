class translator():
    pass



def leitura_do_arquivo(path:str) -> list:
    with open(path, 'r', encoding="utf-8") as arq:
        asm = arq.readlines()
    return asm

def separar_data_text(asm:list)->list:
    data = list()
    text = list()
    data_area = None
    for i in asm:
        i = i.strip()
        if i == '.data':
            data_area = True

        elif i == '.text':
            data_area = False

        elif data_area:
            data.append(i) if i else None
        
        elif not data_area:
            text.append(i)

    return data, text

def traduzir_text(text:list)->list:
    lista = list()
    for i in text:
        match i:
            case 'add.d $f0, $f2':
                k = add.d()
                lista.append(k)







asm = leitura_do_arquivo("app\\archives\\example_saida.asm")
data, text = separar_data_text(asm)
print(data)
print()
print(text)