import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("Options")

        st.divider()

        for option in ["Home", "My Portfolio", "Chatbot"]:
            st.button(option, use_container_width=True)

        theme = st.radio(
            "Theme",
            ["Light", "Dark"]
        )

        st.button("Refresh", use_container_width=True)

    return {
        "theme": theme,
    }