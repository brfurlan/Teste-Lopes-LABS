
# coding: utf-8

# <h1 align="center">  Desafio Lopes LABS </h1>
# 
# <h2 align="right"> Bruno Ramalho Furlan </h2>

# **Objetivo:** Criar um modelo para estimar a qualidade do vinho.

# <h3 align="justified">Importando dados </h3>
# 
# <p align="justified"> Verificando tipo de dados para cada coluna e quantidade de linhas e colunas </p>

# In[1]:


import csv
import pandas as pd


df = pd.read_csv("winequality.csv", sep=";")
df.head(1000)


# In[2]:


print(df.shape)


# In[3]:


print(df.info())


# <p align="justified"> Foi verificado que o tipo da coluna com a variavel álcool ("alcohol") está como object e não como float. Para isso foi realizada a alteração do tipo de coluna para float.</p>

# In[4]:


df["alcohol"] = pd.to_numeric(df["alcohol"], errors="coerce")


# In[5]:


df.info()


# <h3 align="justified">Eliminando duplicatas e linhas com valores nulos </h3>
# <p align="justified"> 
# Eliminando dados duplicados ou que não apresentam valores em todas as colunas para uma estimação do modelo a partir de todos os parâmetros.</p>

# In[6]:


import numpy as np
df = df.drop_duplicates()
df = df.dropna(how='any',axis=0) 
df.info()


# <h3 align="justified">Verificando a correlação dos dados com a qualidade do vinho (método de Pearson)</h3>
# 
# 

# In[7]:


df.corrwith(df["quality"], axis=0, drop=False, method='pearson')


# <p align="justified">As 3 variáveis que apresentam maior correlação encontradas foram:</p>
#     
# 1. Álcool ("alcohol"), correlação positiva (0.469674); 
# 2. Volatilidade da acidez ("volatile acidity"), correlação negativa (-0.266608);
# 3. Cloretos ("chlorides"), correlação negativa (-0.201844);
# 
# <p align="justified">Estas 3 variáveis apresentaram correlação fraca, as demais apresentaram correlação inferior, em módulo, a 0,1.</p> 
# <p align="justified">Para fins de comparação, feitas as correlações utilizando outros 2 métodos de correlação (Spearman e Kendall), sendo selecionadas  as 3 maiores correlações em módulo.</p>
#     
#      

# <h3 align="justified">Verificando a correlação dos dados com a qualidade do vinho (método de Spearman)</h3>
# 

# In[8]:


df.corrwith(df["quality"], axis=0, drop=False, method='spearman')


# <p align="justified">As 3 variáveis que apresentam maior correlação encontradas foram:</p>
#     
# 1. Álcool ("alcohol"), correlação positiva (0.479853); 
# 2. Densidade ("density"), correlação negativa (-0.349593);
# 3. Cloretos ("chlorides"), correlação negativa (-0.303533);
# 
# 
#     

# <h3 align="justified">Verificando a correlação dos dados com a qualidade do vinho (método de Kendall)</h3>
# 

# In[9]:


df.corrwith(df["quality"], axis=0, drop=False, method='kendall')


# <p align="justified">As 3 variáveis que apresentam maior correlação encontradas foram:</p>
#     
# 1. Álcool ("alcohol"), correlação positiva (0.377853); 
# 2. Densidade ("density"), correlação negativa (-0.268305);
# 3. Cloretos ("chlorides"), correlação negativa (-0.235499);
# 
# <p align="justified">Estas 3 variáveis apresentaram correlação fraca, as demais apresentaram correlação despresível (inferior, em módulo a 0,1).</p>
# <p align="justified">Como o método de Kendall apresentou menor correlação das variáveis em comparação com os outros métodos, especialmente na variável álcool (que apresenta menor correlação em comparação com os demais métodos). Este não será utilizado na modelagem da qualidade. Assim ,serão comarados os métodos de Spearman e Pearson.</p>

# <h3 align="justified">Verificando dados para a modelagem </h3>
# 

# In[10]:


df.describe()


