import streamlit as st

import time

from menu import menu_with_redirect
from utils import render_whispers

menu_with_redirect()

db = st.session_state.db

name = st.session_state.name
username = st.session_state.username

whispers = db.fetch_all_whispers(username)

if not whispers:
    st.info(f"Hey {name}...You have no whispers yet. Start whispering!")
    time.sleep(3)
    st.switch_page("pages/Whisper_Within.py")
else:
    render_whispers(whispers)