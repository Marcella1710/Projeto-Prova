import streamlit as st

st.set_page_config(
    page_title="Lista de Exercícios Projetos",
    page_icon="👋",
)

st.subheader("Criação de Projetos")

st.code(code, language='python')

import pandas as pd  

arquivo = "projetos.csv" 
df = pd.read_csv(arquivo, sep=';') 
df.head(23)

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
print(df.tail())

colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
df.groupby('ano')[colunas].sum()

import matplotlib.pyplot as plt
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*')
plt.show()

df["Projeto1"].plot(kind = 'hist')
df["Projeto4"].plot(kind = 'hist')
plt.show()