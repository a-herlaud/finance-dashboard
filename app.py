import streamlit as st

st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("Finance Dashboard")


st.divider()


st.subheader("Project overview")
st.markdown(
    """
    This dashboard is designed to provide an easy-to-read view of market data, both daily and historical, as well as a chatbot for follow-up questions.

    It lets users explore market indexes and ask questions about the data.

    """
)

st.subheader("Main pages")
st.markdown(
    """
    - **Stock Index**: market overview and basic analysis for multiple key benchmark indexes across different markets.
    - **Chatbot**: conversational interface for asking financial questions about stock indexes and the market.
    """
)

st.divider()

st.subheader("Stock Index page")
st.markdown(
    """
    The stock page loops through the supported tickers and renders a full market card for each one.

    Each index view includes:
    - a current daily return,
    - an expandable details section,
    - daily intraday metrics,
    - and a one-minute price chart for the latest session.

    Buttons are accessible for each index to:
    - show a further historical analysis of the index,
    - display the historical price chart of the index,
    - display a treemap of the constituents in the index with their weight.
    """
)

st.subheader("Chatbot page")
st.markdown(
    """
    The chatbot is powered by Gemini and provides a way to answer questions about stock indexes.

    Configure `GEMINI_API_KEY` before using it.
    """
)

st.info(
    "Use the sidebar to navigate to the dedicated pages and explore the index view or the chatbot.",
    icon="ℹ️",
)
