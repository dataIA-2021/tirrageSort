import pandas as pd
import random


# Group 1




# Group 2
data = pd.read_csv("liste_apprenants.csv")

def Tirage2(data):
    data_without_prof = data.loc[data["Prof"]!=1].reset_index(drop=True)
    df = data_without_prof['Prénom'].sample(n=len(data_without_prof)).reset_index(drop=True)
    df1ip =df.iloc[::2].reset_index()
    df1p=df = df.iloc[1::2].reset_index()
    res = pd.concat([df1p,df1ip],axis =1,ignore_index=True)
    resultat = res[[1,3]]
    return(resultat)

# Group 3
def Tirage3():
    #Renvoie un dataframe contenant des groupes de 3 personnes

    fichier = "liste_apprenants.csv"
    df = pd.read_csv(fichier)
    dfa = df[df.Prof==0]
    L = dfa["Prénom"].tolist()

    Tirage=[[],[],[]]
    N = len(L)
    
    for k in range(N):
        
        r = round(random.random()*(N-k)-1)
        
        if k%3 == 0 :
            Tirage[0].append(L[r])
            
        elif k%3 == 1:
            Tirage[1].append(L[r])
            
        elif k%3 == 2:
            Tirage[2].append(L[r])
            
        L.pop(r)
        
        
    Tirage = pd.DataFrame(Tirage)
    return(pd.DataFrame.transpose(Tirage))
# Group 3


file_location = 'liste_apprenants.csv'
df = pd.read_csv(file_location)
df = df[df.Prof==0]
df= pd.DataFrame(df['Prénom']).reset_index()
dictionaire = dict(df.values)


def Tirage42():
    file_location = 'liste_apprenants.csv'
    df = pd.read_csv(file_location)
    df = df[df.Prof==0]
    df= pd.DataFrame(df['Prénom']).reset_index()
    dictionaire = dict(df.values)
    listgroup = []
    for it in Tirage4(dictionaire):
        listgroup.append(it)
        df = pd.DataFrame(listgroup)
    return df

# Grouper par 4, size
# Liste des index, keys
# Mélange ordre des index, shuffle
# Boucle sur les keys en focntion de la size
# yield à la place de return, pour afficher tous les groupes sans les répéter

def Tirage4(d, size=4):
    "Demande un dictionnaire et un int size retourne une liste de tableau contenant les membre d'un group"
    keys = list(d.keys())
    random.shuffle(keys)
    
    for i in range(0, len(keys), size): #On prend les i par groupe de size
         yield [d[key] for key in keys[i:i + size]] # On prend les gens de i à i+size, le yield retourne un groupe à la fois
    









# Group 4
def Tirage5():
    df = pd.read_csv('liste_apprenants.csv')
    
    #etudiants = df.iloc[4:20,0]
    etudiants = df.iloc[:, 0]
    
    def selectRandom(names):
        return numpy.random.choice(names,1)
    
    # On melange notre dataframe
    L = etudiants.tolist()
    random.shuffle(L)
    
    
    liste1 = []
    liste2 = []
    liste3 = []
    
    cpt = 1
    
    for i in L:
        if cpt <= 5:
            liste1.append(i)
        elif cpt > 5 and cpt <= 10:
            liste2.append(i)
        else:
            liste3.append(i)
    
        cpt = cpt + 1
        
    print('liste1',liste1)
    print('liste2',liste2)
    print('liste3',liste3)
    
    new_df = pd.DataFrame({'Colonne 1':[liste1[0], liste2[0], liste3[0]],
                           'Colonne 2':[liste1[1], liste2[1], liste3[1]],
                           'Colonne 3':[liste1[2], liste2[2], liste3[2]],
                           'Colonne 4':[liste1[3], liste2[3], liste3[3]],
                           'Colonne 5':[liste1[4], liste2[4], liste3[4]],
                           'Colonne 6':[liste3[5], None, None]})
    
    return new_df




# Programme principal

'''d = Tirage2(data)
print(d)
print('-------------------------------------')
'''
df = Tirage42()
print(df)
print('-------------------------------------')

for group in Tirage4(dictionaire):
    print(group)
#print(df)
'''
print('-------------------------------------')
df = Tirage5()
print(df)
print('-------------------------------------')
'''