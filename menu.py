import streamlit as st


def authenticated_menu():
    st.sidebar.page_link("MySpace.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/New_Entry.py", label="Make Entry", icon="✏️")
    st.sidebar.page_link("pages/My_Entries.py", label="My Entries", icon="📄")
    
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