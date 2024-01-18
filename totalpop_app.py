import pandas as pd
import streamlit as st
import plotly.express as px

st.title('This app shows analysis od Kenya 2009 Cencus population')
st.write("Cencus Population Analysis")
 
@st.cache_data
def load_data():
    data=pd.read_csv('Rural_Urban_Population_By_Age_Sex_and_by_District__2009.CSV')
    data.head()
    data['Total_population']=data['Male']+data['Female']
    Nairobi=data[data['County']=='Nairobi']
    Nairobi.head()
    return data

data=load_data()



if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)

fig=px.bar(data,x='District',y='Total',title='Total by District Nairobi County')
fig.show()
st.plotly_chart(fig)


