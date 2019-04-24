# -*- coding: utf-8 -*-
"""
@grupo: Alexandre,kosé victor, michelle moura
"""
class Pilha:
     def __init__(self):
         self.pilha = []
     def Vazio(self):
         return self.pilha ==[]
     def Push(self, item):
         self.pilha.append(item)
     def Pop(self):
         return self.pilha.pop()
     def Topo(self):
         if len(self.pilha) == 0:
          return None
         return self.pilha[len(self.pilha)-1]
     def Tamanho(self):
         return len(self.pilha)
     def CopiaPilha(self):
         return self.pilha[:]
     def LimpaPilha(self):
         self.pilha=[]
     def ReescrevendoPilha(self,pilhaCopy):
         self.pilha = pilhaCopy[:]

class Automato:
    def __init__(self):
       self.Estados = []
       self.EstadoInicial = None
       self.EstadosFinais= []
       self.Alfabeto = []
       self.AlfabetoPilha=[]
       self.Epslon = '&'
       self.PilhaAutomato=Pilha()
       self.Regras = {}
       self.EstadoAtual = None

    def SetEstado(self,estado):
        self.Estados.append(estado)
        self.Regras[estado] = []
        if self.EstadoInicial==None:
            self.EstadoInicial = estado
            self.EstadoAtual = estado
            self.PilhaAutomato.Push('#')
    
    def SetEstadoFinal(self,estado):
        self.EstadosFinais.append(estado)
        
    def SetAlfabeto(self,item):
        self.Alfabeto.append(item)
        
    def SetAlfabetoPilha(self,item):
        self.AlfabetoPilha.append(item)
        
    def SetEpslon(self,item):
        self.Epslon = item
        
    #exemplo de regra:q ->s,d,a
    def SetRegra(self,reg):
        [estado,regra] = reg.split('->')
        self.Regras[estado] += regra.split(',')
        print(estado, self.Regras[estado])
        
    def Verfifica(self,palavra,p):
      
       # print("{} {} {}".format(self.EstadoAtual, p, self.PilhaAutomato.pilha))
        
        if (self.PilhaAutomato.Topo()=='#'
            and self.EstadoAtual in self.EstadosFinais
            and p == len(palavra)):
            return True
          
        for b in range(0,len(self.Regras[self.EstadoAtual]),4):
            copiaP = p
            copiaEstado = self.EstadoAtual
            copiaPilha =self.PilhaAutomato.CopiaPilha()

            simbolo = self.Regras[self.EstadoAtual][b]
            topo = self.Regras[self.EstadoAtual][b+1]
            adiciona = self.Regras[self.EstadoAtual][b+2]
            proxEstado = self.Regras[self.EstadoAtual][b+3]
            
           #s print(simbolo, topo, adiciona, proxEstado)

            if topo == self.Epslon:
              if adiciona == self.Epslon:
                if self.EstadoAtual == proxEstado:
                  continue
              else:
                self.PilhaAutomato.Push(adiciona)                  
            else:
              if self.PilhaAutomato.Topo() is None or self.PilhaAutomato.Topo() != topo:
                continue
              self.PilhaAutomato.Pop()

            if simbolo != self.Epslon:
              if p == len(palavra) or simbolo != palavra[p]:
                self.EstadoAtual = copiaEstado
                self.PilhaAutomato.ReescrevendoPilha(copiaPilha)
                continue
              p += 1


            self.EstadoAtual = proxEstado
            if self.Verfifica(palavra,p):
              return True

            p = copiaP
            self.EstadoAtual = copiaEstado
            self.PilhaAutomato.ReescrevendoPilha(copiaPilha)
                
        return False
      
    def ValidaPalavra(self,palavra):
        for a in palavra:
            if a not in self.Alfabeto:
                return False
        return True

AutomatoTeste = Automato()
AutomatoTeste.SetEstado("q0")
AutomatoTeste.SetEstado("q1")
AutomatoTeste.SetEstado("q2")
AutomatoTeste.SetEstadoFinal("q2")
AutomatoTeste.SetAlfabeto("1")
AutomatoTeste.SetAlfabeto("2")
AutomatoTeste.SetAlfabetoPilha("1")
AutomatoTeste.SetAlfabetoPilha("2")
AutomatoTeste.SetRegra("q0->1,&,1,q0")
AutomatoTeste.SetRegra("q0->2,&,2,q0")
AutomatoTeste.SetRegra("q0->&,&,&,q1")
AutomatoTeste.SetRegra("q1->1,1,&,q1")
AutomatoTeste.SetRegra("q1->2,2,&,q1")
AutomatoTeste.SetRegra("q1->&,&,&,q2")

while True:
    palavra = input("Digite a Palavra de deseja Testar: ")
    if palavra == '':
        break
    if not AutomatoTeste.ValidaPalavra(palavra):
        print("Palavra não Aceita")
    elif AutomatoTeste.Verfifica(palavra,0):
       print("Palavra Aceita")
    else:
        print("Palavra não Aceita")