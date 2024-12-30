import streamlit as st

from menu import menu_with_redirect
from utils import group_entries_by_month

menu_with_redirect()

db = st.session_state.db

username = st.session_state.username
name = st.session_state.name
entries = db.fetch_all_entries(username)
grouped_entries = group_entries_by_month(entries)

if not entries:
    st.info(f"Hey {name}...You have no diary entries yet. Start writing your first entry!")
else:
    if st.sidebar.toggle("Delete Entries"):
        for month, month_entries in grouped_entries.items():
            with st.expander(month):
                with st.container(border=True, height=600):
                    for i, entry in enumerate(month_entries):
                        formatted_date = entry.created_at.strftime('%A, %B %d, %Y at %H:%M')
                        day = int(entry.created_at.strftime('%d'))
                        suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
                        formatted_date = entry.created_at.strftime(f'%A, %B {day}{suffix} %Y at %H:%M')
                        st.markdown(f"*{formatted_date}*")
                        st.markdown(f"{entry.vibe}")
                        st.markdown(f"> {entry.content}")
                        if st.button("Delete", key=f"delete_{i}"):
                            delete_entry = db.delete_entry(entry)
                            st.rerun()
                        if i < len(month_entries) - 1:
                            st.markdown("---")
    else:
        for month, month_entries in grouped_entries.items():
            with st.expander(month):
                with st.container(border=True, height=600):
                    for i, entry in enumerate(month_entries):
                        formatted_date = entry.created_at.strftime('%A, %B %d, %Y at %H:%M')
                        day = int(entry.created_at.strftime('%d'))
                        suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
                        formatted_date = entry.created_at.strftime(f'%A, %B {day}{suffix} %Y at %H:%M')
                        st.markdown(f"*{formatted_date}*")
                        st.markdown(f"{entry.vibe}")
                        st.markdown(f"> {entry.content}")
                        if i < len(month_entries) - 1:
                            st.markdown("---")
        