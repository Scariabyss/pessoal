from cavaloMarinho import *
from random import *
import os
import time 





def geracaoIndividuo():
    individuo = CavaloMarinho(choice(["M","F"]))
    for e in range(0,3): 
       
        caracteristica = []
        for i in range(0, tamanhoCaracteristica1):
            caracteristica += [randint(1, limiteMaximoGene)]
        individuo.prenche(e+1,caracteristica)
    return individuo

def reproducaoIndividuos(par1, par2):
    individuo = CavaloMarinho(choice(["M","F"]))
    caracteristica = []

    for j in len(par1.forcaCalda):
        i = par1.forcaCalda[j]
        e = par2.forcaCalda[j]
        caracteristica += [max(i, e)]
    individuo.prenche(1,caracteristica)
    caracteristica = []
    
    for j in len(par1.camuflagem):
        i = par1.camuflagem[j]
        e = par2.camuflagem[j]
        caracteristica += [max(i, e)]
    individuo.prenche(2,caracteristica)
    caracteristica = []
    
    for j in len(par1.estruturaCorporal):
        i = par1.estruturaCorporal[j]
        e = par2.estruturaCorporal[j]
        caracteristica += [max(i, e)]
    individuo.prenche(3,caracteristica)
   
    return individuo

''''''''''''''''
def mutacaoGenetica(individuo):
    if randint(1, 100) <= valorTaxaMutacao:
        i = randint(0, tamanhoCaracteristica1 - 1)
        individuo.caracteristica1[i] = randint(1, limiteMaximoGene)
    return individuo

def avaliacaoPopulacao(populacao):
    adaptado = 0
    for individuo in populacao:
        somatorio = sum(individuo.caracteristica1)
        if somatorio > adaptado:
            adaptado = somatorio
    return adaptado * (valorTaxaSelecao / 100)
'''''''''
cores = ["\33[1;34m","\33[1;39m"]

print(f"{cores[0]}\\\\\\\\\\ Codigo da teoria da eveloção (seleção natural) //////////")
print(f"\n||||| Cavalo Marinho (Hippocampus coronatus) |||||{cores[1]}\n")
time.sleep(1)


limiteMaximoGene = 2400
tamanhoPopulacao = int(input("\nQuantos individuos na população você quer? "))
tamanhoCaracteristica1 = 10
valorTaxaMutacao = float(input("\nQual é a taxa de mutação em % você quer? "))
valorTaxaSelecao = 80
anos = int(input("\nQuantas gerações você deseja? "))


populacao = [geracaoIndividuo() for i in range(0, tamanhoPopulacao)]
popnewage = []
for l in range(0,anos): 
    print(l)
    time.sleep(1)
    populacao = popnewage
    popnewage = []
    for i in range(0, len(populacao) - 1):
        par1 = populacao[i]
        par2 = populacao[i+1]
        ind3 = reproducaoIndividuos(par1, par2)
        #ind3 = mutacaoGenetica(ind3)
        #if sum(ind3.caracteristica1) >= avaliacaoPopulacao(populacao):
        popnewage += [ind3]

    for individuo in populacao:
        print(f"{individuo.nome} - {individuo.sexo}")
        for e in range(0,3):
            
            print(f"Característica {e}: {individuo.caracteristicas(e+1)}")
        
            
        
    print()

    for individuo in popnewage:
        print(f"{individuo.nome} - {individuo.sexo}")
        for e in range(0,3): 
            print(f"Característica {e}: {individuo.caracteristicas(e+1)}")
