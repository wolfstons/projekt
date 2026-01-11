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


def epuletek_szama(ep):
    szama=len(ep.nev)
    print(f"Az épületek száma: {szama}")


def magas_epulet(ep):
    max_mag=169.16
    i=0
    db=0
    while i<len(ep.mag):
        if int(ep.mag[i])>max_mag:
            db+=1
        i+=1
    print(f"Az 555 lábbnál magasabb épületek száma: {db}")

def oreg(ep):
    i=0
    kor=2026
    index=0
    while i<len(ep.ev):
        if ep.ev[i]>kor:
            kor=ep.ev[i]
            index=i
        i+=1
    print(f"A legöregebb épület országa: {ep.orszag[index]}")