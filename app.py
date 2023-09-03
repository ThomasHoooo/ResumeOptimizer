from dotenv import load_dotenv

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from docx import Document
import prompts


def get_resume_text(resume):
    doc = Document(resume)
    resume_text = ""
    for paragraph in doc.paragraphs:
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
        if not (company or role or job_description or resume):
            st.error("Please fill in all the fields")
            st.stop()
        with st.spinner("Loading..."):
            # get resume text
            resume_text = get_resume_text(resume)

            chat_gpt = ChatOpenAI(temperature=0.9, model_name="gpt-4")
            memory = ConversationBufferMemory() 
            convo = ConversationChain(llm=chat_gpt, memory=memory, verbose=True)
            convo.predict(input=prompts.RESPONSIBILITIES.format(job_description=job_description))
            response = convo.predict(input=prompts.TAILOR.format(role=role, company=company, resume=resume_text))
            response = convo.predict(input=prompts.DIFFERENCE)
            st.write(response)

if __name__ == "__main__":
    main()
