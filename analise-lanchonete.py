#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


dados = pd.read_csv('dados.csv')


# In[3]:


dados


# In[4]:


dados.describe()


# In[5]:


dados.dtypes


# In[6]:


dados.drop(columns=['Unnamed: 4','Unnamed: 5','Unnamed: 6'], inplace=True)


# In[7]:


dados


# In[14]:


dados.rename(columns={'Nº DO PEDIDO': 'pedido',
                     'TEMPO DE ESPERA (MINUTOS)': 'espera',
                     'DIA DA SEMANA': 'dia',
                     'PERÍODO': 'periodo'}, inplace=True)


# In[22]:


dados[dados.dia == 'Terça']


# In[23]:


dados_terca = dados[dados.dia == 'Terça']


# In[24]:


dados_terca


# In[27]:


dados['espera'] = dados['espera'].str.replace(',','.')


# In[28]:


dados


# In[32]:


dados['espera'] = dados['espera'].astype(float)


# In[34]:


dados.dtypes


# In[35]:


dados_ter = dados[dados.dia == 'Terça']


# In[36]:


dados_ter


# In[37]:


dados_ter.describe()


# In[38]:


dados.describe()


# In[45]:


plt.figure(figsize=(30,10))
sns.lineplot(x=dados.dia, y=dados.espera)
plt.show()


# In[41]:


dados.describe()


# In[42]:


dados[dados.espera == 9.490000 ]


# In[46]:


dados_seg = dados[dados.dia == 'Segunda']


# In[47]:


dados_seg


# In[50]:


sns.barplot(x=dados_seg.periodo, y=dados_seg.espera)
plt.xlabel("Período do Dia")
plt.ylabel("Tempo de espera (minutos)")
plt.title("Diferença de tempo (Segunda)")
plt.show()


# In[51]:


dados_quar = dados[dados.dia == 'Quarta']


# In[52]:


dados_quar


# In[53]:


sns.barplot(x=dados_quar.periodo, y=dados_quar.espera)
plt.xlabel("Período do Dia")
plt.ylabel("Tempo de espera (minutos)")
plt.title("Diferença de tempo (Quarta)")
plt.show()


# In[54]:


dados_sex = dados[dados.dia == 'Sexta']


# In[55]:


dados_sex


# In[56]:


sns.barplot(x=dados_sex.periodo, y=dados_sex.espera)
plt.xlabel("Período do Dia")
plt.ylabel("Tempo de espera (minutos)")
plt.title("Diferença de tempo (Sexta)")
plt.show()


# In[57]:


dados_dom = dados[dados.dia == 'Domingo']


# In[58]:


dados_dom


# In[59]:


sns.barplot(x=dados_dom.periodo, y=dados_dom.espera)
plt.xlabel("Período do Dia")
plt.ylabel("Tempo de espera (minutos)")
plt.title("Diferença de tempo (Domingo)")
plt.show()


# In[ ]:




