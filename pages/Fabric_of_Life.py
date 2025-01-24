import streamlit as st

import time

from menu import menu_with_redirect
from utils import group_entries_by_month, render_month_entries

menu_with_redirect()

db = st.session_state.db

username = st.session_state.username
name = st.session_state.name
threads = db.fetch_all_entries(username)

if not threads:
    st.info(f"Hey {name}...You have no threads yet. Start weaving the fabric of your life!")
    time.sleep(3)
    st.switch_page("pages/Weave_your_Day.py")
else:
    st.sidebar.header("Manage Threads")
    allow_delete = st.sidebar.checkbox("Enable Delete")
    
    search_content = st.sidebar.text_input("Search threads by Content:", "")
    search_vibe = st.sidebar.text_input("Search threads by Vibe:", "")
    
    sort_by = st.sidebar.selectbox(
        "Sort threads by:",
        options=["Date (Newest)", "Date (Oldest)"],
        index=0
    )
    
    if search_content:
        threads = [thread for thread in threads if search_content.lower() in thread.content.lower()]
    
    if search_vibe:
        threads = [thread for thread in threads if search_vibe.lower() in thread.vibe.lower()]
    
    if sort_by == "Date (Newest)":
        threads = sorted(threads, key=lambda e: e.created_at, reverse=True)
    elif sort_by == "Date (Oldest)":
        threads = sorted(threads, key=lambda e: e.created_at)
    
    if not threads:
        st.info(f"Hey {name}...You have no threads that match your search")

    grouped_entries = group_entries_by_month(threads)
    for month, month_entries in grouped_entries.items():
        render_month_entries(month, month_entries, allow_delete, db)
