"""
Nome do arquivo: MIPS.py
Propósito: Compilador assembly mips com 61 instrucoes
Autor: Rafael Marques, Aysamake Trentin
Data de criação: 19/05/2023
Versão: Versão 1.0
"""

class FloatRegisters:
    """
    Classe que define os registradores de ponto flutuante.

    Esta classe contém métodos que retornam os valores binários correspondentes aos registradores de ponto flutuante.

    Métodos:
        f0(): Retorna o valor binário do registrador f0.
        f1(): Retorna o valor binário do registrador f1.
        f2(): Retorna o valor binário do registrador f2.
        f3(): Retorna o valor binário do registrador f3.
        f4(): Retorna o valor binário do registrador f4.
        f5(): Retorna o valor binário do registrador f5.
        f6(): Retorna o valor binário do registrador f6.
        f7(): Retorna o valor binário do registrador f7.
        f8(): Retorna o valor binário do registrador f8.
        f9(): Retorna o valor binário do registrador f9.
        f10(): Retorna o valor binário do registrador f10.
    """
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
    """
    Classe responsável por gerenciar os registradores do sistema.

    Herda da classe FloatRegisters.

    Attributes:
        None

    Methods:
        imm(imediato: str) -> str:
            Converte o valor imediato para sua representação binária de 16 bits.

    """



    def imm(imediato: str) -> str:
        """
        Converte o valor imediato para sua representação binária de 16 bits.

        Args:
            imediato (str): O valor imediato a ser convertido.

        Returns:
            str: O valor imediato convertido para sua representação binária de 16 bits.
        """
        imediato = str(imediato)
        
        if 'x' in imediato:
            imediato = bin(int(imediato, 16))[2:].zfill(16)
            return imediato
        
        elif 'b' in imediato:
            imediato = imediato[2:].zfill(16)
            return imediato
        
        else:
            if '-' in imediato:
                imediato = imediato.replace("-", "")
                im_negativo = bin(int(imediato))
                im_positivo =  bin(int(imediato))[2:].zfill(16)
                im_negativo = bin(int("1111111111111111", 2) - int(im_positivo, 2) + 1)   
                return str(im_negativo[2:].zfill(16))
            
            else:
                return bin(int(imediato))[2:].zfill(16)

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
    """
    Classe responsável por traduzir instruções.

    Herda da classe Registers.

    Args:
        text (list): O texto da instrução.
        instrução (str): A instrução a ser traduzida.
        registradores (str): Os registradores a serem utilizados.

    Attributes:
        text (str): O texto da instrução.
        instrução (str): A instrução a ser traduzida.
        registradores (str): Os registradores a serem utilizados.
        rd (str): Registrador de destino.
        rs (str): Registrador de origem 1.
        rt (str): Registrador de origem 2.
        imediato (str): Valor imediato.
        _offset (str): Offset.
        base (str): Registrador base.
        label (str): Rótulo.
        ft (str): Registrador destino ponto flutuante.
        fs (str): Registrador origem 1 ponto flutuante.
        fd (str): Registrador origem 2 ponto flutuante.
    """

    def __init__(self, text: list, instrução: str, registradores: str) -> None:
        """
        Inicializa uma nova instância da classe Translator.

        Args:
            text (list): O texto da instrução.
            instrução (str): A instrução a ser traduzida.
            registradores (str): Os registradores a serem utilizados.
        """
        self.text = text
        self.instrução = instrução
        self.registradores = registradores.replace('$', '')
        self.rd = ""
        self.rs = ""
        self.rt = ""
        self.imediato = ""
        self._offset = ""
        self.base = ""
        self.label = ""
        self.ft = ""
        self.fs = ""
        self.fd = ""
        
    def labels(self, label: str) -> str:
        """
        Obtém o valor binário do rótulo.

        Args:
            label (str): O rótulo a ser procurado.

        Returns:
            str: O valor binário do rótulo, preenchido com 16 dígitos.
        """
        for i in self.text:
            if label in i:
                return bin((int(self.text.index(f'{i}')) + 1) * 4)[2:].zfill(16)
            
    def offset(self, endereço: str) -> str:
        """
        Calcula o offset e obtém o registrador base.

        Args:
            endereço (str): O endereço a ser processado.

        Returns:
            str: O valor do offset calculado.
        """
        offset, registrador = endereço.split('(')
        registrador = registrador.replace(')', '')
        offset = Registers.imm(offset)
        self.base = getattr(self, registrador)()
        return offset

    def sa(self, sa: str) -> str:
        """
        Obtém o valor binário do shamt.

        Args:
            sa (str): O valor do shamt.

        Returns:
            str: O valor binário do shamt, preenchido com 5 dígitos.
        """
        if int(sa) > 0:
            return  bin(int(sa)).zfill(5).replace('b', '0')      
        else:
            sa = bin(int(sa)).zfill(5).replace('b', '0').replace('-', '')
            return str(11111 - int(sa)) 
    
    def add_d(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        fmt = "10001"                                                
        self.ft = getattr(self, registrador[2])()
        self.fs = getattr(self, registrador[1])()
        self.fd = getattr(self, registrador[0])()
        funct = "000000"                        
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd + funct), 2))

    def add_s(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        fmt = "10001"                                                
        self.ft = getattr(self, registrador[2])()
        self.fs = getattr(self, registrador[1])()
        self.fd = getattr(self, registrador[0])()
        funct = "000000"                        
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd + funct), 2))

    def add(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"                        
        funct = "100000"
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def sub(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"                        
        funct = "100010"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def _and(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"                        
        funct = "100100"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def _or(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"                        
        funct = "100101"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def nor(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"                        
        funct = "100111"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def xor(self):                        
        registrador = self.registradores.split(", ")                        
                       
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[2]}()")                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "100110"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def addi(self):
        registrador = self.registradores.split(", ")
        opcode = "001000"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[0])()
        self.imediato = Registers.imm(registrador[2])
        return hex(int((opcode + self.rs + self.rt + self.imediato), 2))

    def andi(self):
        registrador = self.registradores.split(", ")
        opcode = "001100"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[0])()
        self.imediato = Registers.imm(registrador[2])
        return hex(int((opcode + self.rs + self.rt + self.imediato), 2))

    def ori(self):
        registrador = self.registradores.split(", ")
        opcode = "001101"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[0])()
        self.imediato = Registers.imm(registrador[2])
        return hex(int((opcode + self.rs + self.rt + self.imediato), 2))

    def xori(self):
        registrador = self.registradores.split(", ")
        opcode = "001110"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[0])()
        self.imediato = Registers.imm(registrador[2])
        
        return hex(int((opcode + self.rs + self.rt + self.imediato), 2))

    def addiu(self):
        registrador = self.registradores.split(", ")
        opcode = "001001"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[0])()
        self.imediato = Registers.imm(registrador[2])
        return hex(int((opcode + self.rs + self.rt + self.imediato), 2))

    def addu(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"
        funct = "100001"
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def subu(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"
        funct = "100011"
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def beq(self):
        registrador = self.registradores.split(", ")
        opcode = "000100"
        self.rs = getattr(self, registrador[0])()
        self.rt = getattr(self, registrador[1])()
        self.label = self.labels(registrador[2])
        return hex(int((opcode + self.rs + self.rt + self.label), 2))
    
    def bne(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000101"                        
        self.rs = getattr(self, registrador[0])()
        self.rt = getattr(self, registrador[1])()
        self.label = self.labels(registrador[2])                                             
        return hex(int((opcode + self.rs + self.rt + self.label),2))

    def bgez(self):
        registrador = self.registradores.split(", ")
        opcode = "000001"
        self.rs = getattr(self, registrador[0])()
        rt = "00001"
        self.label = self.labels(registrador[1])
        return hex(int((opcode + self.rs + rt + self.label), 2))

    def bgezal(self):
        registrador = self.registradores.split(", ")
        opcode = "000001"
        self.rs = getattr(self, registrador[0])()
        rt = "10001"
        self.label = self.labels(registrador[1])
        return hex(int((opcode + self.rs + rt + self.label), 2))

    def c_eq_d(self):
        registrador = self.registradores.split(", ")
        opcode = "010001"
        fmt = "10001"
        self.fs = getattr(self, registrador[0])()
        self.ft = getattr(self, registrador[1])()
        etc = "0011"
        cond = "0010"
        funct = "101001"
        return hex(int((opcode + fmt + self.ft + etc + cond + funct), 2))

    def c_eq_s(self):
        registrador = self.registradores.split(", ")
        opcode = "010001"
        fmt = "10000"
        self.fs = getattr(self, registrador[0])()
        self.ft = getattr(self, registrador[1])()
        etc = "0011"
        cond = "0010"
        funct = "101000"
        return hex(int((opcode + fmt + self.ft + self.fs + etc + cond + funct), 2))

    def clo(self):
        registrador = self.registradores.split(", ")
        opcode = "011100"
        self.rs = getattr(self, registrador[1])()
        rt = '00000'
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"
        funct = "100001"
        return hex(int((opcode + self.rs + rt + self.rd + shamt + funct), 2))

    def div(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[0])()
        self.rt = getattr(self, registrador[1])()
        rd = "00000"
        shamt = "00000"
        funct = "011010"
        return hex(int((opcode + self.rs + self.rt + rd + shamt + funct), 2))

    def div_d(self):
        registrador = self.registradores.split(", ")
        opcode = "010001"
        fmt = "10001"
        self.ft = getattr(self, registrador[2])()
        self.fs = getattr(self, registrador[1])()
        self.fd = getattr(self, registrador[0])()
        funct = "000011"
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd + funct), 2))

    def div_s(self):
        registrador = self.registradores.split(", ")
        opcode = "010001"
        fmt = "10000"
        self.ft = getattr(self, registrador[2])()
        self.fs = getattr(self, registrador[1])()
        self.fd = getattr(self, registrador[0])()
        funct = "000011"
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd + funct), 2))
    
    def j(self):
        registrador = self.registradores.split(", ")
        opcode = "000010"
        self.label = self.labels(registrador[0])
        return hex(int((opcode + self.label.zfill(26)), 2))

    def jal(self):
        registrador = self.registradores.split(", ")
        opcode = "000011"
        self.label = self.labels(registrador[0])
        return hex(int((opcode + self.label.zfill(26)), 2))

    def jalr(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[0])()
        rt = "00000"
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"
        funct = "001001"
        return hex(int((opcode + self.rs + rt + self.rd + shamt + funct), 2))

    def jr(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[0])()
        rt = "00000"
        rd = "00000"
        shamt = "00000"
        funct = "001000"
        return hex(int((opcode + self.rs + rt + rd + shamt + funct), 2))

    def lb(self):
        registrador = self.registradores.split(", ")
        opcode = "100000"
        self._offset = self.offset(registrador[1])
        self.rt = getattr(self, registrador[0])()
        return hex(int((opcode + self.base + self.rt + self._offset), 2))

    def lh(self):
        registrador = self.registradores.split(", ")
        opcode = "100001"
        self._offset = self.offset(registrador[1])
        self.rt = getattr(self, registrador[0])()
        return hex(int((opcode + self.base + self.rt + self._offset), 2))

    def lhu(self):
        registrador = self.registradores.split(", ")
        opcode = "100101"
        self._offset = self.offset(registrador[1])
        self.rt = getattr(self, registrador[0])()
        return hex(int((opcode + self.base + self.rt + self._offset), 2))

    def li(self):
        registrador = self.registradores.split(", ")
        opcode = "001111"
        rs = ""
        rs = getattr(self, registrador[0])
        rt = ""
        rt = getattr(self, registrador[1])
        rd = ""
        rd = getattr(self, registrador[2])
        shamt = ""
        funct = "None"
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def lui(self):
        registrador = self.registradores.split(", ")
        opcode = "001111"
        rs = "00000"
        self.rt = getattr(self, registrador[0])()
        self.imediato = Registers.imm(registrador[1])
        return hex(int((opcode + rs + self.rt + self.imediato), 2))

    def lw(self):
        registrador = self.registradores.split(", ")
        opcode = "100011"
        self._offset = self.offset(registrador[1])
        self.rt = getattr(self, registrador[0])()
        return hex(int((opcode + self.base + self.rt + self._offset), 2))

    def madd(self):
        registrador = self.registradores.split(", ")
        opcode = "011100"
        self.rs = getattr(self, registrador[0])()
        self.rt = getattr(self, registrador[1])()
        rd = "00000"
        shamt = "00000"
        funct = "000000"
        #0111 0001 0100 1011 0000 0000 0000 0000
        #0111 0001 0100 1011 0000 0000 00 0000
        #38a58000
        return hex(int((opcode + self.rs + self.rt + rd + shamt + funct), 2))

    def mfhi(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        rs = "00000"
        rt = "00000"
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"
        funct = "010000"
        return hex(int((opcode + rs + rt + self.rd + shamt + funct), 2))

    def mflo(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        rs = "00000"
        rt = "00000"
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"
        funct = "010010"
        return hex(int((opcode + rs + rt + self.rd + shamt + funct), 2))

    def movn(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"
        funct = "001011"
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))
    
    def msubu(self):
        registrador = self.registradores.split(", ")
        opcode = "011100"
        self.rs = getattr(self, registrador[0])()
        self.rt = getattr(self, registrador[1])()
        rd = "00000"
        shamt = "00000"
        funct = "000101"
        return hex(int((opcode + self.rs + self.rt + rd + shamt + funct), 2))

    def mul(self):
        registrador = self.registradores.split(", ")
        opcode = "011100"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"
        funct = "000010"
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def mul_d(self):
        registrador = self.registradores.split(", ")
        opcode = "010001"
        fmt = "10001"
        self.ft = getattr(self, registrador[2])()
        self.fs = getattr(self, registrador[1])()
        self.fd = getattr(self, registrador[0])()
        funct = "000010"
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd + funct), 2))

    def mul_s(self):
        registrador = self.registradores.split(", ")
        opcode = "010001"
        fmt = "10000"
        self.ft = getattr(self, registrador[2])()
        self.fs = getattr(self, registrador[1])()
        self.fd = getattr(self, registrador[0])()
        funct = "000010"
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd + funct), 2))

    def mult(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[0])()
        self.rt = getattr(self, registrador[1])()
        rd = "00000"
        shamt = "00000"
        funct = "011000"
        return hex(int((opcode + self.rs + self.rt + rd + shamt + funct), 2))

    def sb(self):
        registrador = self.registradores.split(", ")
        opcode = "101000"
        self._offset = self.offset(registrador[1])
        self.rt = getattr(self, registrador[0])()
        return hex(int((opcode + self.base + self.rt + self._offset), 2))

    def sll(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        rs = "00000"
        self.rt = getattr(self, registrador[1])()
        self.rd = getattr(self, registrador[0])()
        sa = self.sa(registrador[2])
        funct = "000000"
        return hex(int((opcode + rs + self.rt + self.rd + sa + funct), 2))

    def srl(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        rs = "00000"
        self.rt = getattr(self, registrador[1])()
        self.rd = getattr(self, registrador[0])()
        sa = self.sa(registrador[2])
        funct = "000010"                
        return hex(int((opcode + rs + self.rt + self.rd + sa + funct),2))

    def slt(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"
        funct = "101010"
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def slti(self):
        registrador = self.registradores.split(", ")
        opcode = "001010"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[0])()
        self._imediato = Registers.imm(registrador[2])
        return hex(int((opcode + self.rs + self.rt + self._imediato), 2))

    def sltu(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[1])()
        self.rd = getattr(self, registrador[0])()
        shamt = "00000"
        funct = "101011"
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def sra(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        rs = "00000"
        self.rt = getattr(self, registrador[1])()
        self.rd = getattr(self, registrador[0])()
        sa = self.sa(registrador[2])
        funct = "000011"
        return hex(int((opcode + rs + self.rt + self.rd + sa + funct), 2))

    def srav(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[1])()
        self.rt = getattr(self, registrador[2])()
        self.rd = getattr(self, registrador[0])()
        shamt = "000000"
        funct = "000111"
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct), 2))

    def sub_d(self):
        registrador = self.registradores.split(", ")
        opcode = "010001"
        self.fs = getattr(self, registrador[1])()
        self.ft = getattr(self, registrador[2])()
        self.fd = getattr(self, registrador[0])()
        fmt = "10001"
        funct = "000001"
        return hex(int((opcode + self.ft + self.fs + self.fd + fmt + funct), 2))

    def sub_s(self):
        registrador = self.registradores.split(", ")
        opcode = "010001"
        self.fs = getattr(self, registrador[1])()
        self.ft = getattr(self, registrador[2])()
        self.fd = getattr(self, registrador[0])()
        fmt = "10000"
        funct = "000001"
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd + funct), 2))

    def sw(self):
        registrador = self.registradores.split(", ")
        opcode = "101011"
        self.rt = getattr(self, registrador[0])()
        self._offset = self.offset(registrador[1])
        return hex(int((opcode + self.base + self.rt + self._offset), 2))

    def teq(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[0])()
        self.rt = getattr(self, registrador[1])()
        code = "0000000000"
        funct = "110100"
        return hex(int((opcode + self.rs + self.rt + code + funct), 2))

    def tge(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[0])()
        self.rt = getattr(self, registrador[1])()
        code = "0000000000"
        funct = "110000"
        return hex(int((opcode + self.rs + self.rt + code + funct), 2))

    def tgei(self):
        registrador = self.registradores.split(", ")
        opcode = "000001"
        self.rs = getattr(self, registrador[0])()
        tgei = "01000"
        self.imediato = Registers.imm(registrador[1])
        return hex(int((opcode + self.rs + tgei + self.imediato), 2))

    def tgeu(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[0])()
        self.imediato = Registers.imm(registrador[1])
        code = "0000000000"
        funct = "110001"
        return hex(int((opcode + self.rs + self.rt + code + funct), 2))

    def tne(self):
        registrador = self.registradores.split(", ")
        opcode = "000000"
        self.rs = getattr(self, registrador[0])()
        self.rt = getattr(self, registrador[1])()
        tne = "0000000000"
        funct = "110110"
        return hex(int((opcode + self.rs + self.rt + tne + funct), 2))

    def tnei(self):
        registrador = self.registradores.split(", ")
        opcode = "000001"
        self.rs = getattr(self, registrador[0])()
        tnei = "01110"
        self.imediato = Registers.imm(registrador[1])
        return hex(int((opcode + self.rs + tnei + self.imediato), 2))


