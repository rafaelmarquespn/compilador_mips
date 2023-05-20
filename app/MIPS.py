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

    def imm(self, imediato:str):
        imediato = str(imediato)
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
    """
    Classe responsável por traduzir instruções.

    Herda da classe Registers.

    Args:
        text (str): O texto da instrução.
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

    def __init__(self, text: str, instrução: str, registradores: str) -> None:
        """
        Inicializa uma nova instância da classe Translator.

        Args:
            text (str): O texto da instrução.
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
            i = i.replace(':', '')
            if label == i:
                return bin((int(self.text.index(f'{i}:')) + 1) * 4)[2:].zfill(16)
            
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
        offset = self.imm(offset)
        exec(f'self.base = self.{registrador}()')
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
        exec(f"self.ft = self.{registrador[2]}")                        
        exec(f"self.fs = self.{registrador[1]}")                         
        exec(f"self.fd = self.{registrador[0]}")                         
        funct = "000000"                        
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd  + funct),2))

    def add_s(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        fmt = "10001"                                                
        exec(f"self.ft = self.{registrador[2]}")                        
        exec(f"self.fs = self.{registrador[1]}")                         
        exec(f"self.fd = self.{registrador[0]}")                         
        funct = "000000"                        
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd  + funct),2))

    def add(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[2]}()")                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "100000"
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def sub(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[2]}()")                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "100010"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def _and(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[2]}()")                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "100100"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def _or(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[2]}()")                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "100101"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def nor(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[2]}()")                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "100111"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

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
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[0]}()")                                                
        exec(f"self.imediato = self.imm({registrador[2]})")                                                
        return hex(int((opcode + self.rs + self.rt + self.imediato ),2))

    def andi(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "001100"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[0]}()")                        
        exec(f"self.imediato = self.imm({registrador[2]})")                                                
        return hex(int((opcode + self.rs + self.rt + self.imediato ),2))
    
    def ori(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "001101"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[0]}()")                        
        exec(f"self.imediato = self.imm({registrador[2]})")                                                
        return hex(int((opcode + self.rs + self.rt + self.imediato),2))
    
    def xori(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "001110"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[0]}()")                        
        exec(f"self.imediato = self.imm({registrador[2]})")                                                
        return hex(int((opcode + self.rs + self.rt + self.imediato),2))

    def addiu(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "001001"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[0]}()")                        
        exec(f"self.imediato = self.imm({registrador[2]})")                                                
        return hex(int((opcode + self.rs + self.rt + self.imediato),2))

    def addu(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[2]}()")                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "100001"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def subu(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[2]}()")                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "100011"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def beq(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000100"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        exec(f"self.rt = self.{registrador[1]}()")                                                
        exec(f"self.label = self.labels({registrador[2]})")                                                
        return hex(int((opcode + self.rs + self.rt + self.label),2))

    def bne(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000101"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        exec(f"self.rt = self.{registrador[1]}()")                        
        exec(f"self.label = self.labels({registrador[2]})")                                                
        return hex(int((opcode + self.rs + self.rt + self.label),2))

    def bgez(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000001"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        rt = "00001"                                                
        exec(f"self.label = self.labels({registrador[1]})")                                                
        return hex(int((opcode + self.rs + rt + self.label),2))

    def bgezal(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000001"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        rt = "10001"                                                
        exec(f"self.label = self.labels({registrador[1]})")
        return hex(int((opcode + self.rs + rt + self.label),2))
#TODO completar as instruções abaixo
    def c_eq_d(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "101001"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))
#TODO completar as instruções abaixo
    def c_eq_s(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "101000"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def clo(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "011100"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        rt = '00000'                       
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "100001"                        
        return hex(int((opcode + self.rs + rt + self.rd + shamt + funct),2))

    def div(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        exec(f"self.rt = self.{registrador[1]}()")                        
        rd = "00000"                                                
        shamt = "00000"                        
        funct = "011010"                        
        return hex(int((opcode + self.rs + self.rt + rd + shamt + funct),2))
    
    def div_d(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        fmt = "10001"                                                
        exec(f"self.ft = self.{registrador[2]}")                        
        exec(f"self.fs = self.{registrador[1]}")                         
        exec(f"self.fd = self.{registrador[0]}")                         
        funct = "000011"                        
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd  + funct),2))

    def div_s(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        fmt = "10000"                                                
        exec(f"self.ft = self.{registrador[2]}")                        
        exec(f"self.fs = self.{registrador[1]}")                         
        exec(f"self.fd = self.{registrador[0]}")                         
        funct = "000011"                        
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd  + funct),2))

    def j(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000010"                        
        exec(f"self.label = self.labels({registrador[0]})")                        
        return hex(int((opcode + self.label.zfill(26) ),2))

    def jal(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000011"                                                
        exec(f"self.label = self.labels({registrador[0]})")                        
        return hex(int((opcode + self.label.zfill(26) ),2))
    
    def jalr(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        rt = "00000"                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "001001"                        
        return hex(int((opcode + self.rs + rt + self.rd + shamt + funct),2))
    
    def jr(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        rt = "00000"                                            
        rd = "00000"                                                
        shamt = "00000"                        
        funct = "001000"                        
        return hex(int((opcode + self.rs + rt + rd + shamt + funct),2))

    def lb(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "100000"                                                
        exec(f"self._offset = self.offset('{registrador[1]}')")                        
        exec(f"self.rt = self.{registrador[0]}()")                                                
        return hex(int((opcode + self.base + self.rt + self._offset),2))

    def lh(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "100001"                        
        exec(f"self._offset = self.offset('{registrador[1]}')")                        
        exec(f"self.rt = self.{registrador[0]}()")                                                
        return hex(int((opcode + self.base + self.rt + self._offset),2))

    def lhu(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "100101"                        
        exec(f"self._offset = self.offset('{registrador[1]}')")                        
        exec(f"self.rt = self.{registrador[0]}()")                                                
        return hex(int((opcode + self.base + self.rt + self._offset),2))
#TODO pseudo instrução
    def li(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "001111"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "None"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def lui(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "001111"                        
        rs = "00000"
        exec(f"self.rt = self.{registrador[0]}()")                                                
        exec(f"self.imediato = self.imm({registrador[1]})")               
        return hex(int((opcode + rs + self.rt + self.imediato),2))

    def lw(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "100011"                        
        exec(f"self._offset = self.offset('{registrador[1]}')")                       
        exec(f"self.rt = self.{registrador[0]}()")                                                
        return hex(int((opcode + self.base + self.rt + self._offset),2))

    def madd(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "011100"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        exec(f"self.rt = self.{registrador[1]}()")                        
        rd = "00000"                                                
        shamt = "00000"                        
        funct = "00000"                        
        return hex(int((opcode + self.rs + self.rt + rd + shamt + funct),2))

    def mfhi(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        rs = "00000"                        
        rt = "00000"                        
        exec(f"self.rd = self.{registrador[0]}()")                        
        shamt = "00000"                        
        funct = "010000"                        
        return hex(int((opcode + rs + rt + self.rd + shamt + funct),2))

    def mflo(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        rs = "00000"                        
        rt = "00000"                                               
        exec(f"self.rd = self.{registrador[0]}()")                        
        shamt = "00000"                        
        funct = "010010"                        
        return hex(int((opcode + rs + rt + self.rd + shamt + funct),2))

    def movn(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[2]}()")                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "001011"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2)).zfill(10)

    def msubu(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "011100"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        exec(f"self.rt = self.{registrador[1]}()")                        
        rd = "00000"                                               
        shamt = "00000"                        
        funct = "000101"                        
        return hex(int((opcode + self.rs + self.rt + rd + shamt + funct),2))

    def mul(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "011100"                        
        exec(f"self.rs = self.{registrador[1]}()")                        
        exec(f"self.rt = self.{registrador[2]}()")                        
        exec(f"self.rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "000010"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def mul_d(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        fmt = "10001"                                                
        exec(f"self.ft = self.{registrador[2]}")                        
        exec(f"self.fs = self.{registrador[1]}")                         
        exec(f"self.fd = self.{registrador[0]}")                         
        funct = "000010"                        
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd  + funct),2))

    def mul_s(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        fmt = "10000"                                                
        exec(f"self.__ft = self.{registrador[2]}")                        
        exec(f"self.__fs = self.{registrador[1]}")                         
        exec(f"self.__fd = self.{registrador[0]}")                         
        funct = "000010"                        
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd  + funct),2))

    def mult(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.__rs = self.{registrador[0]}()")                        
        exec(f"self.__rt = self.{registrador[1]}()")                        
        rd = "00000"                                               
        shamt = "00000"                        
        funct = "011000"                        
        return hex(int((opcode + self.rs + self.rt + rd + shamt + funct),2))

    def sb(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "101000"                        
        exec(f"self._offset = self.offset('{registrador[1]}')")                        
        exec(f"self.rt = self.{registrador[0]}()")                                                
        return hex(int((opcode + self.base + self.rt + self._offset),2))
    
    def sll(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"  
        rs = "00000"                      
        exec(f"self.__rt = self.{registrador[1]}()")                        
        exec(f"self.__rd = self.{registrador[0]}()")                                               
        sa = self.sa(registrador[2])                    
        funct = "000000"                        
        return hex(int((opcode + rs + self.rt + self.rd + sa + funct),2))

    def srl(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        rs = "00000"                        
        exec(f"self.__rt = self.{registrador[1]}()")                        
        exec(f"self.__rd = self.{registrador[0]}()")                        
        sa = self.sa(registrador[2])                       
        funct = "000010"                        
        return hex(int((opcode + rs + self.rt + self.rd + sa + funct),2))

    def slt(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.__rs = self.{registrador[1]}()")                        
        exec(f"self.__rt = self.{registrador[2]}()")                        
        exec(f"self.__rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "101010"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def slti(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "001010"                        
        exec(f"self.__rs = self.{registrador[1]}()")                        
        exec(f"self.__rt = self.{registrador[0]}()")                        
        exec(f"self.__imediato = self.imm({registrador[2]})")                        
        return hex(int((opcode + self.__rs + self.__rt + self.__imediato),2))

    def sltu(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.__rs = self.{registrador[1]}()")                        
        exec(f"self.__rt = self.{registrador[1]}()")                        
        exec(f"self.__rd = self.{registrador[0]}()")                       
        shamt = "00000"                        
        funct = "101011"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def sra(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        rs = "00000"                                               
        exec(f"self.__rt = self.{registrador[1]}()")                        
        exec(f"self.__rd = self.{registrador[0]}()")
        sa = self.sa(registrador[2])
        funct = "000011"                        
        return hex(int((opcode + rs + self.rt + self.rd + sa + funct),2))

    def srav(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.__rs = self.{registrador[1]}()")                        
        exec(f"self.__rt = self.{registrador[2]}()")                        
        exec(f"self.__rd = self.{registrador[0]}()")                       
        shamt = "000000"                        
        funct = "000111"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))
    
    def sub_d(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        exec(f"self.fs = self.{registrador[1]}()")                        
        exec(f"self.ft = self.{registrador[2]}()")                                             
        exec(f"self.fd = self.{registrador[0]}()")                        
        fmt = "10001"                       
        funct = "000001"                        
        return hex(int((opcode + self.__ft + self.__fs + self.__fd + fmt + funct),2))                   

    def sub_s(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "010001"                        
        exec(f"self.fs = self.{registrador[1]}()")                        
        exec(f"self.ft = self.{registrador[2]}()")                                             
        exec(f"self.fd = self.{registrador[0]}()")                          
        fmt = "10000"                        
        funct = "000001"                        
        return hex(int((opcode + fmt + self.ft + self.fs + self.fd + funct),2))

    def sw(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "101011"                                               
        exec(f"self.rt = self.{registrador[0]}()")                                               
        exec(f"self._offset = self.offset('{registrador[1]}')")                                           
        return hex(int((opcode + self.base + self.rt + self._offset),2))

    def teq(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        exec(f"self.rt = self.{registrador[1]}()")                                              
        code = "0000000000"                        
        funct = "110100"                        
        return hex(int((opcode + self.rs + self.rt + code + funct),2))

    def tge(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        exec(f"self.rt = self.{registrador[1]}()")                                              
        code = "0000000000"                        
        funct = "110000"                        
        return hex(int((opcode + self.rs + self.rt + code + funct),2))

    def tgei(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000001"                        
        exec(f"self.rs = self.{registrador[0]}()")                        
        tgei = "01000"                                         
        imm = ""
        exec(f"self.imediato = self.imm({registrador[1]})")
        return hex(int((opcode + self.rs + tgei + self.imediato),2))
#não ta na documentação fornecida
    def u(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        rs = ""                        
        exec(f"rs = self.registrador[0]")                        
        rt = ""                        
        exec(f"rt = self.registrador[1]")                        
        rd = ""                        
        exec(f"rd = self.registrador[2]")                        
        shamt = ""                        
        funct = "110001"                        
        return hex(int((opcode + self.rs + self.rt + self.rd + shamt + funct),2))

    def tne(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000000"                        
        exec(f"self.__rs = self.{registrador[0]}()")                        
        exec(f"self.__rt = self.{registrador[1]}()")                        
        tne = "0000000000"                     
        funct = "110110"                        
        return hex(int((opcode + self.rs + self.rt + tne + funct),2))

    def tnei(self):                        
        registrador = self.registradores.split(", ")                        
        opcode = "000001"                        
        exec(f"self.rs = self.{registrador[0]}()")  
        tnei = "01110"                      
        exec(f"self.imediato = self.imm({registrador[1]})")
        return hex(int((opcode + self.rs + tnei + self.imediato),2))


class Compiler(Translator):
    """Classe responsável por compilar e traduzir um arquivo de assembly."""

    def __init__(self, path: str):
        """
        Inicializa a classe Compiler.

        Args:
            path (str): O caminho do arquivo a ser compilado.
        """
        self.path: str = path
        self.asm: list[str] = list()
        self.data: list[str] = list()
        self.text: list[str] = list()
        self.text_hexa: list[str] = list()

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
        for i in text:
            instrucao, registradores = i.split(" ", 1)
            instrucao = instrucao.replace('.', '_')
            match instrucao:
                case 'add_d':
                    translator: Translator = Translator(text, instrucao, registradores)
                    traduction: str = translator.add_d()
                    translated.append(traduction)

                # Resto das traduções de instruções omitidas por brevidade

        self.text = translated

    def write_mif_text(self, path_destino: str) -> None:
        """
        Escreve o arquivo de saída em formato MIF (Memory Initialization File).

        Args:
            path_destino (str): O caminho de destino para o arquivo MIF.

        Returns:
            None
        """

        traduction: list[str] = self.text
        contador: int = 0
        with open(path_destino, "w", encoding="ASCII") as f:
            f.write("DEPTH = 256;\n") * int(len(traduction))
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
                contador += 1

            f.write("\n")
            f.write( "END ;\n")
            f.close()
        return print(f"Arquivo compilado com sucesso!    \n" + path_destino)

        
    
    

if __name__ == "__main__":
    #path = input("Digite o caminho do arquivo(root\\\example_entrada.asm):\t\t")
    compiled = Compiler("D:\\developer\\projetos\\OAC-MIPS\\app\\archives\\exemplos\\example_saida.asm")
    start = compiled.load_file()
    compiled.translate_text()
    #path_destino = input("Digite o caminho do arquivo de destino(root\\\example_saida.mif):\t\t")
    compiled.write_mif_text("tests\\archives\\saida1.mif")
    





