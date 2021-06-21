
import re

ler_arquivo = 'contatos.csv'
escrever_arquivo = 'emails_extraidos.txt'
delimitador = [',', ';']



def validaEmail(strEmail):
    if re.match("(.*)@(.*).(.*)", strEmail):
        return True
    return False

def writeFile(listData):
    file = open(escrever_arquivo, 'w+')
    strData = ""
    for item in listData:
        strData = strData +item +','
    file.write(strData)

listEmail = []
file = open(ler_arquivo, 'r', encoding="utf8")
listLine = file.readlines()


for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimitador:
        item = item.replace(str(delimeter), ' ')

    wordList = item.split()
    for word in wordList:
        if (validaEmail(word)):
            listEmail.append(word)

if listEmail:
    uniqEmail = set(listEmail)
    print(len(uniqEmail), "emails coletados!")
    writeFile(uniqEmail)
else:
    print("Sem emails no arquivo.")
