import csv
from collections import defaultdict

colunas = defaultdict(list)

with open('contatos.csv', encoding="utf8") as f:
    leitor = csv.DictReader(f) # ler linhas em um formato de dicionário
    for row in leitor: # leia uma linha como {coluna1: valor1, coluna2: valor2, ...}
        for (k,v) in row.items(): # repasse o nome e valor de cada coluna
            colunas[k].append(v) # acrescente o valor na lista apropriada com base no nome da coluna k





file = open('telefones_extraidos.txt', 'w+')
for telefone in colunas['Phone']:
    try:
        #print(telefone)
        file.write(telefone + '\n')

    except Exception as e:
        pass
file.close()