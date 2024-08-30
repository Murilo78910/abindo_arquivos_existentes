# Abre o arquivo em modo de leitura
with open('lista de telefones.txt', 'r') as arquivo:
    num_linhas = 0
    # Percorre cada linha do arquivo
    for linha in arquivo:
        # Exibe a linha no prompt
        print(linha.strip())  # strip() remove espaços em branco e quebras de linha extras
        num_linhas += 1

print("Total de linhas:", num_linhas)