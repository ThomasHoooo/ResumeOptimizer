from dotenv import load_dotenv

import streamlit as st
from langchain.llms import OpenAI
from docx import Document


def get_resume_text(resume):
    doc = Document(resume)
    resume_text = ""
    for paragraph in doc.paragraphs:
        st.write(paragraph.text)  # to remove
        resume_text += paragraph.text + "\n"
    return resume_text


def main():
    load_dotenv()

    st.set_page_config(page_title="Improve your resume")
    st.header("Improve your resume")
    company = st.text_input("Which company are you applying for?")
    role = st.text_input("What role are you applying for?")
    job_description = st.text_input("Enter the job description here:")

    resume = st.file_uploader("Upload your resume here", type=["docx"])
    if st.button("Go"):
        with st.spinner("Loading..."):
            # get resume text
            resume_text = get_resume_text(resume)

    llm = OpenAI(temperature=0.9)
    


if __name__ == "__main__":
    main()
