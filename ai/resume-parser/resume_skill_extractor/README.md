# 🧠 Resume Analyzer with Groq LLM

A smart resume parsing tool powered by Groq-hosted Large Language Models (LLMs) that extracts and summarizes key skills, soft skills, and professional traits from PDF resumes.

---

## 🚨 Problem Statement

Recruiters face the challenge of:
- 🔍 Manually extracting relevant information from resumes.
- ⚠️ Overlooking key skills due to volume or formatting inconsistencies.
- 🎯 Inconsistent evaluation criteria during screening.

This project addresses these problems by:
- 🧾 Automatically parsing resumes in PDF format.
- 🧠 Leveraging LLMs to extract key technical and soft skills.
- 🖥️ Displaying results in a structured, user-friendly format.

---

## 🎯 Objectives

- ✅ Upload resume as a PDF.
- ✅ Parse resume text using `PyMuPDF`.
- ✅ Analyze content using Groq’s `mistral-saba-24b` LLM.
- ✅ Return summarized results via a Gradio interface.
- ✅ Deploy on Hugging Face Spaces.

---

## 🚀 Live Demo
[👉 Try it on Hugging Face Spaces](https://marcndo-resume-analyzer-groq.hf.space/?__theme=system&deep_link=UoLDIusr4Ks)

---

## 🧰 Tech Stack

| Layer         | Tool/Library                              |
|---------------|--------------------------------------------|
| UI Frontend   | [Gradio](https://gradio.app)               |
| PDF Parsing   | [PyMuPDF](https://pymupdf.readthedocs.io) |
| LLM Backend   | [Groq API](https://console.groq.com)       |
| Deployment    | [Hugging Face Spaces](https://huggingface.co/spaces) |
| Secrets Mgmt  | `.env` for local, Secrets tab for HF Spaces |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://huggingface.co/spaces/your-username/resume-analyzer-groq
d resume-analyzer-groq```
