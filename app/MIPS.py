class FloatRegisters:
    def __init__(self) -> None:
        pass
    def f0(self):
        return "00000"
    def f1(self):        
        return "00001"
    def f2(self):
        return "00010"
    def f3(self):
        return "00011"
    def f4(self):
        return "00100"
    def f5(self):
        return "00101"
    def f6(self):
        return "00110"
    def f7(self):
        return "00111"
    def f8(self):
        return "01000"
    def f9(self):
        return "01001"
    def f10(self):
        return "01010"
    def f11(self):
        return "01011"
    def f12(self):
        return "01100"
    def f13(self):
        return "01101"
    def f14(self):
        return "01110"
    def f15(self):
        return "01111"
    def f16(self):
        return "10000"
    def f17(self):
        return "10001"
    def f18(self):
        return "10010"
    def f19(self):
        return "10011"
    def f20(self):
        return "10100"
    def f21(self):
        return "10101"
    def f22(self):
        return "10110"
    def f23(self):
        return "10111"
    def f24(self):
        return "11000"
    def f25(self):
        return "11001"
    def f26(self):
        return "11010"
    def f27(self):
        return "11011"
    def f28(self):
        return "11100"
    def f29(self):
        return "11101"
    def f30(self):
        return "11110" 
    def f31(self):
        return "11111"
    

class Registers(FloatRegisters):

    def __init__(self) -> None:
        pass

    def imm(self, imediato:float):
        if '-' in imediato:
            im_positivo =  bin(int(imediato))[2:].zfill(16)
            im_negativo = int(1111111111111111) - int(im_positivo)
            return str(im_negativo)
        else:
            return bin(int(imediato))[2:].zfill(16)

    def zero(self, registers:str):
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
    def __init__(self, text, instrução, registradores) -> None:
        self.text = text
        self.instrução = instrução
        self.registradores = registradores.replace('$', '')


    def labels(self, label):
        for i in self.text:
            i = i.replace(':', '')
            if label == i:
                return bin((int(self.text.index(f'{i}:')) + 1) * 4)[2:].zfill(16)
            
    def offset(self, endereço):
        offset, registrador = endereço.split('(').replace(')', '')
        offset = self.imm(offset)
        registrador = ''
        exec(f'registrador = self.{registrador}()')
        return offset, registrador
#TODO: Implementar as instruções
    def add_d(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}")                        
        shamt = ""                        
        funct = "000001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))
