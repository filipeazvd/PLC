
import re
from unidecode import unidecode
import numpy as np
import scipy
import json
from scipy.stats import norm
import os

"""
---------------  fazer umas certas perguntas --------------

order: nome | email | entidade | nível | número de chamadas ao backend
ex: Élia Cristina Viegas Pedro :: epedro@ccdr-alg.pt :: ent_CCDR-Alg :: 1 :: 0

1:Produz uma listagem apenas com o nome e a entidade do utilizador, ordenada alfabeticamente por nome

2:Produz uma lista ordenada alfabeticamente das entidades referenciadas, indicando, para cada uma, quantos
utilizadores estão registados

3:Qual a distribuição de utilizadores por níveis de acesso?

4:Produz uma listagem dos utilizadores, agrupados por entidade, ordenada primeiro pela entidade e dentro desta
pelo nome

5:Por fim, produz os seguintes indicadores:
1. Quantos utilizadores?
2. Quantas entidades?
3. Qual a distribuição em número por entidade?
4. Qual a distribuição em número por nível?
"""
path = "C:\\Users\\filip\\Desktop\\Python\\RegularExpressions\\clav-users.txt"

def abrirficheiro(path):
    with open(path,'r',encoding="utf-8") as file:
        content = file.read()    

    return content

def primeiro():
    lista1 = []
    lista3 = []
    lista2 = []
    #tenho a str com o ficheiro todo no txt
    txt = abrirficheiro(path)
    txtstripped = txt.split("\n")
    #print(txtstripped)
    for line in txtstripped:
        #Élia Cristina Viegas Pedro :: epedro@ccdr-alg.pt :: ent_CCDR-Alg :: 1 :: 0
        
        n = re.findall(r'^([^:]+)',line)
        #n devolve ['nome']

        l = re.findall(r'\bent_.*?(?::)',line)
        #devolve ['ent']

        for s in n:
            lista3.append(s)

        #retirar : das strings

        for s in l:
            s = s.replace(" ","")
            lista2.append(s.replace(":",""))

        #tenho entidates aqui - #newlist 

    lista1 = list(zip(lista3,lista2))
    #dar sort normal
    listasorted = sorted(lista1,key=lambda x:x[0])
    #dar sort para casos de acentos e maiusculas

    #função para 
    def custom_sort(item):
        return unidecode(item[0].lower())

    listafinal = sorted(listasorted, key=custom_sort)

    for i in listafinal:
        print(i)
        
def segundo():
    listafinal =[]
    
    lista2 = []
    l = abrirficheiro(path)
    txtstripped = l.split("\n")

    for line in txtstripped:

        l = re.findall(r'\bent_.*?(?::)',line)
        for s in l:
            s = s.replace(" ","")
            lista2.append(s.replace(":",""))

    dict = {}

    #print(lista2)
    for i in lista2:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    for i,j in dict.items():
        print(f"Key: {i}, value: {j}")

def terceiro():

    #Élia Cristina Viegas Pedro :: epedro@ccdr-alg.pt :: ent_CCDR-Alg :: 1 :: 0

    l = abrirficheiro(path)
    txtstripped = l.split("\n")

    desviolista = []
    somatotal = 0
    #numero de linhas aka numero de pessoas
    numero = len(txtstripped)

    for i in txtstripped[:-1]:

        

        linha = i.split("::")
        

        #print(linha)
    
        n = float(linha[3].strip())
        #print(n)
        somatotal = somatotal + n
        desviolista.append(n)
        
    print(f"soma = {somatotal}")
    print(f"n = {numero}")
    print(desviolista)          

    #calculo desvio padrao
    desvio_populacional = np.std(desviolista)
    desvio_amostral = np.std(desviolista, ddof=1)

    #media
    media = somatotal / numero

    #calculo 
    valor = 1.5 #random one
    probabilidade = norm(loc = media,scale=desvio_populacional).pdf(valor)

    print(f"Distribuição: {probabilidade}, média: {media}")

#4:Produz uma listagem dos utilizadores, agrupados por entidade, ordenada primeiro pela entidade e dentro desta pelo nome
#Élia Cristina Viegas Pedro :: epedro@ccdr-alg.pt :: ent_CCDR-Alg :: 1 :: 0

def quarto():

    l = abrirficheiro(path)
    txtstripped = l.split("\n")

    dicionario= {}

    for i in txtstripped[:-1]:

        linha = i.split("::")

        if linha[2] not in dicionario:

            dicionario[linha[2]]=[linha[0]]
        else: 
            dicionario[linha[2]].append(linha[0])

    #print(dict)
    #sort by key and lists inside

    sorteddict = dict(sorted(dicionario.items()))

    for key, value in sorteddict.items():
        sorteddict[key]= sorted(value)

    for key,value in sorteddict.items():
        print(f"Key: {key}, value: {value}")


"""
5:Por fim, produz os seguintes indicadores:
1. Quantos utilizadores?
2. Quantas entidades?
3. Qual a distribuição em número por entidade?
4. Qual a distribuição em número por nível?

"""

def quinto():

    l = abrirficheiro(path)
    txtstripped = l.split("\n")
    soma = 0
    listautilizadores = []
    listaentidade = []
    for i in txtstripped[:-1]:
        
        linha = i.split("::")
        if linha[0] not in listautilizadores:

            listautilizadores.append(linha[0])

        if linha[2] not in listaentidade:
            listaentidade.append(linha[2])


    utilizadores = len(listautilizadores)
    entidades = len(listaentidade)
    return utilizadores, entidades

def interface():

    b, d = quinto()

    while True:
        print("\nMenu:")
        print("1. Utilizadores")
        print("2. Entidades")
        print("3. exiting...")

        choice = input("Between 1 and 2 press: ")
        if choice == '1':
            print(b)
        elif choice == '2':
            print(d)
        elif choice == '3':
            print("bye bye")
            break
        else: 
            print("invalid, do another")



def jason():
    
    l = abrirficheiro(path)
    txtstripped = l.split("\n")

    #tenho as 10 primeiras strings
    selet = txtstripped[:10]
    #print(selet)
    list = []
    

    for i in selet:
        
        #print(i)
        
        dict= {}
        b = i.split("::")
        #print(b[])
        #print(i[0]
           
        dict["Name"] = b[0]
        dict["Mail"] = b[1]
        dict["Entity"] = b[2]
        dict["Nível"] = b[3]
        dict["Backend"] = b[4]

        list.append(dict)
        
    #list tem uma lista de dicts
    pathh = 'C:\\Users\\filip\\Desktop\\'

    
    final = json.dumps(list, indent=2)
    print(final)



jason()