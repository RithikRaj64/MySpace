import streamlit as st

from utils import processContent

def render_entry(entry, month, i, allow_delete, db):
    formatted_date = format_date(entry.created_at)
    st.markdown(f"🗓️ *{formatted_date}*")
    st.markdown(f"📌 {entry.vibe}")
    processed_content = processContent(entry.content)
    st.markdown(processed_content)
    
    if allow_delete:
        if st.button("Delete", key=f"delete_{month}_{i}"):
            db.delete_entry(entry)
            st.rerun()  

def format_date(created_at):
    day = int(created_at.strftime('%d'))
    suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    return created_at.strftime(f'%A, %B {day}{suffix} %Y at %H:%M')

def render_month_entries(month, month_entries, allow_delete, db):
    with st.expander(month):
        with st.container(border=True, height=600):
            for i, entry in enumerate(month_entries):
                render_entry(entry, month, i, allow_delete, db)  
                if i < len(month_entries) - 1:
                    st.markdown("---")

def render_whispers(whispers):
    for whisper in whispers:
        st.markdown(f"📌 {whisper.topic}")
        processed_content = processContent(whisper.content)
        st.markdown(processed_content)
        st.markdown("---")