#TODO: Implementar as instruções
    def add_s(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "000000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def add(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "100000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sub(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "100010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def _and(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "100100"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def _or(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "100101"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def nor(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "100111"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def xor(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "100110"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def addi(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "001000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        imm = ""                        
        exec(f"imm = self.imm({registrador[2]})")                                                
        return hex(int((opcode + rs + rt + imm ),2))

    def andi(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "001100"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        imm = ""                        
        exec(f"imm = self.imm({registrador[2]})")                                                
        return hex(int((opcode + rs + rt + imm ),2))
    
    def ori(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "001101"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        imm = ""                        
        exec(f"imm = self.imm({registrador[2]})")                                                
        return hex(int((opcode + rs + rt + imm ),2))
    
    def xori(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "001110"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        imm = ""                        
        exec(f"imm = self.imm({registrador[2]})")                                                
        return hex(int((opcode + rs + rt + imm ),2))

    def addiu(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "001001"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        imm = ""                        
        exec(f"imm = self.imm({registrador[2]})")                                                
        return hex(int((opcode + rs + rt + imm ),2))

    def addu(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "100001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def subu(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"    
        rs = ""                    
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "100011"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def beq(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000100"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        label = ""                        
        exec(f"label = self.labels({registrador[2]})")                                                
        return hex(int((opcode + rs + rt + label),2))

    def bne(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000101"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        label = ""                        
        exec(f"label = self.labels({registrador[2]})")                                                
        return hex(int((opcode + rs + rt + label),2))

    def bgez(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000001"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = "00001"                        
        label = ""                        
        exec(f"label = self.labels({registrador[1]})")                                                
        return hex(int((opcode + rs + rt + label),2))

    def bgezal(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000001"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = "10001"                                                
        offset = ""
        exec(f"offset = self.labels({registrador[1]})")
        return hex(int((opcode + rs + rt + offset),2))
#TODO completar as instruções abaixo
    def c_eq_d(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "101001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))
#TODO completar as instruções abaixo
    def c_eq_s(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "101000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def clo(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "011100"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "100001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def div(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = {self.registrador[1]}()")                        
        rd = "00000"                                                
        shamt = "00000"                        
        funct = "011010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))
#TODO completar as instruções abaixo
    def div_d(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "111001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))
#TODO completar as instruções abaixo
    def div_s(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "111000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def j(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000010"                        
        label = ""
        exec(f"label = self.labels({registrador[0]})")                        
        return hex(int((opcode + label.zfill(26) ),2))

    def jal(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000011"                                                
        label = ""
        exec(f"label = self.labels({registrador[0]})")                        
        return hex(int((opcode + label.zfill(26) ),2))
#foi colocado no valor de shampt "00000" como hint
    def jalr(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = "00000"                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "001001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))
#foi colocado no valor de shampt "00000" como hint
    def jr(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = "00000"                                            
        rd = "00000"                                                
        shamt = "00000"                        
        funct = "001000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def lb(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "100000"                        
        base = ""                        
        exec(f"base, offset = self.offset({registrador[1]})")                        
        rt = ""                        
        exec(f"rt = self.{registrador[0]}()")                                                
        offset = ""                                               
        return hex(int((opcode + base + rt + offset),2))

    def lh(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "100001"                        
        base = ""                        
        exec(f"base, offset = self.offset({registrador[1]})")                        
        rt = ""                        
        exec(f"rt = self.{registrador[0]}()")                                                
        offset = ""                                               
        return hex(int((opcode + base + rt + offset),2))

    def lhu(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "100101"                        
        base = ""                        
        exec(f"base, offset = self.offset({registrador[1]})")                        
        rt = ""                        
        exec(f"rt = self.{registrador[0]}()")                                                
        offset = ""                                               
        return hex(int((opcode + base + rt + offset),2))
#TODO pseudo instrução
    def li(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "001111"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def lui(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "001111"                        
        rs = "00000"
        rt = ""                        
        exec(f"rt = self.{registrador[0]()}")                                                
        imm = ""
        exec(f"self.imm({registrador[1]})")               
        return hex(int((opcode + rs + rt + imm),2))

    def lw(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "100011"                        
        base = ""                        
        exec(f"base, offset = self.offset({registrador[1]})")                        
        rt = ""                        
        exec(f"rt = self.{registrador[0]}()")                                                
        offset = ""                                               
        return hex(int((opcode + base + rt + offset),2))

    def madd(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "011100"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]()}")                        
        rd = "00000"                                                
        shamt = "00000"                        
        funct = "00000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def mfhi(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = "00000"                        
        rt = "00000"                        
        rd = ""                        
        exec(f"rd = self.{registrador[0]}()")                        
        shamt = "00000"                        
        funct = "010000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def mflo(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = "00000"                        
        rt = "00000"                                               
        rd = ""                        
        exec(f"rd = self.{registrador[0]}()")                        
        shamt = "00000"                        
        funct = "010010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def movn(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "001011"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def msubu(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "011101"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = "00000"                                               
        shamt = "00000"                        
        funct = "000101"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def mul(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "011100"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = ""                        
        exec(f"rd = self.{registrador[2]}()")                        
        shamt = "00000"                        
        funct = "000010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))
####
    def mul_d(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "010010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))
####
    def mul_s(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "010000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def mult(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.{registrador[0]}()")                        
        rt = ""                        
        exec(f"rt = self.{registrador[1]}()")                        
        rd = "00000"                                               
        shamt = "00000"                        
        funct = "011000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sb(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "101000"                        
        base = ""                        
        exec(f"base, offset = self.offset({registrador[1]})")                        
        rt = ""                        
        exec(f"rt = self.{registrador[0]}()")                                                
        offset = ""                                               
        return hex(int((opcode + base + rt + offset),2))
#TODO
    def sll(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rt = ""                        
        exec(f"rs = self.registrador[0]")                        
        rd = ""                        
        exec(f"rt = self.registrador[1]")                                               
        shamt = ""                        
        funct = "000000"                        
        return hex(int((opcode +  rt + rd + shamt + funct),2))
#TODO
    def srl(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "000010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def slt(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "101010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def slti(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "001010"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sltu(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "101011"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sra(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "000011"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def srav(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "000111"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sub_d(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "000011"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sub_s(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "000010"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def sw(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "101011"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def teq(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "110100"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def tge(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "110000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def tgei(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "010000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def u(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "110001"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def tne(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "00001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "01000"                        
        return hex(int((opcode + rs + rt + rd + shamt + funct),2))

    def tnei(self):                        
        registrador = self.registradores.split(", ", "")                        
        opcode = "000001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
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
        instrucao, registradores = i.split(" ", 1)
        instrucao = instrucao.replace('.', '_')
        match instrucao:
            case 'add_d':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.add_d()                         
                translated.append(traduction) 

            case 'add_s':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.add_s()                         
                translated.append(traduction) 

            case 'add':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.add()                         
                translated.append(traduction) 

            case 'sub':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.sub()                         
                translated.append(traduction) 

            case 'and':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator._and()                         
                translated.append(traduction) 

            case 'or':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator._or()                         
                translated.append(traduction) 

            case 'nor':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.nor()                         
                translated.append(traduction) 

            case 'xor':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.xor()                         
                translated.append(traduction) 

            case 'addi':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.addi()                         
                translated.append(traduction) 

            case 'andi':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.andi()                         
                translated.append(traduction) 

            case 'ori':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.ori()                         
                translated.append(traduction) 

            case 'xori':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.xori()                         
                translated.append(traduction) 

            case 'addiu':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.addiu()                         
                translated.append(traduction) 

            case 'addu':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.addu()                         
                translated.append(traduction) 

            case 'subu':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.subu()                         
                translated.append(traduction) 

            case 'beq':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.beq()                         
                translated.append(traduction) 

            case 'bne':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.bne()                         
                translated.append(traduction) 

            case 'bgez':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.bgez()                         
                translated.append(traduction) 

            case 'bgezal':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.bgezal()                         
                translated.append(traduction) 

            case 'c_eq_d':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.c_eq_d()                         
                translated.append(traduction) 

            case 'c_eq_s':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.c_eq_s()                         
                translated.append(traduction) 

            case 'clo':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.clo()                         
                translated.append(traduction) 

            case 'div':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.div()                         
                translated.append(traduction) 

            case 'div_d':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.div_d()                         
                translated.append(traduction) 

            case 'div_s':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.div_s()                         
                translated.append(traduction) 

            case 'j':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.j()                         
                translated.append(traduction) 

            case 'jal':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.jal()                         
                translated.append(traduction) 

            case 'jalr':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.jalr()                         
                translated.append(traduction) 

            case 'jr':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.jr()                         
                translated.append(traduction) 

            case 'lb':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.lb()                         
                translated.append(traduction) 

            case 'lh':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.lh()                         
                translated.append(traduction) 

            case 'lhu':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.lhu()                         
                translated.append(traduction) 

            case 'li':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.li()                         
                translated.append(traduction) 

            case 'lui':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.lui()                         
                translated.append(traduction) 

            case 'lw':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.lw()                         
                translated.append(traduction) 

            case 'madd':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.madd()                         
                translated.append(traduction) 

            case 'mfhi':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.mfhi()                         
                translated.append(traduction) 

            case 'mflo':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.mflo()                         
                translated.append(traduction) 

            case 'movn':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.movn()                         
                translated.append(traduction) 

            case 'msubu':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.msubu()                         
                translated.append(traduction) 

            case 'mul':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.mul()                         
                translated.append(traduction) 

            case 'mul_d':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.mul_d()                         
                translated.append(traduction) 

            case 'mul_s':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.mul_s()                         
                translated.append(traduction) 

            case 'mult':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.mult()                         
                translated.append(traduction) 

            case 'sb':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.sb()                         
                translated.append(traduction) 

            case 'sll':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.sll()                         
                translated.append(traduction) 

            case 'srl':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.srl()                         
                translated.append(traduction) 

            case 'slt':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.slt()                         
                translated.append(traduction) 

            case 'slti':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.slti()                         
                translated.append(traduction) 

            case 'sltu':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.sltu()                         
                translated.append(traduction) 

            case 'sra':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.sra()                         
                translated.append(traduction) 

            case 'srav':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.srav()                         
                translated.append(traduction) 

            case 'sub_d':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.sub_d()                         
                translated.append(traduction) 

            case 'sub_s':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.sub_s()                         
                translated.append(traduction) 

            case 'sw':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.sw()                         
                translated.append(traduction) 

            case 'teq':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.teq()                         
                translated.append(traduction) 

            case 'tge':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.tge()                         
                translated.append(traduction) 

            case 'tgei':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.tgei()                         
                translated.append(traduction) 

            case 'u':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.u()                         
                translated.append(traduction) 

            case 'tne':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.tne()                         
                translated.append(traduction) 

            case 'tnei':                         
                translator = Translator(text, instrucao, registradores)
                traduction = translator.tnei()                         
                translated.append(traduction) 

    return translated



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