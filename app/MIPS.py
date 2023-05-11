class Registers():
    def __init__(self) -> None:
        pass
        
    def zero(self, registers:str):
        return "00000"
    def at(self, registers:str):
        return "00001"
    def v0(self, registers:str):
        return "00010"
    def v1(self, registers:str):
        return "00011"
    def a0(self, registers:str):
        return "00100"
    def a1(self, registers:str):
        return "00101"
    def a2(self, registers:str):
        return "00110"
    def a3(self, registers:str):
        return "00111"
    def t0(self, registers:str):
        return "01000"
    def t1(self, registers:str):
        return "01001"
    def t2(self, registers:str):
        return "01010"
    def t3(self, registers:str):
        return "01011"
    def t4(self, registers:str):
        return "01100"
    def t5(self, registers:str):
        return "01101"
    def t6(self, registers:str):
        return "01110"
    def t7(self, registers:str):
        return "01111"
    def s0(self, registers:str):
        return "10000"
    def s1(self, registers:str):
        return "10001"
    def s2(self, registers:str):
        return "10010"
    def s3(self, registers:str):
        return "10011"
    def s4(self, registers:str):
        return "10100"
    def s5(self, registers:str):
        return "10101"
    def s6(self, registers:str):
        return "10110"
    def s7(self, registers:str):
        return "10111"
    def t8(self, registers:str):
        return "11000"
    def t9(self, registers:str):
        return "11001"
    def k0(self, registers:str):
        return "11010"
    def k1(self, registers:str):
        return "11011"
    def gp(self, registers:str):
        return "11100"
    def sp(self, registers:str):
        return "11101"
    def fp(self, registers:str):
        return "11110"
    def ra(self, registers:str):
        return "11111"
    

class Translator(Registers):
    def __init__(self) -> None:
        pass
    def add_d(self, registers:str):
        return 100100


def load_file(path:str) -> list:
    with open(path, 'r', encoding="utf-8") as arq:
        asm = arq.readlines()
    return asm

def split_data_text(asm:list)->list:
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

def translate_text(text:list)->list:
    translated = list()
    for i in text:
        match i:
            case 'add.d $f0, $f2':
                registers = i.split(' ')[1]
                translator = Translator()
                translator.add_d(registers)
                translated.append(translator)







asm = load_file("app\\archives\\example_saida.asm")
data, text = split_data_text(asm)
print(data)
print()
print(text)