# <p align="justified"> Para para a modelagem nos dois métodos foram utilizados os valores máximo e mínimo das seguintes variáveis, além da variável de qualidade (utilizada para validar o modelo):</p>
# 
# 1. Álcool;
# 2. Volatilidade da acidez;
# 3. Cloretos;
# 4. Densidade;
#    
#     
# <p align="justified"> Para o método de Pearson foram utilizadas as variáveis álcool, volatilidade de acidez e cloretos enquanto que para o método de Spearman foram utilizadas as variáveis álcool, densidade e cloretos. para cada uma destas variáveis, foram dados conceitos de qualidade de 0 a 10 (para correlação positiva) e de 10 a 0 (para correlação negativa). Como o valor máximo de qualidade encontrado foi de 9 e o mínimo foi de 3, foram feitos os seguintes métodos para a estimação dos conceitos das variáveis:</p>
# 
# 
# * Foi feita a subtração do menor valor para o maior valor de cada uma das váriáveis, pelo menor valor e este foi dividido por 6 (intervalo entre o maior e o menor valor da variável qualidade) para determinar o tamanho do intervalo de dados que receberia cada conceito;
# * Com o tamanho do intervalo de dados para cada variável, foram feitas as divisões de intervalos para variável e atribuidos conceitos para cada variável:de 3 a 9 para correlações positivas e de 9 a 3 para correlações negativas;
# * Com a utilização de cada intervalo de dados, foram estimados os possíveis intervalos para os conceitos de 0,1,2,3 e 10;
# 
# 
# <p align="justified">Assim, voram estimados os seguintes intervalos e conceitos para cada variável</p>
# 
# 1. Álcool;
# 
# | Intervalo |       | Conceito |
# |-----------|-------|----------|
# | Início    | Fim   |          |
# | 0         | 5,7   | 0        |
# | 5,7       | 6,85  | 1        |
# | 6,85      | 8     | 2        |
# | 8         | 9,15  | 3        |
# | 9,15      | 10,3  | 4        |
# | 10,3      | 11,45 | 5        |
# | 11,45     | 12,6  | 6        |
# | 12,6      | 13,75 | 7        |
# | 13,75     | 14,9  | 8        |
# | 14,9      | 16,05 | 9        |
# | <= 16,05  |       | 10       |
# 
# 2. Volatilidade da acidez;
# 
# | Intervalo |      | Conceito |
# |-----------|------|----------|
# | Início    | Fim  |          |
# | 0         | 0,08 | 10       |
# | 0,08      | 0,33 | 9        |
# | 0,33      | 0,58 | 8        |
# | 0,58      | 0,83 | 7        |
# | 0,83      | 1,08 | 6        |
# | 1,08      | 1,33 | 5        |
# | 1,33      | 1,58 | 4        |
# | 1,58      | 1,83 | 3        |
# | 1,83      | 2,08 | 2        |
# | 2,08      | 2,33 | 1        |
# | <= 2,33   |      | 0        |
# 
# 3. Cloretos;
# 
# | Intervalo |        | Conceito |
# |-----------|--------|----------|
# | Início    | Fim    |          |
# | 0,0000    | 0,0090 | 10       |
# | 0,0090    | 0,1093 | 9        |
# | 0,1093    | 0,2097 | 8        |
# | 0,2097    | 0,3100 | 7        |
# | 0,3100    | 0,4103 | 6        |
# | 0,4103    | 0,5107 | 5        |
# | 0,5107    | 0,6110 | 4        |
# | 0,6110    | 0,7113 | 3        |
# | 0,7113    | 0,8117 | 2        |
# | 0,8117    | 0,9120 | 1        |
# | <= 0,9120 |        | 0        |
# 
# 4. Densidade;
# 
# | Intervalo |          | Conceito |
# |-----------|----------|----------|
# | Início    | Fim      |          |
# | 0,0000    | 0,9871   | 10       |
# | 0,9871    | 18,1389  | 9        |
# | 18,1389   | 35,2907  | 8        |
# | 35,2907   | 52,4426  | 7        |
# | 52,4426   | 69,5944  | 6        |
# | 69,5944   | 86,7462  | 5        |
# | 86,7462   | 103,8980 | 4        |
# | 103,8980  | 121,0498 | 3        |
# | 121,0498  | 138,2016 | 2        |
# | 138,2016  | 155,3534 | 1        |
# | <= 155,353|          | 0        |
# 
# 
# <p align="justified">* O final de cada intervalo é aberto</p>
# <p align="justified"> Em seguida, é feita uma cópia do banco de dados para cada método, sendo calculados os conceitos para cada variável em cada vinho, sendo também feita as sua qualidade estimada. O cálculo da qualidade estimada, é feito  pela média ponderada, multiplicando cada conceito de cada variável pelo módulo da correlação da mesma e dividindo pela soma do módulo das correlações. </p>
# 
# <p align="justified"> O erro de estimação também foi calculado para cada vinho, sendo este o módulo da diferença da qualidade no banco da dados e da qualidade estimada no modelo. Assim, para a determinação do modelo mais eficaz foi considerado o que apresentou menor média de erro de estimação dentre os dois métodos e por tipo de vinho.</p>

