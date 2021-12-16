import pandas as pd


# Group 1




# Group 2
fichier = "liste_apprenants.csv"
df = pd.read_csv(fichier)

dfa = df[df.Prof==0]
dfa.describe()
listt= dfa["Prénom"].tolist()

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
