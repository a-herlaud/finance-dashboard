import streamlit as st

def render_sidebar():
    with st.sidebar:

        theme = st.radio(
            "Theme",
            ["Light", "Dark"]
        )

        st.button("Refresh", width='stretch')

    return {
        "theme": theme,
    }