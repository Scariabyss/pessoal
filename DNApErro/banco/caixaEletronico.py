from conta import *

if __name__ == "__main__":
    print("\U0001F446")
    
    minhaConta = ContaCorrente("16883-5","Moisés Henrique Ramos Pereira",2500.18)
    print("Saldo de ",minhaConta," = "+str(minhaConta.saldo))
    print(f"Saldo simples de {minhaConta.titular} = {minhaConta.saldo}")
    print(f"Saldo total de {minhaConta.titular} = {minhaConta.saldoTotal()}")
    minhaConta.limite = 5000
    print(f"Saldo simples de {minhaConta.titular} = {minhaConta.saldoTotal()}")
    minhaConta.sacar(1000)
    print(f"Saldo simples de {minhaConta.titular} = {minhaConta.saldo:.2f}")
    print(f"Saldo total de {minhaConta.titular} = {minhaConta.saldoTotal()}")
    outraConta = ContaCorrente("17777-9","Zé Cebola", 5000.33)
    print(ContaCorrente.contador)
    outraContaDenovo = ContaCorrente("33355-3","Teste", 500.50)
    print(ContaCorrente.contador)