import streamlit as st

st.title("Trieskové obrábanie - Poznámky")
with open("trieskove_obrabanie.odt", "rb") as file:
    btn = st.download_button(
            label="Download",
            data=file,
            file_name="trieskove_obrabanie.odt",
            mime="application/vnd.oasis.opendocument.text",
            key="1"
          )