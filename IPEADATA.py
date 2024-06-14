import streamlit as st

st.set_page_config(
    page_title="Lista de Exercícios IPEADATA",
    page_icon="👋",
)

st.subheader("Criação de IPEADATA")

st.code(code, language='python')

import ipeadatapy as ip
ip.list_series('Selic')

selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
selic

ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))")
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))")
plt.show()

