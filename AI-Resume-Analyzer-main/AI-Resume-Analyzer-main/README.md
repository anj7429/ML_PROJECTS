# Hello
# AI Resume Analyzer 📝
The AI Resume Analyzer is an intelligent web-based tool designed to help job seekers evaluate and enhance their resumes by comparing them directly against a specific job description. Leveraging advanced AI models, this tool simulates how Applicant Tracking Systems (ATS) and recruiters assess your resume for relevance, alignment, and suitability for a role. Completely in a single Python file.

Watch our [Youtube Tutorial](https://youtu.be/XfoHr9GivCs) for a Demo and detailed explanation of installation steps and code.

## 🔍 What Does This Project Do?
### 1. Resume Text Extraction
Users upload their resumes in PDF format, and the system automatically extracts the raw text for further analysis.

### 2. Job Description Input
The user provides the job description for the position they are targeting. This sets the criteria against which the resume will be evaluated.

### 3. ATS Similarity Score
Using Sentence Transformers (BERT-based model), the tool calculates a similarity score between the resume and the job description. This score reflects how well the resume matches keywords, context, and requirements typically scanned by ATS software.

### 4. AI-Powered Resume Evaluation
With the help of Groq's Llama-based LLM, the tool generates a detailed, human-readable evaluation report. The AI analyzes various factors such as skills, experience, and qualifications, assigning a score (out of 5) for each aspect and using emojis (✅, ❌, ⚠️) to quickly highlight strengths and gaps.

### 5. Actionable Feedback
The AI not only scores your resume but also provides personalized suggestions on how to improve it, helping candidates refine their applications before submission.

### 6. Downloadable Report
Users can easily download the detailed analysis for reference, making it convenient to track and implement the suggested changes.


---

### 🎯 **Why Use This Tool?**

- **Optimize for ATS**: Understand how your resume fares in automated screenings.
- **Get AI Insights**: Receive professional-quality feedback without hiring a consultant.
- **Improve Success Rate**: Apply data-driven improvements to increase your chances of getting shortlisted.


This project is perfect for job seekers who want to make sure their resumes are tailored to specific roles, career coaches looking for efficient feedback tools, or developers seeking to explore AI’s capabilities in HR-tech workflows.


# ⚙️ Installation Steps

Follow these steps to set up and run the **AI Resume Analyzer** locally:


Make sure you have Python and Git installed.

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/Altoks-AI/AI-Resume-Analyzer.git
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

## Possible Changes you may want to make:

- Change the prompt in main.py file to get the results in the way you want.
- Embedding Model is "sentence-transformers/all-mpnet-base-v2" ,Change to the model you desire (Ex: BERT, SBERT,etc)
- Currently using Groq API and LLM model is "llama-3.3-70b-versatile", Change is model is removed or use other API's like OpenAI-GPT-4o model.
- Change the Title, Labels and other names and display formats according to your liking.


## Contact us :

- Join our [Discord Community](https://discord.com/invite/qbhACtUB)
- Our Company Website: [Altoks AI]( https://altoks.vercel.app/)

🔗 Follow us everywhere:
- [Linkedin](https://www.linkedin.com/in/altoks-ai/)
- [Instagram](https://www.instagram.com/altoks_ai/)
- [X (Twitter)](https://x.com/Altoks_AI)
