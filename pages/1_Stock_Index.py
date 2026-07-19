import streamlit as st
from components.sidebar import render_sidebar
from components.full_analysis import full_analysis
from components.daily_analysis import daily_analysis

st.set_page_config(page_title="Stock Indexes", layout="wide")


indexes = {
    "S&P 500": "^GSPC",
    "NASDAQ 100": "^NDX",
    "Dow Jones": "^DJI",
    "CAC 40": "^FCHI",
    "Nikkei 225": "^N225",
    "KOSPI": "^KS11",
    "DAX 40": "^GDAXI",
    "FTSE 100": "^FTSE",
}

if "selected_index" not in st.session_state:
    st.session_state.selected_index = None

render_sidebar()
# st.write(indexes.keys())
if st.session_state.selected_index is None:
    st.title("INDEX OVERVIEW")

    for name, ticker in indexes.items():
        st.divider()
        daily_analysis(ticker, name)

        if st.button(f"Analyze {name}", key=name):
            st.session_state.selected_index = name
            st.rerun()

else:

    index = st.session_state.selected_index

    st.title(f"{index} Full Analysis")

    full_analysis(indexes[index])