import streamlit as st

import random
from datetime import datetime
import time

from menu import menu_with_redirect
from schema import Entry
from utils import get_personalized_greeting

menu_with_redirect()

name = st.session_state.name
username = st.session_state.username

db = st.session_state.db

if "personalized_greeting" not in st.session_state:
    st.session_state.personalized_greeting = get_personalized_greeting(name)
st.header(st.session_state.personalized_greeting)

content = st.text_area("Write your entry here:", "", height=200)

vibe = st.text_input("Describe your day in a few words:", "")

created_at = datetime.now()

if st.button("Make Entry"):
    with st.status("Saving your memory") as status:
        entry = Entry(username=st.session_state.username, content=content, vibe=vibe, created_at=created_at)
        db.create_new_entry(entry)
        status.update(
                label="Memory updated",
                state="complete",
                expanded=False,
        )
        time.sleep(3)
        st.switch_page("pages/My_Entries.py")
