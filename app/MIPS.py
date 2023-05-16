class Registers():
    def __init__(self) -> None:
        pass
        
    def zero(self):
        return "00000"
    def at(self):
        return "00001"
    def v0(self):
        return "00010"
    def v1(self):
        return "00011"
    def a0(self):
        return "00100"
    def a1(self):
        return "00101"
    def a2(self):
        return "00110"
    def a3(self):
        return "00111"
    def t0(self):
        return "01000"
    def t1(self):
        return "01001"
    def t2(self):
        return "01010"
    def t3(self):
        return "01011"
    def t4(self):
        return "01100"
    def t5(self):
        return "01101"
    def t6(self):
        return "01110"
    def t7(self):
        return "01111"
    def s0(self):
        return "10000"
    def s1(self):
        return "10001"
    def s2(self):
        return "10010"
    def s3(self):
        return "10011"
    def s4(self):
        return "10100"
    def s5(self):
        return "10101"
    def s6(self):
        return "10110"
    def s7(self):
        return "10111"
    def t8(self):
        return "11000"
    def t9(self):
        return "11001"
    def k0(self):
        return "11010"
    def k1(self):
        return "11011"
    def gp(self):
        return "11100"
    def sp(self):
        return "11101"
    def fp(self):
        return "11110"
    def ra(self):
        return "11111"
    

