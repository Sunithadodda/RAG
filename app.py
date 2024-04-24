import streamlit as st
import PyPDF2
import google.generativeai as genai

def retrieve_text_from_pdf(pdf):
    with open(pdf, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def main():
   
    pdf_path = "context.pdf"
    model_name = "gemini-1.5-pro-latest"
    with open("apikey.txt", "r") as file:
        key = file.read()
    genai.configure(api_key=key)
    st.title("""RAG System for 'Leave No Context Behind' paper""")
    question = st.text_input("Enter your question: ")

    if st.button("Generate"):
        if question:
            text = retrieve_text_from_pdf(pdf_path)
            context = text + "\n\n" + question
            ai = genai.GenerativeModel(model_name=model_name)
            response = ai.generate_content(context)  
            st.subheader("Question:")
            st.write(question)
            st.subheader("Answer:")
            st.write(response.text)
        else:
            st.warning("Please enter your question.")

if __name__ == "__main__":
    main()
