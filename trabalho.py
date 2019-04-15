# -*- coding: utf-8 -*-
"""
@author: Alexandre
"""

class Pilha:
     def __init__(self):
         self.pilha = []
     def Vazio(self):
         return self.pilha == []
     def Push(self, item):
         self.pilha.append(item)
     def Pop(self):
         return self.pilha.pop()
     def Topo(self):
         return self.pilha[len(self.pilha)-1]
     def Tamanho(self):
         return len(self.pilha)
class Automato:
    def __init__(self):
       Estados = []
       EstadoInicial = None
       EstadosFinais= []
       Alfabeto = []
       AlfabetoPilha=[]
       Epslon = ''
       PilhaAutomato = Pilha()
       Regras = {}
       EstadoAtual = None
    def SetEstado(self,estado):
        self.Estados.append(estado)
        if self.EstadoInicial==None:
            self.EstadoInicial = estado
            self.EstadoAtual = estado
            PilhaAutomato.Push('&')
    
    def SetEstadoFinal(self,estado):
        self.EstadosFinais.append(estado)
        
    def SetAlfabeto(self,item):
        self.Alfabeto.append(item)
        
    def SetAlfabetoPilha(self,item):
        self.AlfabetoPilha.append(item)
    def SetEpslon(self,item):
        self.Epslon = item
    #exemplo de regra:q ->s,d,a
    def SetRegra(self,regra):
        [estado,regra] = regra.split('->')
        self.regras[estado] = regra.split(',')
    def Verfifica(self,palavra):
        for i in range(0,len(palavra))
        if PilhaAutomato.Tamanho==0:
            return True 
        if EstadoAtual == EstadoInicial:
            simbolo = palavra[i]
            reg = Regras[EstadoAtual]
           #verificando se existe mais de um caminho para esse nó
            if len(reg)>4:
                for i in range(0,len(reg)):
                    if i%4==0:
                        if reg[i]==palavra[i]:
                            [simbolo,topo,adicionar,proximo]=palavra[i],palavra[i+1],palavra[i+2],palavra[i+3]
                            break
            else:
                [simbolo,topo,adicionar,proximo]=reg
            
                
                            
'''
def check(self, w, g=''):
        if g == '':
            g = self.start
        if len(g) > len(w):
            return False
        print(">>> " + g)

        variables = [x for x in g if x.isupper()]
        if len(variables) == 0:
            return w == g

        c = variables[0]
        for r in self.rules[c]:
            gg = g.replace(c, r, 1)
            if self.check(w, gg):
                return True
        return False


G = Grammar()

while True:
    line = input()
    if line == '':
        break
    G.add_rule(line)

while True:
    w = input()
    if w == '':
        break
    if G.check(w):
        print('Yes')
    else:
        print('No')
dicionario={}
dicionario = {'chave':'valor'}
dicionario['teste'=10
'''