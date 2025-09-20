# Constructive Alignment Checker (CAC)

## Overview
The Constructive Alignment Checker (`CAC.ipynb`) automates the evaluation of course syllabi by analyzing the alignment between learning outcomes, deliverables, and assessments. It uses semantic similarity and Bloom’s taxonomy classification to identify and report alignment issues.

---

## Tech Requirements

- **Operating System:** Linux (tested on Ubuntu 24.04.2 LTS)
- **Python:** 3.8+
- **Jupyter Notebook:** Recommended for interactive execution
- **Required Python Libraries:**
  - torch
  - transformers
  - pandas
  - numpy
  - scikit-learn

---

## Tools & Techniques

- **PyTorch:** For loading and running trained model weights.
- **Transformers (HuggingFace):** For semantic similarity and Bloom’s taxonomy classification using DistilBERT.
- **pandas & numpy:** For data manipulation and analysis.
- **scikit-learn:** For similarity calculations.
- **Custom Rule-Based Logic:** For alignment scoring and feedback.

### Large Language Models (LLM)
Using large language models to analyze the structure and semantics of syllabus content enables the model to identify Bloom's taxonomy verbs across Learning Outcomes (LOs), Deliverables/Outputs (DOs), and Assessments/Tasks (ATs). This approach supports contextual interpretation even when syllabi use varied or implicit phrasing.

---

## Step-by-Step Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kiroVal/Syllabi-Verification-Py-Model.git
   cd Syllabi-Verification-Py-Model
   ```

2. **Set Up Python Environment**
   - (Recommended) Create a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install dependencies:
     ```bash
     pip install torch transformers pandas numpy scikit-learn
     ```

3. **Prepare Data and Models**
   - Place your syllabus data CSV in the expected path (e.g., `dataset/test/test.csv`).
   - Ensure trained model weights are available:
     - `model/bloombert_model.pt`
     - `model/obert_distilbert.pt`
   - Place Bloom’s verbs CSV in `dataset/blooms_verbs/blooms_verbs.csv`.

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```
   - Open `Model Development/CAC.ipynb`.

5. **Run the Notebook Cells Sequentially**
   - **Load Models:** Loads trained weights for semantic and Bloom’s taxonomy models.
   - **Load Data:** Imports syllabus data for analysis.
   - **Data Preparation:** Extracts relevant columns for processing.
   - **Semantic Alignment:** Calculates semantic similarity between outcomes, deliverables, and assessments.
   - **Bloom’s Taxonomy Alignment:** Classifies text into Bloom’s levels and checks for verb usage.
   - **Alignment Scoring:** Applies rule-based logic to determine alignment status.
   - **Results Display:** Shows alignment results and scores for each syllabus entry.

6. **Interpret Results**
   - Review the output tables for alignment status.
   - Use the feedback and scores to improve syllabus design.

---

## Notes

- If you encounter errors, verify that all file paths and model weights are correct.
- You can adjust alignment thresholds and rules in the notebook to fit your evaluation criteria.
- For advanced feedback, consider integrating with a generative model (e.g., Ollama) as described in the documentation.

---

## Contact

For questions or support, open an issue in the repository or contact the maintainer.
