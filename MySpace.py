import streamlit as st
from menu import menu

from utils import DB
from schema import User

db = DB()

st.session_state.db = db

user_info = db.users

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:

    tabs = st.tabs(["Login", "Register"])

    with tabs[0]:
        login_username = st.text_input("Username", key="login_username")
        login_password = st.text_input(
            "Password", type="password", key="login_password"
        )

        if st.button("Login", key="login_button"):
            user = next((u for u in user_info if u.username == login_username), None)
            if user:
                if user.password == login_password:
                    st.session_state.name = user.name
                    st.session_state.username = user.username
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("The password that you have entered is incorrect")
            else:
                st.error("Invalid username")

    with tabs[1]:
        username_check = False
        password_check = False
        confirm_password_check = False

        reg_username = st.text_input(
            "Username", key="reg_username", help="Username should be unique"
        )
        if reg_username:
            if any(u.username == reg_username for u in user_info):
                st.error("Username already exists")
            else:
                username_check = True

        reg_name = st.text_input(
            "Preferred Name",
            key="reg_name",
            help="If left empty, username will be taken as preferred name",
        )

        reg_password = st.text_input(
            "Password",
            type="password",
            key="reg_password",
            help="Password should contain atleast 8 characters",
        )
        if reg_password:
            if not len(reg_password) >= 8:
                st.error("Password is weak")
                st.error("Password should contain atleast 8 characters")
            else:
                password_check = True

        reg_conf_password = st.text_input(
            "Confirm Password", type="password", key="reg_conf_password"
        )
        if reg_conf_password:
            if reg_password != reg_conf_password:
                st.error("Password and Confirm Password doesn't match")
            else:
                confirm_password_check = True

        if st.button(
            "Register",
            disabled=(not username_check & password_check & confirm_password_check),
            key="register_button",
        ):
            if not reg_name:
                reg_name = reg_username

            new_user = User(**{
                "username": reg_username,
                "password": reg_password,
                "name": reg_name,
            })

            user_info.append(db.create_new_user(new_user))

            st.session_state.name = reg_name
            st.session_state.username = reg_username
            st.session_state.authenticated = True
            st.rerun()

else:
    # with st.spinner("Creating LLM and Embedding Model instances") as spin:
    #     if "kg" not in st.session_state:
    #         st.session_state.kg = knowledge_graph = KG()

    markdown_content = """
# Welcome to LegalFlow 🏛️  

**LegalFlow** is your go-to platform for understanding and navigating complex legal documents. Whether you're a legal professional or a general user, our intelligent chatbot is here to provide accurate, insightful, and easy-to-understand answers to your legal queries.  

We aim to bridge the gap between legal complexity and accessibility. By leveraging the latest advancements in AI, our platform delivers unparalleled legal insights to empower users with accurate and actionable information.  

**Simplifying Laws, Empowering Decisions, LegalFlow!**  
    """
    st.markdown(markdown_content)

menu()
