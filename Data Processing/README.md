# Syllabi Batch Docx to CSV Notebook
This notebook helps you extract tables from multiple Word documents (.docx) and save them as CSV files, then combine those CSVs into a single file. It's designed for non-technical users who need to process syllabi or similar documents in bulk.

## Prerequisites
* Windows PC (recommended)
* Python 3.8+ installed
* Jupyter Notebook installed (comes with Anaconda, or install via pip)

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
     1. Extract tables from Word files to CSVs
     2. Combine all CSVs into one file
   * The notebook will print progress and save output files in the specified folders.
### Output
* Individual CSV files for each Word document (in your output folder)
* One combined CSV file with all data (in the combined output folder)
### Troubleshooting
* If you see errors about missing libraries, run the install commands above.
* Make sure your folder paths are correct and use forward slashes (/) or double backslashes (\\).

# Syllabi Batch CSV to Cleaned Data

