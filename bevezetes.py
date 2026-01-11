def varazslo():
    nev=input("Játékos neve: ")
    szerepkör=input("szerekör: ")
    if szerepkör=="varázsló":
        print(f"Üdvözöllek {nev}, 2 életed van!")
    if szerepkör=="harcos":
        print(f"Üdvözöllek {nev}, 10 életed van!")
    else:
        print(f"Üdvözöllek {nev}, 8 életed van!")