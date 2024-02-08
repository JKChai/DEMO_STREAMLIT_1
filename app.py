import pandas as pd
import streamlit as st

from time import time
from pkgs.config import SetupFactory

@st.cache_data
def get_data():
    rootpath = SetupFactory()
    df = pd.read_csv(f"{rootpath}\\..\\assets\\ContosoRetailDW_FactSales.csv")
    return df

def load_streamlit(obj):

    st.title("WORKFLOW PROTOTYPE")

    col1, col2, col3 = st.columns([0.49,0.02,0.49])

    with col1:
        st.write("COUNT of ROWS")
        st.write(obj.shape[0])

    with col3:
        st.write("COUNT of COLUMNS")
        st.write(obj.shape[1])

    st.dataframe(obj)

def convert_seconds(seconds):
    (hours, seconds) = divmod(seconds, 3600)
    (minutes, seconds) = divmod(seconds, 60)
    (seconds, milliseconds) = divmod(seconds, 1)

    milliseconds *= 1000

    return f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}.{milliseconds:06.03f}"

def main():
    t_0 = time()

    st.set_page_config(layout="wide")
    df = get_data()
    
    load_streamlit(df)
    t_1 = time()

    with st.expander("Amount of time to take to run this main process 👇"):
        # st.info(strftime('%H:%M:%S.%f', gmtime(t_1 - t_0)))
        st.info(convert_seconds(t_1 - t_0))
        st.info(t_1 - t_0)

if __name__ == "__main__":
    main()
    main = 0