class Assembler(Translator):

    """
        Classe responsável por compilar e traduzir um arquivo de assembly.

    """

    def __init__(self, path: str, arquivo_destino: str):
        """
        Inicializa a classe Assembler.

        Args:
            path (str): O caminho do arquivo a ser compilado.
        """
        import os

        diretorio = os.path.dirname(path)
        nome_arquivo = os.path.basename(path)
        self.path: str = os.path.join(diretorio, nome_arquivo)

        file_path = os.path.abspath(__file__)
        directory = os.path.dirname(file_path)
        self.path_destino: str = os.path.join(directory, arquivo_destino)

        self.asm: list[str] = list()
        self.data: list[str] = list()
        self.text: list[str] = list()
        self.text_hexa: list[str] = list()
        self.linha: list[str] = list()
        self.load_file()
        self.translate_text()
        self.translate_data()

    def is_label(self, linha: str) -> None:
        """
        Verifica se a linha atual é uma label.

        Returns:
        None
        """
        if ":" in linha:
                label, instrucao, registradores = linha.split(" ", 2)
                instrucao = instrucao.replace('.', '_')
        else:
            instrucao, registradores = linha.split(" ", 1)
            instrucao = instrucao.replace('.', '_')
        self.linha = [instrucao, registradores]
        return 
    
    def read_file(self) -> list[str]:
        """
        Lê o arquivo de assembly e retorna uma lista com as linhas lidas.

        Returns:
            list[str]: Lista com as linhas lidas do arquivo de assembly.
        """
        with open(self.path, 'r', encoding="utf-8") as arq:
            asm = arq.readlines()
        return asm

    def load_file(self) -> None:
        """
        Carrega o arquivo de assembly e separa as seções de dados e texto em listas.

        Returns:
            None
        """
        self.asm: list[str] = self.read_file()
        asm: list[str] = self.asm
        data: list[str] = list()
        text: list[str] = list()
        data_area: bool = None
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
        self.data = data
        self.text = text

    def translate_text(self) -> None:
        """
        Traduz o texto da seção de texto para instruções correspondentes.

        Returns:
            None
        """
        text: list[str] = self.text
        translated: list[str] = list()
        for linha in text:
            if linha:
                self.is_label(linha)
                instrucao, registradores = self.linha[0], self.linha[1]

                match instrucao:
                    case 'add_d':
                        translator: Translator = Translator(text, instrucao, registradores)
                        traduction: str = translator.add_d()
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
                        imediato = registradores.split(', ')[1]
                        imm = Registers.imm(imediato)
                        imm = int('0b'+imm,2)
                        if imm < 65536:
                            imm = hex(imm)
                            imm = imm.replace('0x', '')
                            registradores = registradores.split(', ')[0]+ ', ' + '$zero' +   ', ' + '0x' + imm.zfill(8)
                            translator = Translator(text, instrucao, registradores)
                            traduction = translator.addiu()                         
                            translated.append(traduction)
                        else:
                            imm = hex(imm)
                            imm = imm.replace('0x', '')
                            tamanho = len(imm)
                            ori_imm = imm[-4:]
                            tamanho -= 4
                            lui_imm = imm[:tamanho]
                            registradores_ori = str(registradores.split(", ")[0]
                                                    )+ ", " + "$at" + ", " + "0x" + ori_imm.zfill(8)
                            registradores_lui = '$at' + ", " + '0x' + lui_imm.zfill(8)

                            translator = Translator(text, instrucao, registradores_lui)
                            traduction = translator.lui()                         
                            translated.append(traduction)
                            translator = Translator(text, instrucao, registradores_ori)
                            traduction = translator.ori()
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

                    case 'tgeu':                         
                        translator = Translator(text, instrucao, registradores)
                        traduction = translator.tgeu()                         
                        translated.append(traduction) 

                    case 'tne':                         
                        translator = Translator(text, instrucao, registradores)
                        traduction = translator.tne()                         
                        translated.append(traduction) 

                    case 'tnei':                         
                        translator = Translator(text, instrucao, registradores)
                        traduction = translator.tnei()                         
                        translated.append(traduction) 

                    case _:
                        if '#'in linha or '%' in linha:
                            pass
                        else:
                            raise Exception('Instrução não suportada')

        self.text = translated
        return self.write_mif_text()

    def translate_data(self) -> None:
        """
        Translates data in the assembly file to hexadecimal format.
    
        This method translates specific data sections in the assembly file to their corresponding hexadecimal representation.
        It supports three types of data: '.word', '.ascii', and '.float'.
        
        Args:
            self: The object instance.
        
        Returns:
            None
        
        Raises:
            None

        Examples:
            # Example usage of translate_data()
            obj = MyClass()
            obj.translate_data()
        """
        data = self.data
        translated = []
        for line in data:
            if  '.word' in line:
                line = line.split(' ', 2)[2]
                line = line.split(', ')
                for word in line:
                    word = hex(int(word))
                    word = word.replace('x', '0').zfill(8)
                    translated.append(word)
                    
            elif '.ascii' in line:
                line = line.split(' ', 2)[2]
                line = line.split(', ')
                hex_text = ''
                for text in line:
                    for char in text:
                        hex_value = hex(ord(char))[2:]  # Obtém o valor hexadecimal sem o prefixo "0x"
                        hex_text += hex_value
                    translated.append(hex_text)

            elif '.float' in line:
                import struct
                line = line.split(' ', 2)[2]
                line = line.split(', ')
                for num in line:
                    packed = struct.pack('!f', num)
                    hex_value = ''.join('{:02x}'.format(b) for b in packed)                
                    translated.append(hex_value)

        self.data = translated
        return self.write_mif_data()

    def write_mif_text(self) -> None:
        """
        Escreve o arquivo de saída em formato MIF (Memory Initialization File).

        Args:
            path_destino (str): O caminho de destino para o arquivo MIF.

        Returns:
            None
        """
        path_destino: str = self.path_destino
        traduction: list[str] = self.text
        contador: int = 0
        with open(path_destino + "_text.mif", "w", encoding="ASCII") as f:
            depth: int = len(traduction) * 256
            f.write(f"DEPTH = {depth};\n") * int(len(traduction))
            f.write("WIDTH = 32;\n")
            f.write("ADDRESS_RADIX = HEX;\n")
            f.write("DATA_RADIX = HEX;\n")
            f.write("CONTENT\n")
            f.write("BEGIN\n")
            f.write("\n")
            
            for i in range(len(traduction)):
                linha_hexa: str = hex(contador)
                linha_hexa = linha_hexa.split("x")[1]
                linha_hexa= linha_hexa.zfill(8)
                instrucao = traduction[i]
                instrucao = instrucao.split("x")[1].zfill(8)
                f.write(str(linha_hexa) + " : " + instrucao + ";\n")
                contador += 4

            f.write("\n")
            f.write( "END ;\n")
            f.close()
        return print(f"Caminho do arquivo:    \n\t\t\t" + path_destino +'_text.mif')

    def write_mif_data(self) -> None:
        """
        Escreve o arquivo de saída em formato MIF (Memory Initialization File).

        Args:
            path_destino (str): O caminho de destino para o arquivo MIF.

        Returns:
            None
        """
        path_destino: str = self.path_destino
        traduction: list[str] = self.data
        contador: int = 0
        with open(path_destino + "_data.mif", "w", encoding="ASCII") as f:
            depth: int = len(traduction) * 256
            f.write(f"DEPTH = {depth};\n") * int(len(traduction))
            f.write("WIDTH = 32;\n")
            f.write("ADDRESS_RADIX = HEX;\n")
            f.write("DATA_RADIX = HEX;\n")
            f.write("CONTENT\n")
            f.write("BEGIN\n")
            f.write("\n")
            
            for i in range(len(traduction)):
                linha_hexa: str = hex(contador)
                linha_hexa = linha_hexa.split("x")[1]
                linha_hexa= linha_hexa.zfill(8)
                instrucao = traduction[i]
                f.write(str(linha_hexa) + " : " + instrucao + ";\n")
                contador += 4

            f.write("\n")
            f.write( "END ;\n")
            f.close()
        return print(f"Caminho do arquivo:\n\t\t\t" + path_destino +'_data.mif') 
  

if __name__ == "__main__":
    # path = input("Digite o caminho do arquivo(path = '/home/usuario/projeto/arquivo.asm'):\t\t")
    # path_destino = input("Digite o nome do arquivo de destino, sem extensao ('saida_teste1'):\t\t\t")
    path = "C:\\dev1\\Projetos\\oac-mips\\compilador_mips\\archives\\exemplos\\exemplo_teste.asm"
    path_destino = "saida_teste1"
    compiled = Assembler(path, path_destino)


#TODO 
#olhar o xori
#olhar width e lenght do mif
#tirar print do caminho destino 


