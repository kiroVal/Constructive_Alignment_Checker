#!/usr/bin/env python3
"""
Thesis Defense Helper for Syllabi Verification Python Model
============================================================

This script demonstrates the key components of the Constructive Alignment Checker (CAC)
for thesis defense purposes. It provides a simplified version of the main functionality
without requiring pre-trained model weights.

Author: Generated for thesis defense assistance
"""

import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

class ThesisDefenseDemo:
    """
    A simplified version of the CAC for demonstration purposes during thesis defense.
    This version uses TF-IDF for semantic similarity instead of requiring trained models.
    """
    
    def __init__(self):
        self.bloom_levels = {
            'remembering': ['remember', 'recall', 'list', 'identify', 'name', 'state', 'define'],
            'understanding': ['understand', 'explain', 'describe', 'summarize', 'interpret', 'classify'],
            'applying': ['apply', 'use', 'implement', 'demonstrate', 'solve', 'execute', 'operate'],
            'analyzing': ['analyze', 'examine', 'compare', 'contrast', 'categorize', 'differentiate'],
            'evaluating': ['evaluate', 'assess', 'judge', 'critique', 'justify', 'defend', 'support'],
            'creating': ['create', 'design', 'develop', 'construct', 'produce', 'generate', 'compose']
        }
        
    def extract_bloom_verbs(self, text):
        """Extract Bloom's taxonomy verbs from text"""
        if pd.isna(text):
            return []
        
        text_lower = text.lower()
        found_verbs = []
        
        for level, verbs in self.bloom_levels.items():
            for verb in verbs:
                if verb in text_lower:
                    found_verbs.append((verb, level))
        
        return found_verbs
    
    def classify_bloom_level(self, text):
        """Classify text into Bloom's taxonomy levels"""
        verbs = self.extract_bloom_verbs(text)
        if not verbs:
            return ['Undetected']
        
        levels = [verb[1] for verb in verbs]
        return list(set(levels))
    
    def calculate_semantic_similarity(self, texts):
        """Calculate semantic similarity using TF-IDF"""
        # Clean and preprocess texts
        clean_texts = []
        for text in texts:
            if pd.isna(text):
                clean_texts.append("")
            else:
                # Remove newlines and extra spaces
                clean_text = re.sub(r'\s+', ' ', str(text).replace('\\n', ' ')).strip()
                clean_texts.append(clean_text)
        
        if not any(clean_texts):
            return np.zeros((len(texts), len(texts)))
        
        # Use TF-IDF for similarity calculation
        vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        try:
            tfidf_matrix = vectorizer.fit_transform(clean_texts)
            similarity_matrix = cosine_similarity(tfidf_matrix)
            return similarity_matrix
        except:
            return np.zeros((len(texts), len(texts)))
    
    def determine_alignment(self, semantic_score, bloom_alignment):
        """Determine overall alignment based on semantic and Bloom's scores"""
        # Threshold for alignment (can be adjusted)
        semantic_threshold = 0.3
        
        semantic_aligned = semantic_score >= semantic_threshold
        bloom_aligned = bloom_alignment == 'Aligned'
        
        if semantic_aligned and bloom_aligned:
            return 'Aligned'
        elif semantic_aligned or bloom_aligned:
            return 'Partially Aligned'
        else:
            return 'Misaligned'
    
    def generate_feedback(self, semantic_aligned, bloom_aligned, overall_aligned):
        """Generate feedback based on alignment results"""
        if semantic_aligned and bloom_aligned:
            return "Excellent alignment! Both semantic content and cognitive levels are well-matched."
        elif semantic_aligned and not bloom_aligned:
            return "Good semantic alignment, but cognitive levels may need adjustment. Consider revising Bloom's verbs."
        elif not semantic_aligned and bloom_aligned:
            return "Cognitive levels are appropriate, but content relevance could be improved."
        else:
            return "Both semantic and cognitive alignment need improvement. Review content and learning objectives."
    
    def analyze_syllabus(self, df):
        """Main analysis function for syllabus data"""
        print("🎓 THESIS DEFENSE DEMO: Constructive Alignment Checker")
        print("=" * 60)
        
        # Prepare data
        if 'Learning Outcomes' not in df.columns:
            print("❌ Error: 'Learning Outcomes' column not found in the data")
            return None
            
        # Extract key columns
        learning_outcomes = df['Learning Outcomes'].fillna('')
        deliverables = df.get('Deliverables/\nOutcomes', df.get('Deliverables', '')).fillna('')
        assessments = df.get('Assessment', df.get('Assessments', '')).fillna('')
        
        print(f"📊 Analyzing {len(df)} syllabus entries...")
        print()
        
        # Combine all texts for similarity calculation
        all_texts = list(learning_outcomes) + list(deliverables) + list(assessments)
        similarity_matrix = self.calculate_semantic_similarity(all_texts)
        
        results = []
        num_rows = len(df)
        
        for i in range(num_rows):
            # Calculate semantic similarities
            lo_deliverable_sim = similarity_matrix[i, i + num_rows] if i + num_rows < len(similarity_matrix) else 0
            lo_assessment_sim = similarity_matrix[i, i + 2 * num_rows] if i + 2 * num_rows < len(similarity_matrix) else 0
            deliverable_assessment_sim = similarity_matrix[i + num_rows, i + 2 * num_rows] if (i + num_rows < len(similarity_matrix) and i + 2 * num_rows < len(similarity_matrix)) else 0
            
            overall_semantic_score = np.mean([lo_deliverable_sim, lo_assessment_sim, deliverable_assessment_sim])
            
            # Analyze Bloom's taxonomy
            lo_blooms = self.classify_bloom_level(learning_outcomes.iloc[i])
            deliverable_blooms = self.classify_bloom_level(deliverables.iloc[i])
            assessment_blooms = self.classify_bloom_level(assessments.iloc[i])
            
            # Determine Bloom's alignment (simplified)
            bloom_alignment = 'Aligned' if (set(lo_blooms) & set(deliverable_blooms)) or (set(lo_blooms) & set(assessment_blooms)) else 'Misaligned'
            
            # Overall alignment
            overall_alignment = self.determine_alignment(overall_semantic_score, bloom_alignment)
            
            # Generate feedback
            semantic_aligned = overall_semantic_score >= 0.3
            bloom_aligned = bloom_alignment == 'Aligned'
            feedback = self.generate_feedback(semantic_aligned, bloom_aligned, overall_alignment == 'Aligned')
            
            results.append({
                'Row': i + 1,
                'Learning Outcome': learning_outcomes.iloc[i][:100] + '...' if len(str(learning_outcomes.iloc[i])) > 100 else learning_outcomes.iloc[i],
                'Semantic Score': round(overall_semantic_score, 3),
                'Bloom Alignment': bloom_alignment,
                'Overall Alignment': overall_alignment,
                'LO Bloom Levels': ', '.join(lo_blooms),
                'Feedback': feedback
            })
        
        results_df = pd.DataFrame(results)
        return results_df
    
    def print_summary_statistics(self, results_df):
        """Print summary statistics for thesis defense"""
        if results_df is None:
            return
            
        print("\n📈 SUMMARY STATISTICS")
        print("-" * 40)
        
        total_entries = len(results_df)
        aligned = len(results_df[results_df['Overall Alignment'] == 'Aligned'])
        partially_aligned = len(results_df[results_df['Overall Alignment'] == 'Partially Aligned'])
        misaligned = len(results_df[results_df['Overall Alignment'] == 'Misaligned'])
        
        print(f"Total Entries: {total_entries}")
        print(f"Aligned: {aligned} ({aligned/total_entries*100:.1f}%)")
        print(f"Partially Aligned: {partially_aligned} ({partially_aligned/total_entries*100:.1f}%)")
        print(f"Misaligned: {misaligned} ({misaligned/total_entries*100:.1f}%)")
        
        avg_semantic_score = results_df['Semantic Score'].mean()
        print(f"\nAverage Semantic Score: {avg_semantic_score:.3f}")
        
        bloom_aligned = len(results_df[results_df['Bloom Alignment'] == 'Aligned'])
        print(f"Bloom's Taxonomy Alignment: {bloom_aligned}/{total_entries} ({bloom_aligned/total_entries*100:.1f}%)")

