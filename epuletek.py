from Epulet import Epulet
def beolvasas():
    f=open("epulet.txt","r",encoding="utf-8")
    f.readline()
    sorok=f.readlines()
    f.close()
    i=0
    while i<len(sorok):
        sor=sorok[i].strip().split("$")
        ep=Epulet(sor[1],sor[2],sor[3],sor[4],sor[5],sor[6],)
        i+=1
    return ep
    