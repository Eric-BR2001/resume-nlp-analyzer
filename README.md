# 📄 Resume Analyzer with NLP 🤖  

## 📝 Overview  
This project automates the **resume screening process** by:  
✅ Extracting text from **PDF resumes**  
✅ Identifying **skills** using **Natural Language Processing (NLP)**  
✅ **Comparing skills** with job requirements  
✅ **Classifying candidates** based on skill relevance  

This tool is ideal for **HR Tech companies, recruiters, and job portals** to streamline resume screening efficiently.  

---  

## 🚀 Features  
🔹 **PDF Resume Support** – Reads resumes in **PDF format**  
🔹 **AI-based Skill Extraction** – Uses **SpaCy NLP** to detect skills  
🔹 **Candidate Classification** – Automatically ranks candidates based on job requirements  
🔹 **Batch Processing** – Analyze multiple resumes in one run  

---  

## 🛠️ Technologies Used  
- **Python** 🐍  
- **SpaCy** (Natural Language Processing)  
- **pdfminer.six** (Extract text from PDFs)  
- **Pandas** (Data handling & visualization)  
- **Matplotlib** (Data visualization)  

---  

## 📦 Installation  

### 1️⃣ Clone the Repository  
```bash  
git clone https://github.com/Eric-BR2001/resume-nlp-analyzer.git  
cd analyze_resumes
```  

### 2️⃣ Install Dependencies  
```bash  
pip install -r requirements.txt  
python -m spacy download en_core_web_sm  
```  

---  

## ⚡ How to Use  

### 1️⃣ Add Resumes (PDF format) to the Project Folder  
Place resume files (**.pdf**) inside the project directory.  

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
| candidate2.pdf | Power BI                      | **Rejected - Few skills found** |  

---  

## 🎯 Use Cases  
✔ **HR & Recruiting Agencies** – Automate candidate screening  
✔ **Job Portals** – Enhance job-matching accuracy  
✔ **AI & NLP Developers** – Extend with more advanced NLP models  

---  

## 📜 License  
This project is licensed under the **MIT License**.  

---  

## 🤝 Contributing  
Feel free to **fork** this project, improve it, and submit **pull requests!** 🚀
