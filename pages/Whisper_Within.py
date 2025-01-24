import streamlit as st

import time

from menu import menu_with_redirect
from schema import Whisper

menu_with_redirect()

name = st.session_state.name
username = st.session_state.username

db = st.session_state.db

st.header(f"Hey {name}, what's on your mind?")

whisper_content = st.text_area("What's your whisper?:", "", height=200)

topic = st.text_input("What is this about?", "")

if st.button("Make Whisper"):
    with st.status("Saving your whisper") as status:
        whisper = Whisper(username=st.session_state.username, content=whisper_content, topic=topic)
        db.create_new_whisper(whisper)
        status.update(
            label="Your whisper has been saved. Feel free to revisit it anytime!",
            state="complete",
            expanded=False,
        )
        time.sleep(2)
        st.switch_page("pages/Echoes_of_Whisper.py")