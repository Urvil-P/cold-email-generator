import streamlit as st

from lm import llm
from mail_generator import Email_Generator

st.title("Email Generator")
col1, col2, col3 = st.columns(3)

with col1:
    sender = st.text_input("Sender")
with col2:
    receiver = st.text_input("Receiver")
with col3:
    purpose = st.text_input("Purpose:")

eg = Email_Generator(llm)

button = st.button("Generate")
if button:
    sub, cont = eg.generate_email(sender, receiver, purpose)
    # Use st.text_area for wrapping or st.markdown for rich text formatting
    st.subheader("Generated Email")
    st.markdown(f"**Subject:** {sub}")
    st.text_area("Email Content", value=cont, height=200, max_chars=None)
