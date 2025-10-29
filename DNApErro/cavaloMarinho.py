class CavaloMarinho:
    contador = 0
    def __init__(self,sexo):
        CavaloMarinho.contador += 1
        self.nome = CavaloMarinho.contador
        self.sexo = sexo
        self.forcaCalda = []
        self.camuflagem = []
        self.estruturaCorporal = []
        
    def caracteristicas(self,op:int):
        if op == 1:
            return self.forcaCalda
        elif op == 2:
            return self.camuflagem
        elif op == 3:
            
            return self.estruturaCorporal
    
    def prenche(self,op: int, lis):
        if op == 1:
            self.forcaCalda = lis 
        elif op == 2:
            self.camuflagem = lis
        else:
            self.estruturaCorporal = lis