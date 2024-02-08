import datetime
import pandas as pd
import streamlit as st

from time import time
from pkgs.config import SetupFactory

@st.cache_data
def get_data():
    # rootpath = SetupFactory()
    df = pd.read_csv("assets/ContosoRetailDW_FactSales.csv")
    return df

def load_streamlit(obj):

    st.title("WORKFLOW PROTOTYPE")
    st.markdown("***")
    st.markdown("### ASSUMING :rainbow[PRODUCTS] PEOPLE 🦺 ARE USING THIS FOR THE WORKFLOW INPUT")
    st.markdown("***")
    with st.sidebar:
        st.title("BEFORE 🔓")
        col1, col2= st.columns(2)
        with st.container():
            with col1:
                st.markdown('''#### COUNT ROWS''')
                st.write(obj.shape[0])
            with col2:
                st.markdown('''#### COUNT COLUMNS''')
                st.write(obj.shape[1])
        st.markdown('''#### COUNT UNIQUE DateKey''')
        st.write(obj["DateKey"].nunique())
        st.markdown('''#### COUNT UNIQUE UnitCost''')
        st.write(obj["UnitCost"].nunique())


    col1, col2, col3 = st.columns([0.45,0.1,0.45])

    with col1:
        ## Get StoreKey
        uniq_store = obj["StoreKey"].unique()
        options = st.multiselect(
            " ✋ Hey Folks!! Select StoreKey items PLEASE...",
            uniq_store)

        if len(options) == 0:
            st.write("Please select an item 🤬")
        else:
            st.write("Here is the list of SELECTED StoreKey 👩‍💻", options)
            obj = obj.loc[obj["StoreKey"].isin(options)]
    with col3:
        ## Get Cost Selection
        cost_filter = st.number_input('Please provide the MINIMUM ACCEPTED COST 💰')
        st.write("Current :red[MIN] is ", obj["UnitCost"].min(),"& :green[MAX] is ", obj["UnitCost"].max())
        st.write('Provided cost states that it should be at least ', cost_filter)

        if (cost_filter >= obj["UnitCost"].min()) & (cost_filter <= obj["UnitCost"].max()):
            obj = obj.loc[obj["UnitCost"] >= cost_filter]
        
    if len(options) != 0:
        with st.container(border=True):
            ## Get DateKey
            min_date = min(pd.to_datetime(obj["DateKey"], format="%Y-%m-%d").dt.date)
            max_date = max(pd.to_datetime(obj["DateKey"], format="%Y-%m-%d").dt.date)
            daterange = st.slider(
                "Please Select a Date",
                min_value=min_date,
                max_value=max_date,
                value=(datetime.date(2008, 1, 1), datetime.date(2008, 2, 1)),
                format="yyyy-MM-DD"
            )

            st.write("You selected date from ", daterange[0].strftime("%Y-%m-%d"), " to ", daterange[1].strftime("%Y-%m-%d"))
            obj.loc[:,"DateKey"] = pd.to_datetime(obj["DateKey"], format="%Y-%m-%d").dt.date
            obj = obj.loc[(obj["DateKey"] >= daterange[0]) & (obj["DateKey"] <= daterange[1])]

    obj.reset_index(inplace=True)
    st.text("")
    st.markdown("# OUTPUT RESULTS OF THE TABLE FOR USERS ✨")
    st.dataframe(obj)

    with st.sidebar:
        st.title("AFTER 🎊")
        col1, col2= st.columns(2)
        with st.container():
            with col1:
                st.markdown('''#### COUNT ROWS''')
                st.write(obj.shape[0])
            with col2:
                st.markdown('''#### COUNT COLUMNS''')
                st.write(obj.shape[1])
        st.markdown('''#### COUNT UNIQUE DateKey''')
        st.write(obj["DateKey"].nunique())
        st.markdown('''#### COUNT UNIQUE UnitCost''')
        st.write(obj["UnitCost"].nunique())


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