# In[11]:


dfp=df.copy()
dfs=df.copy()


# <h3 align="justified">Criando o modelo (método de Pearson)</h3>

# In[12]:


dfp.insert(13, 'qualidade_alcool', 0)
dfp.insert(14, 'qualidade_volatilidade da acidez', 0)
dfp.insert(15, 'qualidade_cloretos', 0)
dfp.insert(16, 'qualidade_estimada', 0)
dfp.insert(17, 'erro', 0)
dfp.describe()


# In[13]:


for index, row in dfp.iterrows():
    if row['alcohol']<5.7:
        dfp.at[index,'qualidade_alcool']=0
    elif row['alcohol']<6.85:
        dfp.at[index,'qualidade_alcool']=1
    elif row['alcohol']<8:
        dfp.at[index,'qualidade_alcool']=2
    elif row['alcohol']<9.15:
        dfp.at[index,'qualidade_alcool']=3
    elif row['alcohol']<10.30:
        dfp.at[index,'qualidade_alcool']=4
    elif row['alcohol']<11.45:
        dfp.at[index,'qualidade_alcool']=5
    elif row['alcohol']<12.60:
        dfp.at[index,'qualidade_alcool']=6
    elif row['alcohol']<13.75:
        dfp.at[index,'qualidade_alcool']=7
    elif row['alcohol']<14.90:
        dfp.at[index,'qualidade_alcool']=8
    elif row['alcohol']<16.05:
        dfp.at[index,'qualidade_alcool']=9
    elif row['alcohol']>16.05:
        dfp.at[index,'qualidade_alcool']=10


# In[14]:


for index, row in dfp.iterrows():
    if row['volatile acidity']<0.08:
        dfp.at[index,'qualidade_volatilidade da acidez']=10
    elif row['volatile acidity']>=0.08:
        dfp.at[index,'qualidade_volatilidade da acidez']=9
    elif row['volatile acidity']>=0.33:
        dfp.at[index,'qualidade_volatilidade da acidez']=8
    elif row['volatile acidity']>=0.58:
        dfp.at[index,'qualidade_volatilidade da acidez']=7
    elif row['volatile acidity']>=0.83:
        dfp.at[index,'qualidade_volatilidade da acidez']=6
    elif row['volatile acidity']>=1.08:
        dfp.at[index,'qualidade_volatilidade da acidez']=5
    elif row['volatile acidity']>=1.33:
        dfp.at[index,'qualidade_volatilidade da acidez']=4
    elif row['volatile acidity']>=1.58:
        dfp.at[index,'qualidade_volatilidade da acidez']=3
    elif row['volatile acidity']>=1.83:
        dfp.at[index,'qualidade_volatilidade da acidez']=2
    elif row['volatile acidity']>=2.08:
        dfp.at[index,'qualidade_volatilidade da acidez']=1
    elif row['volatile acidity']>=2.33:
        dfp.at[index,'qualidade_volatilidade da acidez']=0


# In[15]:


for index, row in dfp.iterrows():
    if row['chlorides']<0.009:
        dfp.at[index,'qualidade_cloretos']=10
    elif row['chlorides']>=0.009:
        dfp.at[index,'qualidade_cloretos']=9
    elif row['chlorides']>=0.1093:
        dfp.at[index,'qualidade_cloretos']=8
    elif row['chlorides']>=0.2097:
        dfp.at[index,'qualidade_cloretos']=7
    elif row['chlorides']>=0.3100:
        dfp.at[index,'qualidade_cloretos']=6
    elif row['chlorides']>=0.4103:
        dfp.at[index,'qualidade_cloretos']=5
    elif row['chlorides']>=0.5107:
        dfp.at[index,'qualidade_cloretos']=4
    elif row['chlorides']>=0.6110:
        dfp.at[index,'qualidade_cloretos']=3
    elif row['chlorides']>=0.7113:
        dfp.at[index,'qualidade_cloretos']=2
    elif row['chlorides']>=0.8117:
        dfp.at[index,'qualidade_cloretos']=1
    elif row['chlorides']>=0.9120:
        dfp.at[index,'qualidade_cloretos']=0


# In[16]:


dfp['qualidade_estimada']=((dfp['qualidade_alcool']*0.47)+ (dfp['qualidade_volatilidade da acidez']*0.25)+(dfp['qualidade_cloretos']*0.2))/(0.47+0.25+0.2)
dfp['erro']=np.sqrt((dfp['qualidade_estimada']-dfp['quality'])**2)


# In[17]:


dfp.describe()


# <h3 align="justified">Criando o modelo (método de Spearman)</h3>

