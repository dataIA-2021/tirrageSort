import pandas as pd


# Group 1




# Group 2
from random import*

def Tirage3():
    #Renvoie un dataframe contenant des groupes de 3 personnes

    fichier = "liste_apprenants.csv"
    df = pd.read_csv(fichier)
    dfa = df[df.Prof==0]
    
    Grp = 3 
    Tirage=[]
    
    for k in range (Grp):
        Tirage.append([])
    
    L=["Marceline","Steve","Victorien","Jeremy","Eric","Clara","César","Tim","Alexia","Noli","Tess","Célia","François","Louis","Sylvain","Kyllian"]
    N = 16
    
    for k in range(N):
        r = round(random()*(N-k)-1)
        if k%3 == 0 :
            Tirage[0].append(L[r])
        elif k%3 == 1:
            Tirage[1].append(L[r])
        elif k%3 == 2:
            Tirage[2].append(L[r])
        L.pop(r)
    
    return(pd.DataFrame(Tirage))
# Group 3



# Group 4




# Programme principal

# df = Tirage2()
# print(df)
# df = Tirage3()
# print(df)
# df = Tirage4()
# print(df)
# df = Tirage5()
# print(df)
