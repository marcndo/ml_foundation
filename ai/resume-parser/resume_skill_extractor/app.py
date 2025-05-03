import fitz  # PyMuPDF
import gradio as gr
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI-compatible client for Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def extract_text_from_pdf(file_bytes):
    try:
        with fitz.open(stream=file_bytes, filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        return f"Failed to read PDF: {e}"


def summarize_resume_with_llm(text):
    if "Failed to read PDF" in text:
        return text  # Propagate the error message

    prompt = f"""
You're an expert recruiter reviewing resumes.

Analyze the text below and summarize:
- Key technical skills
- Soft skills
- Professional characteristics (e.g., leadership, adaptability)

Format the response with bullet points under each heading.

Resume:
{text}
    """
    try:
        response = client.chat.completions.create(
            model="mistral-saba-24b",  # Change if using a different model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error communicating with the LLM: {e}"


def analyze_resume(file_bytes):
    resume_text = extract_text_from_pdf(file_bytes)
    if not resume_text or not resume_text.strip():
        return "Could not extract any text from the resume. Please upload a clearer PDF."
    return summarize_resume_with_llm(resume_text)


iface = gr.Interface(
    fn=analyze_resume,
    inputs=gr.File(type="binary", label="Upload Resume (PDF)"),
    outputs=gr.Textbox(label="Resume Summary"),
    title="🧠 Resume Analyzer with LLM",
    description="Upload your resume and get a summarized view of your key strengths, skills, and professional qualities using Groq's LLM (Mixtral)."
)

if __name__ == "__main__":
    iface.launch(share=True)