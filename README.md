# 📄 Automated Resume Analyzer with NLP 🤖  
**An AI-powered tool to extract and evaluate skills from resumes using NLP and Machine Learning.**  

## 📝 Overview  
This project automates the **resume screening process** by:  
✅ Extracting text from **PDF and Word (.docx) files**  
✅ Identifying **skills** using **Natural Language Processing (NLP)**  
✅ **Comparing skills** with job requirements  
✅ **Classifying candidates** based on skill relevance  

This tool is ideal for **HR Tech companies, recruiters, and job portals** to streamline resume screening efficiently.  

---  

## 🚀 Features  
🔹 **PDF & Word (.docx) Support** – Reads resumes from multiple formats  
🔹 **AI-based Skill Extraction** – Uses **SpaCy NLP** and **pre-trained AI models** to detect skills  
🔹 **Candidate Classification** – Automatically ranks candidates based on job requirements  
🔹 **Batch Processing** – Analyze multiple resumes in one run  
🔹 **HR System Integration** – Connects with ATS (Applicant Tracking Systems) via API  

---  

## 🛠️ Technologies Used  
- **Python** 🐍  
- **SpaCy** (Natural Language Processing)  
- **pdfminer.six** (Extract text from PDFs)  
- **python-docx** (Extract text from Word files)  
- **Pandas** (Data handling & visualization)  
- **FastAPI** (For HR system integration)  

---  

## 📦 Installation  

### 1️⃣ Clone the Repository  
```bash  
git clone https://github.com/YOUR_GITHUB_USERNAME/resume-analyzer.git  
cd resume-analyzer  
```  

### 2️⃣ Install Dependencies  
```bash  
pip install -r requirements.txt  
python -m spacy download en_core_web_sm  
```  

---  

## ⚡ How to Use  

### 1️⃣ Add Resumes (PDF or Word) to the Project Folder  
Place resume files (**.pdf** or **.docx**) inside the project directory.  

### 2️⃣ Edit the List of **Required Skills** (Optional)  
Modify the `REQUIRED_SKILLS` set in the script to match job criteria:  
```python  
REQUIRED_SKILLS = {"Python", "Machine Learning", "Data Science", "SQL", "TensorFlow", "NLP", "Power BI"}  
```  

### 3️⃣ Run the Script  
```bash  
python analyze_resumes.py  
```  

### 4️⃣ View Results  
The script will output a **table** with:  
- **Extracted skills**  
- **Candidate classification (Approved/Consider/Rejected)**  

---  

## 🖼️ Example Output  
| File         | Skills Found                      | Classification                  |  
|-------------|---------------------------------|-------------------------------|  
| candidate1.pdf | Python, SQL, Machine Learning | **Approved - Strong Candidate** |  
| candidate2.docx | Power BI                      | **Rejected - Few skills found** |  

---  

## 🎯 Use Cases  
✔ **HR & Recruiting Agencies** – Automate candidate screening  
✔ **Job Portals** – Enhance job-matching accuracy  
✔ **AI & NLP Developers** – Extend with more advanced NLP models  


---  

## 🤝 Contributing  
Feel free to **fork** this project, improve it, and submit **pull requests!** 🚀  
