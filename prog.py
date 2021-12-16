import pandas as pd


# Group 1




# Group 2


# Group 3


# In[223]:


import pandas as pd
import random


# In[231]:


file_location = 'liste_apprenants.csv'
df = pd.read_csv(file_location)
df


# In[232]:


df.drop([0,1,2,3],0,inplace=True)


# In[233]:


df


# In[234]:


df1= pd.DataFrame(df[['Prénom','Nom']])

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

def random_group(d, size=4):
    keys = list(d.keys())
    random.shuffle(keys)
    for i in range(0, len(keys), size):
         yield [d[key] for key in keys[i:i + size]]
            

for group in random_group(dictionaire):
    print(group)







# Group 4




# Programme principal

