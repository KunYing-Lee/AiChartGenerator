from langchain.chains import create_tagging_chain_pydantic

from langchain.chat_models import ChatOpenAI
from enum import Enum
from pydantic import BaseModel, Field
import streamlit as st
import pandas as pd
import os
os.environ["OPENAI_API_KEY"] = "API_Key"

def show_chart(chartType, column):

    if chartType == "bar_chart":
        st.bar_chart(df_now, x=column)
    elif chartType == "area_chart":
        st.area_chart(df_now, x=column)
    elif chartType == "line_chart":
        st.line_chart(df_now, x=column)
    return True

df_now = None
text_input = ''

st.title("AI Chart Generator")

uploaded_file = st.file_uploader("Choose a dataset file", type=['csv'])
if uploaded_file is not None:
    df_now = pd.read_csv(uploaded_file)
    st.dataframe(df_now, use_container_width=True)

if df_now is None:
    st.stop()
    
text_input = df_now.to_string()

class DataFeature(BaseModel):
    chartType: str = Field(..., 
                        enum=["bar_chart", "area_chart", "line_chart"],
                        description="""
                        the chart type to visualize the dataframe strickly following rules:
                        Use 'area_chart': if the dataframe is monthly-basis, daily-basis, or yearly-basis
                        Use 'bar_chart': if the dataframe contains categorical data.
                        Use 'line_chart': if the dataframe is seconds-basis or smaller periods.
                        """)
    column: str = Field(..., 
                        description="""
                        the column name in the dataframe that is best for the x-axis
                        """)

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

tagging_chain = create_tagging_chain_pydantic(DataFeature, llm)
res = tagging_chain.run(text_input)

show_chart(res.chartType, res.column)
