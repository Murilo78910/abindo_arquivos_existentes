import pywhatkit
import pywhatkit.whats
import pyautogui
import time

num = input('Digite o número de telefone: ')

# Função para ler os números de telefone do arquivo .txt
def ler_numeros_de_telefone(nome_do_arquivo):
    numeros = []
    with open(nome_do_arquivo, 'r') as arquivo:
        for linha in arquivo:
            numero = linha.strip() # Remover espaços em branco e quebras de linha
            numeros.append(numero)
    return numeros

# Ler os números de telefone do arquivo
arquivo_telefones = "lista de telefones.txt"
numeros_de_telefone = ler_numeros_de_telefone(arquivo_telefones)

if num in numeros_de_telefone:
    print('Esse número já está nessa lista.')
else:
    print('Esse número ainda não está na lista.')
