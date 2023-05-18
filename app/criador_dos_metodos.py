


def ordem_alfabetica():
    with open('app\\archives\\exemplos_in.txt', 'r') as f :
        i = f.readlines()
        i = [m.strip() for m in i]
        lista = i.sort()
        pass
        with open('app\\archives\\exemplos_in.txt', 'w') as f :
            for n in i:
                f.write(n +'\n')

#ordem_alfabetica()

def separar_linha():
    lista = []
    with open('compilador_mips\\app\\archives\\exemplos_in.txt', 'r') as arq :
        i = arq.readlines()
        i = [m.strip() for m in i]
        for n in i:
            if '/' in n:
                instruções, registradores = n.split(' ', 1)
                instruções = instruções.split('/')
                for i in instruções:
                    lista.append(i + ' ' + registradores)
            else:
                lista.append(n)

    with open('compilador_mips\\app\\archives\\exemplos_in.txt', 'w') as arq :
        for n in lista:
            arq.write(n +'\n')

#separar_linha()

def match_case_automatico():
    lista = []
    with open('compilador_mips\\app\\archives\\entradas_validas.txt', 'r') as arq :
        i = arq.readlines()
        i = [m.strip() for m in i]
        for n in i:
            j = n.replace('.','_')
            instrucao, registradores = n.split(' ', 1)
            lista.append("case " + f"'{n}'" + ":" + f'\
                        \n\tregisters = i.split(" ", 1)[1]\
                        \n\ttranslator = Translator()' + 
                        f'\n\ttraduction = translator.{instrucao}("{registradores}")\
                        \n\ttranslated.append(traduction) ' + "\n")

    with open('compilador_mips\\app\\archives\\match.txt', 'w') as arq :
        for n in lista:
            arq.write(n +'\n')

#match_case_automatico()

def metodos_automatico():
    with open('compilador_mips\\app\\archives\\instrucoes.txt', 'r') as arq :
        i = arq.readlines()
        i = [m.strip() for m in i]
    with open('compilador_mips\\app\\archives\\inst_binario.txt', 'r') as arq :
        h = arq.readlines()
        h = [m.strip() for m in h]
        lista2 = []
        for p in h:
            bin = p.split(';')
            if len(bin) == 2:
                opcode = bin[1].replace('0b', '')
                lista2.append(opcode)
            if len(bin) == 3:
                opcode = bin[1].replace('0b', '')
                funct = bin[2].replace('0b', '')
                lista2.append((opcode, funct))
        lista = []
        for n in range(len(i)):
            j = i[n].replace('.','_')
            lista.append(f'def {j}(self, registers:str):\
                        \n\topcode = "{lista2[n][0] if len(lista2[n]) == 2 else lista2[n]}"\
                        \n\trs = ""\
                        \n\trt = ""\
                        \n\trd = ""\
                        \n\tshamt = ""\
                        \n\tfunct = "{lista2[n][1] if len(lista2[n]) == 2 else None}"\
                        \n\treturn hex(int((opcode + rs + rt + rd + shamt + func),2))\n')    

    with open('compilador_mips\\app\\archives\\metodos.txt', 'w') as arq :
        for n in lista:
            arq.write(n +'\n')

#metodos_automatico()

def instrucoes():
    with open('compilador_mips\\app\\archives\\entradas_validas.txt', 'r') as arq :
        i = arq.readlines()
        i = [m.strip() for m in i]
        lista = []
        for n in i:
            j = n.split(' ', 1)[0]
            lista.append(f'{j}')    
    with open('compilador_mips\\app\\archives\\instrucoes.txt', 'w') as arq :
        for n in lista:
            arq.write(n +'\n')

#instrucoes()


def separa_tipo():
    lista = []
    with open('compilador_mips\\app\\archives\\entradas_validas.txt', 'r', encoding='utf-8') as arq:
        for i in arq.readlines():
            i = i.strip()
            lista.append(i)
    for i in lista:
        instrucao, registradores = i.split(' ', 1)
        if len(registradores.split(',')) == 1:
            with open('compilador_mips\\app\\archives\\tipo_r.txt', 'a', encoding='utf-8') as arq:
                arq.write(i + '\n')
        elif len(registradores.split(',')) == 2:
            with open('compilador_mips\\app\\archives\\tipo_i.txt', 'a', encoding='utf-8') as arq:
                arq.write(i + '\n')
        elif len(registradores.split(',')) == 3:
            with open('compilador_mips\\app\\archives\\tipo_j.txt', 'a', encoding='utf-8') as arq:
                arq.write(i + '\n')


