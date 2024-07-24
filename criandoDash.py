import streamlit as st #criar dashboard
import pandas as pd #manipular dados
import plotly_express as px #construir gráficospip install pandas

df = pd.read_csv("supermarketSales.csv", sep=",",
                 decimal=",")
df["Date"]=pd.to_datetime(df["Date"])
df=df.sort_values(["Date"])

df["Month"]=df["Date"].apply(lambda x:str(x.year)+
                             "-"+str(x.month))
month=st.sidebar._selectbox("Mês",df["Month"].unique())

df_filter=df[df["Month"]==month]
df_filter


#executar no terminal streamlit run dashboard.py