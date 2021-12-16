import pandas as pd

data = pd.read_csv("/home/maison/ProjetGit/tirrageSort/liste_apprenants.csv")

# Group 1




# Group 2

def Tirage2(data):
    data_without_prof = data.loc[data["Prof"]!=1].reset_index(drop=True)
    df = data_without_prof['Prénom'].sample(n=len(data_without_prof)).reset_index(drop=True)
    df1ip =df.iloc[::2].reset_index()
    df1p=df = df.iloc[1::2].reset_index()
    res = pd.concat([df1p,df1ip],axis =1,ignore_index=True)
    resultat = res[[1,3]]
    return(resultat)


# Group 3



# Group 4




# Programme principal

d = Tirage2(data)
print(d)
'''df = Tirage3()
print(df)
df = Tirage4()
print(df)
df = Tirage5()
print(df)'''
