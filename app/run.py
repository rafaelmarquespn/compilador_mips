from MIPS import Compiler

if __name__ == "__main__":
    #path = input("Digite o caminho do arquivo(path = "/home/usuario/projeto/arquivo.asm"):\t\t")
    #path_destino = input("Digite o caminho do arquivo de destino(path = "/home/usuario/projeto/arquivo.mif"):\t\t")
    path = "D:\\developer\\projetos\\OAC-MIPS\\archives\\exemplos\\example_saida.asm"
    path_destino = "D:\\developer\\projetos\\OAC-MIPS\\tests\\archives\\saida1.mif"
    compiled = Compiler(path, path_destino)