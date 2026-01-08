import streamlit as st
st.title("Pre inteligentných ľudí")
with open("trieskove_obrabanie.odt", "rb") as file:
    btn = st.download_button(
            label="Download",
            data=file,
            file_name="trieskove_obrabanie.odt",
            mime="application/vnd.oasis.opendocument.text",
            key="1"
          )
st.title("Pre kognitívne menej vyspelých jedincov")
with open("trieskove_brabanie(2).odt", "rb") as file:
    buten = st.download_button(
            label="Download",
            data=file,
            file_name="trieskove_obrabanie.odt",
            mime="application/vnd.oasis.opendocument.text",
            key="2"
          )