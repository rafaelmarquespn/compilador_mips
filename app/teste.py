def ordem_alfabetica():
    with open('app\\archives\\exemplos_in.txt', 'r') as f :
        i = f.readlines()
        i = [m.strip() for m in i]
        lista = i.sort()
        pass
        with open('app\\archives\\exemplos_in.txt', 'w') as f :
            for n in i:
                f.write(n +'\n')


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


def match_case_automatico():
    lista = []
    with open('compilador_mips\\app\\archives\\exemplos_in.txt', 'r') as arq :
        i = arq.readlines()
        i = [m.strip() for m in i]
        for n in i:
            j = n.replace('.','_')
            instruções, registradores = n.split(' ', 1)
                # case 'add.d $f0, $f2':#
                # registers = i.split(' ')[1]
                # translator = Translator()
                # traduction = translator.add_d(registers)
                # translated.append(translator)
            lista.append("case " + f"'{n}'" + ":" + "\n" + f'\tregisters = i.split(' f')[1]\n\ttranslator = Translator()\n\ttraduction = translator.{j}({registradores})\n\ttranslated.append(traduction) ' + "\n")

    with open('compilador_mips\\app\\archives\\exemplos_match.txt', 'w') as arq :
        for n in lista:
            arq.write(n +'\n')

#match_case_automatico()

def metodos_automatico():
    with open('compilador_mips\\app\\archives\\exemplos_in.txt', 'r') as arq :
        i = arq.readlines()
        i = [m.strip() for m in i]
        lista = []
        for n in i:
            j = n.replace('.','_')
            lista.append(f'def {j}(self, registers:str):\n\tpass\n')    


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

instrucoes()