class Translator(Registers):
    def __init__(self) -> None:
        pass
    def separar_registradores(self, registers:str) -> list:
        registers = registers.split(', ')
        return registers

    def add_d(self, registers:str):                        
        opcode = "010001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "000001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def add_s(self, registers:str):                        
        opcode = "010001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "000000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def add(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "100000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sub(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "100010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def _and(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "100100"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def _or(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "100101"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def nor(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "100111"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def xor(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "100110"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def addi(self, registers:str):                        
        opcode = "001000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def andi(self, registers:str):                        
        opcode = "001100"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def ori(self, registers:str):                        
        opcode = "001101"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def xori(self, registers:str):                        
        opcode = "001110"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def addiu(self, registers:str):                        
        opcode = "001001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def addu(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "100001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def subu(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "100011"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def beq(self, registers:str):                        
        opcode = "000100"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def bne(self, registers:str):                        
        opcode = "000101"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def bgez(self, registers:str):                        
        opcode = "000001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "000001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def bgezal(self, registers:str):                        
        opcode = "000001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "100001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def c_eq_d(self, registers:str):                        
        opcode = "010001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "101001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def c_eq_s(self, registers:str):                        
        opcode = "010001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "101000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def clo(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "100001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def div(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "011010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def div_d(self, registers:str):                        
        opcode = "010001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "111001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def div_s(self, registers:str):                        
        opcode = "010001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "111000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def j(self, registers:str):                        
        opcode = "000010"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def jal(self, registers:str):                        
        opcode = "000011"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def jalr(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "001001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def jr(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "001000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def lb(self, registers:str):                        
        opcode = "100000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def lh(self, registers:str):                        
        opcode = "100001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def lhu(self, registers:str):                        
        opcode = "100101"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def li(self, registers:str):                        
        opcode = "001111"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def lui(self, registers:str):                        
        opcode = "001111"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def lw(self, registers:str):                        
        opcode = "100011"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def madd(self, registers:str):                        
        opcode = "011100"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def mfhi(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "010000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def mflo(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "010010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def movn(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "001011"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def msubu(self, registers:str):                        
        opcode = "011101"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def mul(self, registers:str):                        
        opcode = "011100"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def mul_d(self, registers:str):                        
        opcode = "010001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "010010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def mul_s(self, registers:str):                        
        opcode = "010001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "010000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def mult(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "011000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sb(self, registers:str):                        
        opcode = "101000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sll(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "000000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def srl(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "000010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def slt(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "101010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def slti(self, registers:str):                        
        opcode = "001010"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sltu(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "101011"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sra(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "000011"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def srav(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "000111"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sub_d(self, registers:str):                        
        opcode = "010001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "000011"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sub_s(self, registers:str):                        
        opcode = "010001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "000010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sw(self, registers:str):                        
        opcode = "101011"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def teq(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "110100"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def tge(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "110000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def tgei(self, registers:str):                        
        opcode = "000001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "010000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def u(self, registers:str):                        
        opcode = "000000"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "110001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def tne(self, registers:str):                        
        opcode = "00001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "01000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def tnei(self, registers:str):                        
        opcode = "000001"                        
        rs = ""                        
        rt = ""                        
        rd = ""                        
        shamt = ""                        
        funct = "01001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))


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
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.add.d("$f0, $f2")                         
                translated.append(traduction) 

            case 'add.s $f1, $f2':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.add.s("$f1, $f2")                         
                translated.append(traduction) 

            case 'add $t0, $s2, $t0':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.add("$t0, $s2, $t0")                         
                translated.append(traduction) 

            case 'sub $t0, $s2, $t0':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.sub("$t0, $s2, $t0")                         
                translated.append(traduction) 

            case 'and $t0, $s2, $t0':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator._and("$t0, $s2, $t0")                         
                translated.append(traduction) 

            case 'or $t0, $s2, $t0':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator._or("$t0, $s2, $t0")                         
                translated.append(traduction) 

            case 'nor $t0, $s2, $t0':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.nor("$t0, $s2, $t0")                         
                translated.append(traduction) 

            case 'xor $t0, $s2, $t0':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.xor("$t0, $s2, $t0")                         
                translated.append(traduction) 

            case 'addi $t2, $t3, -10':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.addi("$t2, $t3, -10")                         
                translated.append(traduction) 

            case 'andi $t2, $t3, -10':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.andi("$t2, $t3, -10")                         
                translated.append(traduction) 

            case 'ori $t2, $t3, -10':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.ori("$t2, $t3, -10")                         
                translated.append(traduction) 

            case 'xori $t2, $t3, -10':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.xori("$t2, $t3, -10")                         
                translated.append(traduction) 

            case 'addiu $t1, $t2, $t3':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.addiu("$t1, $t2, $t3")                         
                translated.append(traduction) 

            case 'addu $t1, $t2, $t3':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.addu("$t1, $t2, $t3")                         
                translated.append(traduction) 

            case 'subu $t1, $t2, $t3':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.subu("$t1, $t2, $t3")                         
                translated.append(traduction) 

            case 'beq $t1, $zero, LABEL':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.beq("$t1, $zero, LABEL")                         
                translated.append(traduction) 

            case 'bne $t1, $zero, LABEL':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.bne("$t1, $zero, LABEL")                         
                translated.append(traduction) 

            case 'bgez $t1, LABEL':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.bgez("$t1, LABEL")                         
                translated.append(traduction) 

            case 'bgezal $t1, LABEL':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.bgezal("$t1, LABEL")                         
                translated.append(traduction) 

            case 'c.eq.d $f2, $f4':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.c.eq.d("$f2, $f4")                         
                translated.append(traduction) 

            case 'c.eq.s $f0, $f1':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.c.eq.s("$f0, $f1")                         
                translated.append(traduction) 

            case 'clo $t1, $t2':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.clo("$t1, $t2")                         
                translated.append(traduction) 

            case 'div $t1, $t2':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.div("$t1, $t2")                         
                translated.append(traduction) 

            case 'div.d $f2, $f4, $f6':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.div.d("$f2, $f4, $f6")                         
                translated.append(traduction) 

            case 'div.s $f0, $f1, $f2':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.div.s("$f0, $f1, $f2")                         
                translated.append(traduction) 

            case 'j LABEL':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.j("LABEL")                         
                translated.append(traduction) 

            case 'jal LABEL':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.jal("LABEL")                         
                translated.append(traduction) 

            case 'jalr $t1':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.jalr("$t1")                         
                translated.append(traduction) 

            case 'jr $t0':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.jr("$t0")                         
                translated.append(traduction) 

            case 'lb $t1, 100($t2)':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.lb("$t1, 100($t2)")                         
                translated.append(traduction) 

            case 'lh $t1, -100($t2)':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.lh("$t1, -100($t2)")                         
                translated.append(traduction) 

            case 'lhu $t1, -100($t2)':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.lhu("$t1, -100($t2)")                         
                translated.append(traduction) 

            case 'li $t1, XX (incluindo na forma de pseudoinstrução)':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.li("$t1, XX (incluindo na forma de pseudoinstrução)")                         
                translated.append(traduction) 

            case 'lui $t1, 0xXXXX':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.lui("$t1, 0xXXXX")                         
                translated.append(traduction) 

            case 'lw $t0, OFFSET($s3)':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.lw("$t0, OFFSET($s3)")                         
                translated.append(traduction) 

            case 'madd $t1, $t2':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.madd("$t1, $t2")                         
                translated.append(traduction) 

            case 'mfhi $t1':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.mfhi("$t1")                         
                translated.append(traduction) 

            case 'mflo $t1':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.mflo("$t1")                         
                translated.append(traduction) 

            case 'movn $t1, $t2, $t3':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.movn("$t1, $t2, $t3")                         
                translated.append(traduction) 

            case 'msubu $t1, $t2':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.msubu("$t1, $t2")                         
                translated.append(traduction) 

            case 'mul $t1, $t2, $t5':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.mul("$t1, $t2, $t5")                         
                translated.append(traduction) 

            case 'mul.d $f2, $f4, $f6':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.mul.d("$f2, $f4, $f6")                         
                translated.append(traduction) 

            case 'mul.s $f1, $f2, $f3':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.mul.s("$f1, $f2, $f3")                         
                translated.append(traduction) 

            case 'mult $t1, $t2':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.mult("$t1, $t2")                         
                translated.append(traduction) 

            case 'sb $t4, 1000($t2)':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.sb("$t4, 1000($t2)")                         
                translated.append(traduction) 

            case 'sll $t2, $t3, 10':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.sll("$t2, $t3, 10")                         
                translated.append(traduction) 

            case 'srl $t2, $t3, 10':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.srl("$t2, $t3, 10")                         
                translated.append(traduction) 

            case 'slt $t1, $t2, $t3':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.slt("$t1, $t2, $t3")                         
                translated.append(traduction) 

            case 'slti $t1, $t2, -100':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.slti("$t1, $t2, -100")                         
                translated.append(traduction) 

            case 'sltu $t1, $t2, -100':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.sltu("$t1, $t2, -100")                         
                translated.append(traduction) 

            case 'sra $t2, $t1, 10':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.sra("$t2, $t1, 10")                         
                translated.append(traduction) 

            case 'srav $t1, $t2, $t3':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.srav("$t1, $t2, $t3")                         
                translated.append(traduction) 

            case 'sub.d $f2, $f4, $f6':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.sub.d("$f2, $f4, $f6")                         
                translated.append(traduction) 

            case 'sub.s $f0, $f1, $f3':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.sub.s("$f0, $f1, $f3")                         
                translated.append(traduction) 

            case 'sw $t0, OFFSET($s3)':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.sw("$t0, OFFSET($s3)")                         
                translated.append(traduction) 

            case 'teq $t1, $t2':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.teq("$t1, $t2")                         
                translated.append(traduction) 

            case 'tge $t1, $t2':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.tge("$t1, $t2")                         
                translated.append(traduction) 

            case 'tgei $t1, -100':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.tgei("$t1, -100")                         
                translated.append(traduction) 

            case 'u $t1, -100':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.u("$t1, -100")                         
                translated.append(traduction) 

            case 'tne $t1, $t2':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.tne("$t1, $t2")                         
                translated.append(traduction) 

            case 'tnei $t1, -100':                         
                registers = i.split(" ", 1)[1]                         
                translator = Translator()
                traduction = translator.tnei("$t1, -100")                         
                translated.append(traduction) 



#asm = load_file("app\\archives\\example_saida.asm")
#data, text = split_data_text(asm)
# print(data)
# print()
# print(text)
registrador = Registers()
print(registrador.zero())
var = 'zero'
var2 = f'registrador.{var}()'
print(exec(f"var3 = {var2}"))
# print(var3)