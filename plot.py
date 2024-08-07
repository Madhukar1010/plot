import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

st.header("1. Altair scatter plot")
chart_data = pd.DataFrame(np.random.randn(500,5),
                          columns = ["a","b","c","d","e"])
st.table(chart_data.head())

chart = alt.Chart(chart_data).mark_circle().encode(x = "a",y = "b",
                 size = "c",  tooltip = ["a","b","c","d","e"])
st.altair_chart(chart)

st.header("2. Intercative charts")
st.subheader("2.1 line chart")
df = pd.read_csv("C:/Users/madhu/OneDrive/Desktop/streamlit/lang_data.csv")
lang_list = df.columns.tolist()
lang_choices = st.multiselect("select lans : ", lang_list)
new_df = df[lang_choices]
st.table(new_df.head())
st.line_chart(new_df)

st.subheader("2.2 area chart")
st.area_chart(new_df)

st.header("3. data visualisation with plotly")
st.subheader("3.1 Displaying the dataset")
df = pd.read_csv("C:/Users/madhu/OneDrive/Desktop/streamlit/tips.csv")
st.table(df.head())

st.subheader("3.2 pie chart")
fig = px.pie(df, values = "total_bill", names = "day")
st.plotly_chart(fig)

st.subheader("3.3 multiple parameteres in pie chart")
fig = px.pie(df, values = "total_bill", names = "day", opacity = .7,
             color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader("3.4 Histogram")
x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)

hist_data = [x1,x2,x3]
group_labels = ["group-1","group-2","group-3"]
fig = ff.create_distplot(hist_data, group_labels, bin_size = [.1,.25,.5])
st.plotly_chart(fig)
