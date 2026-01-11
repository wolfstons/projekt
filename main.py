import bevezetes
import sorozat
import epuletek

bevezetes.varazslo()
lista=sorozat.sor()
fej=sorozat.szamolas(lista)
sorozat.fajlba_ir(fej)
ep=epuletek.beolvasas()
epuletek.epuletek_szama(ep)
epuletek.magas_epulet(ep)
epuletek.oreg(ep)