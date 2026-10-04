##importing required libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns



#  Loading the dataset
df = pd.read_csv("dataset/cleaned.csv")

# Set webpage configuration
st.set_page_config(page_title="SARA ENTERPRICES", layout='wide')

# web page tiltle

st.title("SARA ENTERPRICES")
st.subheader("SARA ENTERPRICES dashboard for sales analysis.")


# slicer
col1 ,col2 ,col3 , col4 , col5    = st.columns(5)

with col1:
    country = st.selectbox("Select Country ",['All']+ list(df.Country.unique()))
    if country!='All':
        df = df[df.Country == country]

with col2:
    segment = st.selectbox("Select Segment ",['All']+ list(df.Segment.unique()))
    if segment!='All':
        df = df[df.Segment == segment]

with col3:
    product = st.selectbox("Select Product ",['All']+ list(df.Product.unique()))
    if product!='All':
        df = df[df.Product == product]

with col4:
    year  = st.selectbox("Select Year ",['All']+ list(df.Year.unique()))
    if year !='All':
        df = df[df.Year   == year]

with col5:
    month = st.selectbox("Select Month",['All']+list(df['Month Name'].unique()))
    if month!='All':
        df = df[df['Month Name']==month]

# KPI's
col1 ,col2 ,col3 , col4 , col5     = st.columns(5)
cols = [col1,col2,col3,col4,col5]
kpi = [' Sales','GrossManu','Profit','Units Sold','COGS']
for i in range(5):
    with cols[i]:
        if round(df[kpi[i]].sum(),2)>1000000:
            st.metric("Total"+kpi[i],str(round(df[kpi[i]].sum()/1000000,2))+"M")
        elif round(df[kpi[i]].sum(),2)>1000:
            st.metric("Total"+kpi[i],str(round(df[kpi[i]].sum()/1000,2))+"K")
        else:
            st.metric("Total"+kpi[i],str(round(df[kpi[i]].sum()/1000,2)))

# Plotting / Graph
col1 , col2 = st.columns(2)
with col1:
    pbd = df.groupby('Discount Band').agg({'Profit':'sum'}).reset_index()
    fig , ax1 = plt.subplots(figsize=(12,4))
    ax1.bar(pbd['Discount Band'] , pbd['Profit'])
    st.pyplot(fig)
with col2:
    fig , ax2 = plt.subplots(figsize=(12,4))
    sns.histplot(df['Profit'] , kde=True , ax=ax2)
    st.pyplot(fig)


st.text("Data Info"+ str(df.shape))
st.dataframe(df , height=250)



