import csv
from collections import defaultdict

colunas = defaultdict(list)

with open('contatos.csv', encoding="utf8") as f:
    leitor = csv.DictReader(f) # ler linhas em um formato de dicionário
    for row in leitor: # leia uma linha como {coluna1: valor1, coluna2: valor2, ...}
        for (k,v) in row.items(): # repasse o nome e valor de cada coluna
            colunas[k].append(v) # acrescente o valor na lista apropriada com base no nome da coluna k

#cria o arquivo para salvar os dados extraidos do CSV para formato de celular
file = open('contatos_para_celular.vcf', 'w+')


#percorre todos os dados do CSV extraindo somente o nome e telefone
for nome, telefone,email in  zip(colunas['First Name'],colunas['Phone'],colunas['Email']):
    # se o nome ou telefone estiver vazio ele pula e nao salva os dados
    if nome == '' or telefone == '':
        pass
    else:
        #se existir o nome e telefone ele salva os dados
        print(f'Nome:{nome}  --- Telefone: {telefone} -- Email: {email}')
        texto = f"""BEGIN:VCARD
VERSION:2.1
N:;{nome};;;
FN:{nome}
TEL;CELL:{telefone}
TEL;CELL:{telefone}
EMAIL;HOME:{email}
END:VCARD"""

# grava em um documento .vcf o texto com nome  e telefone dos contatos
        file.write(texto + '\n')
file.close()