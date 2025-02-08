import os
import spacy
import pandas as pd
from pdfminer.high_level import extract_text
from docx import Document

# Load SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Define required skills for the job position (modifiable)
REQUIRED_SKILLS = {"Python", "Machine Learning", "Data Science", "SQL", "TensorFlow", "NLP", "Power BI"}

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file"""
    return extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    """Extracts text from a Word (.docx) file"""
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_skills(text):
    """Uses NLP to identify mentioned skills in the resume"""
    doc = nlp(text)
    words = set([token.text for token in doc if not token.is_stop and not token.is_punct])
    
    # Compare with the required skills list
    skills_found = words.intersection(REQUIRED_SKILLS)
    return skills_found

def classify_candidate(skills_found):
    """Classifies the candidate based on the detected skills"""
    if not skills_found:
        return "Rejected - No relevant skills found"
    
    score = len(skills_found) / len(REQUIRED_SKILLS)
    
    if score >= 0.7:
        return "Approved - Strong candidate"
    elif score >= 0.4:
        return "Consider - Some relevant skills present"
    else:
        return "Rejected - Few relevant skills found"

def analyze_resume(file_path):
    """Analyzes a resume and classifies the candidate"""
    # Determine file type and extract text accordingly
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        return {"File": os.path.basename(file_path), "Error": "Unsupported file format"}
    
    # Extract skills from the text
    skills_found = extract_skills(text)
    
    # Classify candidate
    classification = classify_candidate(skills_found)
    
    return {
        "File": os.path.basename(file_path),
        "Skills Found": ", ".join(skills_found),
        "Classification": classification
    }

# Test with sample resumes (replace with actual file paths)
resume_files = ["candidate1.pdf", "candidate2.docx"]
results = [analyze_resume(file) for file in resume_files]

# Convert results to DataFrame for better visualization
df = pd.DataFrame(results)

# Display results
import ace_tools as tools
tools.display_dataframe_to_user(name="Resume Analysis", dataframe=df)
