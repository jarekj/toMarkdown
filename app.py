from markitdown import MarkItDown
import streamlit as st

st.set_page_config(layout="wide")

def get_markdown(filename):
    md = MarkItDown(enable_plugins=False)
    result = md.convert(filename)
    # print(result)
    return result.text_content


st.title("To Markdown Converter")

uploaded_file = st.file_uploader("Upload a file", type=["docx", "pdf", "xlsx", "xls","pptx", "ppt", "txt", "csv", "html", "xml", "json", "zip","epub", "msg"])

if uploaded_file:
    makrdown = get_markdown(uploaded_file)
    st.text_area("Markdown Output", makrdown, height=500)