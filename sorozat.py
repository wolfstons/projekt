
import random


def sor():
    lista=[]
    i=0
    while i<6:
        szam=random.randint(0,1)
        lista.append(szam)
        if lista[i]==0:
            print("fej",end="-")
        else:
            print("íras",end="-")
        i+=1
    szam=random.randint(0,1)
    lista.append(szam)
    if lista[6]==0:
        print("fej",end="\n")
    else:
        print("íras",end="\n")
    return lista

def szamolas(lista):
    i=0
    fej=0
    while i<len(lista):
        if lista[i]==0:
            fej+=1
        i+=1
    print(f"A fejeke száma: {fej}")
    return fej

def fajlba_ir(fej):
    with open("fejek.txt","w",encoding="utf-8") as f:
        f.write(f"A fejek száma: {fej}")
