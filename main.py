import streamlit as st
from langchain_helper import get_few_shot_db_chain

# Set page title and background color
st.set_page_config(page_title="Gaurav T Shirts store", page_icon="👕", layout="wide", initial_sidebar_state="expanded")

# Set custom background color
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("url_goes_here")
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set title and subtitle with custom colors
st.title("Welcome to Gaurav T Shirts Store!")
st.markdown("<h3 style='color: #FF5733;'>Database Q&A 👕</h3>", unsafe_allow_html=True)

# Input field for question
question = st.text_input("Ask a question about our T-shirts:", "")

if question:
    # Fetch response using LangChain
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    # Display answer with a colored header
    st.markdown("<h2 style='color: #0056b3;'>Answer:</h2>", unsafe_allow_html=True)
    st.write(response)
