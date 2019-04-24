"""
Algoritmo simulando autômato de pilha para palavras palíndromes
@author: Alexandre Pereira, José victor, Michelle Moura
"""
def Arvore(pilha,palavra,b):
    for c in range(b+1,len(palavra)):
        if palavra[c] == pilha[len(pilha)-1]:
            pilha.pop()
            print(pilha,c)
            if c == (len(palavra)-1):
                if pilha[len(pilha)-1]=='#': return True
    return False

while True:
    palavra = str(input("Digite a Palavra que deseja Testar: ")).lower()
    if palavra =='':
        break
    pilha=['#']
    for i in range(0,(len(palavra)-1)):
        pilha.append(palavra[i])
        pilhaCopy = pilha[:]
        if Arvore(pilhaCopy[:],palavra,i):
            print("Palavra Aceita")
            pilha[0] ='aceito'
            break
    if pilha[0]!='aceito':
        print("Palavra não Aceita")