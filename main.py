import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Elderly Project",
    page_icon="🧓🏼",
    layout="wide")

st.title("Modgut's Elderly Project")
st.write('Filter data to find healthy people with following criteria:')

df = pd.read_excel('data.xlsx')
col_list = df.columns.to_list()

for i in range(len(col_list)):
    st.write(col_list[i], "-- Min:", df[col_list[i]].min(), "Max:", df[col_list[i]].max())

#start_time = st.slider(
#    "When do you start?",
#    value=datetime(2020, 1, 1, 9, 30),
#    format="MM/DD/YY - hh:mm",
#)
#st.write("Start time:", start_time)

#show_btn = st.button("Display!")
#if show_btn:
#for i in ('gender', 'age_group', 'bmi_group', 'region'):
#    if i in option:
#        # Create distplot with custom bin_size
#        fig = px.pie(region[option].value_counts(), values=region[option].value_counts().values, names=region[option].value_counts().index)
#        fig.update_traces(hoverinfo='label+value', textinfo='label+value+percent')
#
#        # Plot!
#        st.plotly_chart(fig)

