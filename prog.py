import pandas as pd


# Group 1




# Group 2
from random import*
import numpy as np

def Tirage3():
    #Renvoie un dataframe contenant des groupes de 3 personnes

    fichier = "liste_apprenants.csv"
    df = pd.read_csv(fichier)
    dfa = df[df.Prof==0]
    L = dfa["Prénom"].tolist()

    Tirage=[[],[],[]]
   
    
    N = len(L)
    
    for k in range(N):
        r = round(random()*(N-k)-1)
        if k%3 == 0 :
            Tirage[0].append(L[r])
        elif k%3 == 1:
            Tirage[1].append(L[r])
        elif k%3 == 2:
            Tirage[2].append(L[r])
        L.pop(r)
    Tirage = np.transpose(Tirage)
    return(pd.DataFrame(Tirage))
# Group 3



# Group 4




# Programme principal

# df = Tirage2()
# print(df)
df = Tirage3()
print(df)
# df = Tirage4()
# print(df)
# df = Tirage5()
# print(df)
