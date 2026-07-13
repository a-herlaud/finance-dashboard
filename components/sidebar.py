import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("Options")

        st.divider()

        for option in ["Home", "My Portfolio", "Chatbot"]:
            st.button(option, width='stretch')

        theme = st.radio(
            "Theme",
            ["Light", "Dark"]
        )

        st.button("Refresh", width='stretch')

    return {
        "theme": theme,
    }