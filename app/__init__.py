import os 
import sys
file_path = os.path.abspath(__file__)
directory = os.path.dirname(file_path)
print('Diretório atual: ', directory)
directory = directory.split('\\app', )[0]
file_path =  os.path.join(directory , 'archives\\exemplos\\example_saida_text.mif')
abrir_arquivo = os.system(file_path)