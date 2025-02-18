import os
import spacy
import pandas as pd
from pdfminer.high_level import extract_text
import matplotlib.pyplot as plt

# Load SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Define required skills for the job position (modifiable)
REQUIRED_SKILLS = {"Python", "English", "RPA", "SQL", "Uipath", "NLP", "Power BI"}

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file"""
    return extract_text(pdf_path)

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
    # Extract text from PDF file
    text = extract_text_from_pdf(file_path)
    
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
resume_files = ["Resume.pdf"]
results = [analyze_resume(file) for file in resume_files]

# Convert results to DataFrame for better visualization
df = pd.DataFrame(results)

# Display results
print(df.to_string(index=False))
