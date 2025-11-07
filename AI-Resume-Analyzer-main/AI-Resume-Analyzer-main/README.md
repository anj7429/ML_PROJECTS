# 🧠 AI Resume Analyzer

An **AI-powered Resume Analyzer** built with **Streamlit** that evaluates how well a candidate’s resume aligns with a given job description.  
It uses **BERT embeddings** for similarity scoring and **Groq’s LLM (Llama 3.3 70B)** for detailed AI-based feedback.

---

## 🚀 Features

✅ Extracts text from uploaded **PDF resumes**  
✅ Calculates **ATS similarity score** using `SentenceTransformer`  
✅ Generates an **AI-driven analysis report** using **Groq API**  
✅ Highlights strong and weak alignment points (✅ ❌ ⚠️)  
✅ Provides **improvement suggestions** for better job matching  
✅ Clean **Streamlit UI** with download option for the report  

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| Text Extraction | pdfminer.six |
| Embedding Model | SentenceTransformer (`all-mpnet-base-v2`) |
| AI Analysis | Groq LLM (Llama 3.3-70B-Versatile) |
| Similarity Metric | Cosine Similarity (scikit-learn) |
| Environment Variables | python-dotenv |

---
# ⚙️ Installation Steps

Follow these steps to set up and run the **AI Resume Analyzer** locally:


Make sure you have Python and Git installed.

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/anj7429/AI-Resume-Analyzer.git
```
```
cd FolderName
```

### 2️⃣ Set Up a Virtual Environment
```
python -m venv myenv
```
```
./myenv/Scripts/activate
```

### 3️⃣ Install Dependencies
Make sure you have pip updated, then install all required packages:
```
pip install -r requirements.txt
```

### 4️⃣ Set Up Your .env File
Create a .env file in the root directory and add your Groq API key from [Groq](https://groq.com/) 

```
GROQ_API_KEY=your_groq_api_key_here
```

### 5️⃣ Run the Streamlit App
Launch the app locally using Streamlit:
```
streamlit run main.py
```
### 6️⃣ Open in Browser
Once the app starts, it will automatically open in your default web browser at:
```
http://localhost:8501
```
---
✅ Now you’re all set!
Upload a resume, paste a job description, and let the AI analyze your resume for job-fit and provide suggestions. 







