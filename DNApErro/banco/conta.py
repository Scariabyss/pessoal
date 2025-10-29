class Conta:
    def __init__(self,numero:str,nome:str,saldo:float):
        self.__numero = numero
        self.__titular =  nome
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        partesNomes = self.__titular.split(" ")
        tamanho = len(partesNomes)
        return partesNomes[0] +" "+partesNomes[tamanho-1]

    @titular.setter
    def titular(self,itu):
        self.__titular = itu

    @saldo.setter
    def saldo(self,sal):
        if sal< 0:
            print("Não foi possivel alterar o slado! >=/")
        else:
            self.__saldo = sal

    def depositar(self,valor:float):
        if valor <0:
            print("Não foi possível realizar esse depósito! =(")
        else:
            self.__saldo += valor
    


    def sacar(self,valor:float) -> bool:
        if valor > self.__saldo:
            print("Não foi possível sacar esse valor! >=(")
        else:
            self.__saldo -= valor



class ContaCorrente(Conta):

    contador = 0

    def __init__(self,numero,nome,valor):
        super().__init__(numero,nome,valor)
        self.__limite = 5000
        ContaCorrente.contador +=1

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self,novo):
        if novo < 0:
            print("Não foi possível alterar o limite! >=(")
        else:
            self.__limite = novo
    
    def saldoTotal(self):
        return self.saldo + self.__limite
    
    
    def sacar(self,valor:float) -> bool:
        if valor > self.saldoTotal():
            print("Não foi possível sacar esse valor! =(")
        else:
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                self.limite -= valor - self.saldo
                self.saldo = 0
                


class ContaPouopanca(Conta):
    def __init__(self,numero,nome,valor,rendimento):
        super().__init__(numero,nome,valor)
        self.__rendimento = rendimento

    
    @property
    def rendimento(self):
        return self.__rendimento
    
    
    @rendimento.setter
    def limite(self,limite):
        if limite < 0:
            print("Não foi possível alterar a taxa de rendimento! >=(")
        else:
            self.__rendimento = limite

    def acaoRendimento(self):
        self.saldo = self.saldo * self.__rendimento