# In[18]:


dfs.insert(13, 'qualidade_alcool', 0)
dfs.insert(14, 'qualidade_densidade', 0)
dfs.insert(15, 'qualidade_cloretos', 0)
dfs.insert(16, 'qualidade_estimada', 0)
dfs.insert(17, 'erro', 0)
dfs.describe()


# In[19]:


for index, row in dfs.iterrows():
    if row['alcohol']<5.7:
        dfs.at[index,'qualidade_alcool']=0
    elif row['alcohol']<6.85:
        dfs.at[index,'qualidade_alcool']=1
    elif row['alcohol']<8:
        df.at[index,'qualidade_alcool']=2
    elif row['alcohol']<9.15:
        dfs.at[index,'qualidade_alcool']=3
    elif row['alcohol']<10.30:
        dfs.at[index,'qualidade_alcool']=4
    elif row['alcohol']<11.45:
        dfs.at[index,'qualidade_alcool']=5
    elif row['alcohol']<12.60:
        dfs.at[index,'qualidade_alcool']=6
    elif row['alcohol']<13.75:
        dfs.at[index,'qualidade_alcool']=7
    elif row['alcohol']<14.90:
        dfs.at[index,'qualidade_alcool']=8
    elif row['alcohol']<16.05:
        dfs.at[index,'qualidade_alcool']=9
    elif row['alcohol']>16.05:
        dfs.at[index,'qualidade_alcool']=10


# In[20]:


for index, row in dfs.iterrows():
    if row['density']<0.98711:
        dfs.at[index,'qualidade_densidade']=10
    elif row['density']>=0.98711:
        dfs.at[index,'qualidade_densidade']=9
    elif row['density']>=18.138925:
        dfs.at[index,'qualidade_densidade']=8
    elif row['density']>=35.29074:
        dfs.at[index,'qualidade_densidade']=7
    elif row['density']>=52.442555:
        dfs.at[index,'qualidade_densidade']=6
    elif row['density']>=69.59437:
        dfs.at[index,'qualidade_densidade']=5
    elif row['density']>=86.746185:
        dfs.at[index,'qualidade_densidade']=4
    elif row['density']>=103.898:
        dfs.at[index,'qualidade_densidade']=3
    elif row['density']>=121.049815:
        dfs.at[index,'qualidade_densidade']=2
    elif row['density']>=138.20163:
        dfs.at[index,'qualidade_densidade']=1
    elif row['density']>=155.353445:
        dfs.at[index,'qualidade_densidade']=0


# In[21]:


for index, row in dfs.iterrows():
    if row['chlorides']<0.009:
        dfs.at[index,'qualidade_cloretos']=10
    elif row['chlorides']>=0.009:
        dfs.at[index,'qualidade_cloretos']=9
    elif row['chlorides']>=0.1093:
        dfs.at[index,'qualidade_cloretos']=8
    elif row['chlorides']>=0.2097:
        dfs.at[index,'qualidade_cloretos']=7
    elif row['chlorides']>=0.3100:
        dfs.at[index,'qualidade_cloretos']=6
    elif row['chlorides']>=0.4103:
        dfs.at[index,'qualidade_cloretos']=5
    elif row['chlorides']>=0.5107:
        dfs.at[index,'qualidade_cloretos']=4
    elif row['chlorides']>=0.6110:
        dfs.at[index,'qualidade_cloretos']=3
    elif row['chlorides']>=0.7113:
        dfs.at[index,'qualidade_cloretos']=2
    elif row['chlorides']>=0.8117:
        dfs.at[index,'qualidade_cloretos']=1
    elif row['chlorides']>=0.9120:
        dfs.at[index,'qualidade_cloretos']=0


# In[22]:


dfs['qualidade_estimada']=((dfs['qualidade_alcool']*0.48)+(dfs['qualidade_densidade']*0.34)+(dfs['qualidade_cloretos']*0.30))/(0.48+0.34+0.30)
dfs['erro']=np.sqrt((dfs['qualidade_estimada']-dfs['quality'])**2)


# In[23]:


dfs.describe()


# <h3 align="justified">Comparando o erro de estimação nos diferentes tipos de vinho</h3>

# In[24]:


dfp.groupby('type')['erro'].describe()


# In[25]:


dfs.groupby("type")['erro'].describe()


# <h3 align="justified">Conclusão</h3>
# 
# <p align="justified"> O erro de estimação médio  para o método de correlação de Pearson se mostrou menor que no método de Spearman, tanto para os valores totais quanto para o cada tipo de vinho , sendo este o mais adequado para  a modelagem.</p>
