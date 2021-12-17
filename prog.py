import pandas as pd
import random
import numpy


# Group 1




# Group 2
data = pd.read_csv("liste_apprenants.csv")

def Tirage2(data):
    """

    Retourne une dataframe à 2 tirages
    -------
    resultat : TYPE Dataframe
    """
    
    # Retirer les profs
    data_without_prof = data.loc[data["Prof"]!=1].reset_index(drop=True)
    
    # Melange les prenoms de la dataframe
    df = data_without_prof['Prénom'].sample(n=len(data_without_prof)).reset_index(drop=True)
   
    # Divise en 2 dataframes
    df1ip =df.iloc[::2].reset_index()

    df1p = df.iloc[1::2].reset_index()
    
    #concatanation de 2 dataFrames
    res = pd.concat([df1p,df1ip],axis =1,ignore_index=True)
    
    #garde les prénoms de la colonne 1 et 3
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


# In[223]:



# In[231]:


file_location = 'liste_apprenants.csv'
df = pd.read_csv(file_location)
df


# In[232]:


df.drop([0,1,2,3],0,inplace=True)


# In[233]:


df


# In[234]:


df1= pd.DataFrame(df[['Prénom']])

df1


# In[235]:


df= pd.DataFrame(df['Prénom']).reset_index()

df


# In[239]:


dictionaire = dict(df.values)
dictionaire


# In[240]:


# Grouper par 4, size
# Liste des index, keys
# Mélange ordre des index, shuffle
# Boucle sur les keys en focntion de la size
# yield à la place de return, pour afficher tous les groupes sans les répéter

def Tirage4(d, size=4):
    keys = list(d.keys())
    random.shuffle(keys)
    for i in range(0, len(keys), size):
         yield [d[key] for key in keys[i:i + size]]
            









# Group 4
def Tirage5():
    """

    Retourne une dataframe à 5 tirages
    -------
    new_df : TYPE Dataframe
    """
    
    # On copie le dataset pour traitement
    df = data
    
    # On retire les profs du dataset
    df = df[df.Prof == 0]
    
    # On tranforme la dataframe en liste
    students = df['Prénom'].tolist()
    
    # Melange de la liste aleatoire
    random.shuffle(students)
    
    # Tableau etudiants pour restitution dataframe
    arrayStudents = [[],[],[],[]]
    
    index = 0
    cpt = 0
    for i in range(len(students)):
        arrayStudents[index].append(students[i])
        cpt += 1
        if cpt > 4:
            index += 1
            cpt = 0
            
    new_df = pd.DataFrame(arrayStudents)

    return new_df




# Programme principal

d = Tirage2(data)
print(d)
print('-------------------------------------')
df = Tirage3()
print(df)
print('-------------------------------------')
for group in Tirage4(dictionaire):
    print(group)
print(df)
print('-------------------------------------')
df = Tirage5()
print(df)
print('-------------------------------------')
