import pandas as pd

# Group 1




# Group 2
import random

fichier = "liste_apprenants.csv"
df = pd.read_csv(fichier)

dfa = df[df.Prof==0]
dfa.describe()
listt= dfa["Prénom"].tolist()
listt.append("Louis")

a = round(len(listt)/3)+1

for i in range (a):
    groupe = []
    for c in range(3):
        x = random.choice(listt)
        listt.remove(x)
        groupe.append(str(i+1)+" "+x)
        if len(listt)==0:
            break
    print(groupe)

# groupe = pd.DataFrame(Tirage)
        
        

# for r in range (df):
    
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
