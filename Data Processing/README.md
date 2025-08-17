# Syllabi Batch Docx to CSV Notebook
This notebook helps you extract tables from multiple Word documents (.docx) and save them as CSV files, then combine those CSVs into a single file. It's designed for non-technical users who need to process syllabi or similar documents in bulk.

## Prerequisites
* Windows PC (recommended).
* Python 3.8+ installed.
* Jupyter Notebook installed (comes with Anaconda, or install via pip).

### Step-by-Step Setup
1. Install Python and Jupyter Notebook
   * Download and install Anaconda (recommended for beginners), or
     Install Python from python.org and then run:
     ```bash
     pip install notebook
2. Download Required Libraries
   * Open the notebook and run the first cell to install the required library:
     ```bash
     %pip install python-docx
   * The notebook also uses pandas, which is included with Anaconda. If not, run:
     ```bash
     pip install pandas
3. Prepare Your Files
   * Create a folder for your Word documents (e.g., docx_folder).
   * Place all .docx files you want to process in this folder.
4. Update Folder Paths in the Notebook
   * In the notebook, set the input_folder and output_folder variables to match your folder locations. For example:
     ```bash
     input_folder = "C:/path/to/docx_folder"
     output_folder = "C:/path/to/csv_outputs"
   * Do the same for the combined CSV output folder if needed.
5. Run the Notebook
   * Run each cell in order:
     1. Extract tables from Word files to CSVs.
     2. Combine all CSVs into one file.
   * The notebook will print progress and save output files in the specified folders.
### Output
* Individual CSV files for each Word document (in your output folder)
* One combined CSV file with all data (in the combined output folder)
### Troubleshooting
* If you see errors about missing libraries, run the install commands above.
* Make sure your folder paths are correct and use forward slashes (/) or double backslashes (\\).

# Syllabi Batch CSV to Cleaned Data
This project processes batches of course syllabi in CSV format and extracts clean, structured data for analysis. It is designed for both technical and non-technical users who need to standardize and analyze syllabi information, including learning outcomes, deliverables, assessments, and associated weeks.

## Features
- Batch processing of multiple CSV syllabi files.
- Automatic extraction and cleaning of key columns.
- Week information extraction for each row.
- Combines results into a single, clean dataset.
- Easy to use with step-by-step instructions.

## Technical Requirements
- Windows OS (recommended).
- Python 3.8 or higher.
- VS Code (recommended for editing and running notebooks).
- Required Python packages: pandas, openpyxl, python-docx.

## Installation Steps

### 1. Install Python
- Download and install Python from [python.org](https://www.python.org/downloads/).
- Add Python to your system PATH during installation.

### 2. Install VS Code (Optional but recommended)
- Download and install Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/).

### 3. Clone or Download the Project
- Download the project files or clone the repository to your computer.

### 4. Install Required Python Packages
Open a terminal (PowerShell) in the project directory and run:
```powershell
pip install pandas openpyxl python-docx
```

### 5. Prepare Your Data
- Place your syllabi CSV files in the `csv_outputs` folder.
- (Optional) Place DOCX files in the `docx_folder` if you want to process Word documents.

### 6. Run the Data Processing Notebook
- Open `csvToCleanData.ipynb` in VS Code.
- Run the notebook cells step by step, or run all cells at once.
- The cleaned data will be saved in the `cleaned_csv` and `combined_csv` folders.

### Output
- Cleaned CSV files for each syllabus in `cleaned_csv/`
- Combined cleaned data in `combined_csv/combined_cleaned_syllabi_data.csv`

### Troubleshooting
- If you encounter encoding errors, the script will try alternative encodings automatically.
- Make sure your CSV files have headers for learning outcomes, deliverables, assessments, and (if available) week information.
