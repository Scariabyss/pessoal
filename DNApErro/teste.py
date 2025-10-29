import time



def escrita(frase:str):
    for i in range(0,len(frase)):
        print(frase[i],end=  "",flush= True)
        time.sleep(0.3)


escrita("Isso não é legal? ;)")