def load_sample_data():
    """Load and prepare sample data for demonstration"""
    try:
        # Try to load the actual course outline data
        df = pd.read_csv('dataset/test/test.csv', skiprows=1)  # Skip the first row with numbers
        print("✅ Successfully loaded course outline data")
        print(f"Columns found: {df.columns.tolist()}")
        return df
    except FileNotFoundError:
        print("⚠️  Course outline not found, creating sample data for demonstration...")
        # Create sample data if file not found
        sample_data = {
            'Learning Outcomes': [
                'Students will understand the basic concepts of programming',
                'Analyze different algorithmic approaches to problem solving',
                'Create and implement software solutions using Python',
                'Evaluate the effectiveness of different programming paradigms',
                'Apply object-oriented programming principles in software development'
            ],
            'Deliverables': [
                'Programming exercises and quizzes',
                'Algorithm analysis report',
                'Software project with documentation',
                'Comparative analysis presentation',
                'Object-oriented programming assignment'
            ],
            'Assessment': [
                'Written quiz on programming concepts',
                'Technical report on algorithm efficiency',
                'Project demonstration and code review',
                'Presentation with peer evaluation',
                'Practical programming exam'
            ]
        }
        return pd.DataFrame(sample_data)

def main():
    """Main function for thesis defense demonstration"""
    print("🎓 SYLLABI VERIFICATION PYTHON MODEL - THESIS DEFENSE DEMO")
    print("=" * 70)
    print("This demonstration shows the core functionality of the")
    print("Constructive Alignment Checker without requiring trained models.")
    print()
    
    # Load data
    df = load_sample_data()
    print(f"📄 Loaded {len(df)} syllabus entries for analysis")
    print()
    
    # Initialize the demo system
    demo = ThesisDefenseDemo()
    
    # Analyze the syllabus
    results = demo.analyze_syllabus(df)
    
    if results is not None:
        # Display results
        print("\n📊 ANALYSIS RESULTS")
        print("-" * 50)
        print(results.to_string(index=False))
        
        # Print summary statistics
        demo.print_summary_statistics(results)
        
        print("\n🎯 KEY THESIS CONTRIBUTIONS:")
        print("1. Automated syllabi analysis using NLP techniques")
        print("2. Bloom's taxonomy classification for learning objectives") 
        print("3. Semantic similarity assessment between course components")
        print("4. Rule-based alignment scoring with actionable feedback")
        print("5. Scalable solution for educational quality assurance")
        
        print("\n✨ Demo completed successfully! Good luck with your defense! ✨")
    else:
        print("❌ Analysis failed. Please check your data format.")

if __name__ == "__main__":
    main()