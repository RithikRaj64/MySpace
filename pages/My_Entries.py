import streamlit as st

from menu import menu_with_redirect
from utils import group_entries_by_month, render_month_entries

menu_with_redirect()

db = st.session_state.db

username = st.session_state.username
name = st.session_state.name
entries = db.fetch_all_entries(username)
grouped_entries = group_entries_by_month(entries)

if not entries:
    st.info(f"Hey {name}...You have no diary entries yet. Start writing your first entry!")
else:
    allow_delete = st.sidebar.toggle("Delete Entries")
    for month, month_entries in grouped_entries.items():
        render_month_entries(month, month_entries, allow_delete, db)

    
        