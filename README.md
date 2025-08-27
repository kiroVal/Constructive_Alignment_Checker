## Syllabi-Verification-Py-Model: Bloom's Taxonomy and OBE Alignment

This project, "Syllabi-Verification-Py-Model," is a Python-based application designed to analyze and verify a syllabus. Its primary function is to check if the syllabus's content is aligned with the principles of Bloom's Taxonomy and Outcome-Based Education (OBE).

## 🎓 Thesis Defense Resources

**For thesis defense preparation, see:**
- 📖 **[THESIS_DEFENSE_GUIDE.md](THESIS_DEFENSE_GUIDE.md)** - Complete Q&A preparation guide
- 🐍 **[thesis_defense_demo.py](thesis_defense_demo.py)** - Standalone demo script (no trained models required)
- ⚙️ **[setup_defense.sh](setup_defense.sh)** - Automated environment setup
- 📋 **[requirements.txt](requirements.txt)** - Python dependencies

### Quick Defense Setup
```bash
# Run the setup script
./setup_defense.sh

# Or manually run the demo
python thesis_defense_demo.py
```

## Tools Used

+ python-docx  
  - Used to read and extract content from Word (.docx) syllabus files, focusing on tables such as Learning Outcomes, Deliverables, and Assessments.

+ pandas  
  - Handles data organization, cleaning, and exporting. It converts extracted data into CSV files and also combines multiple outputs into a master dataset.

+ glob and os  
  - Manage file handling tasks such as locating syllabus files in folders and creating output directories.

+ re (Regular Expressions)  
  - Cleans and standardizes text in headers, ensuring that different formats (e.g., "Assessment" vs "Assessments") are treated consistently.

## Data Processing

+ Automated Syllabus Reading:  
  - The system can process multiple syllabi saved in Word (.docx) format. It automatically identifies and extracts important sections such as Learning Outcomes, Deliverables, and Assessments.

+ Consistent Data Extraction:  
  - Even if instructors use different formats or slightly different wording in their tables, the system can recognize and standardize them into a uniform structure. This ensures that syllabi   from different departments or courses can be compared consistently.

+ Spreadsheet-Friendly Outputs:  
  - Each syllabus is converted into a clean CSV file (similar to an Excel sheet). This makes the information easy to review, share, or further analyze without needing technical knowledge.

+ Combined Master Dataset:  
  - The system merges all the processed syllabi into one master file. This provides a consolidated view of all syllabi, making it easier to spot patterns, gaps, or alignment issues across courses and programs.

+ Time-Saving Automation:  
  - Instead of manually going through each syllabus, the tool processes them in bulk. This reduces human error and saves significant time for faculty and administrators.



