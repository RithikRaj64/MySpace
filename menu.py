import streamlit as st


def authenticated_menu():
    st.sidebar.page_link("MySpace.py", label="Home", icon="🏡")
    st.sidebar.page_link("pages/Weave_your_Day.py", label="Weave your Day", icon="🪡")
    st.sidebar.page_link("pages/Fabric_of_Life.py", label="Fabric of Life", icon="🎀")
    st.sidebar.page_link("pages/Whisper_Within.py", label="Whisper Within", icon="🌕")
    st.sidebar.page_link("pages/Echoes_of_Whisper.py", label="Echoes of Whisper", icon="🌌")
    
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.switch_page("MySpace.py")


def unauthenticated_menu():
    st.sidebar.page_link("MySpace.py", label="Log in")


def menu():
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        # unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.switch_page("MySpace.py")
    menu()