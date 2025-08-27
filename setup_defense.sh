#!/bin/bash
# Thesis Defense Setup Script
# This script prepares your environment for the thesis defense

echo "🎓 Setting up Thesis Defense Environment..."
echo "=========================================="

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p model
mkdir -p dataset/test
mkdir -p dataset/blooms_verbs
mkdir -p results
mkdir -p backup

# Set up Python environment
echo "🐍 Setting up Python environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment and install dependencies
echo "📦 Installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

# Copy sample data if available
echo "📊 Setting up sample data..."
if [ -f "Data Processing/course_outline.csv" ]; then
    cp "Data Processing/course_outline.csv" "dataset/test/test.csv"
    echo "✅ Test data copied"
fi

if [ -f "Datasets/combined_and_cleaned/blooms_taxonomy_cleaned_data.csv" ]; then
    cp "Datasets/combined_and_cleaned/blooms_taxonomy_cleaned_data.csv" "dataset/blooms_verbs/blooms_verbs.csv"
    echo "✅ Bloom's verbs data copied"
fi

# Test the demo script
echo "🧪 Testing demo script..."
python thesis_defense_demo.py > results/demo_output.txt 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Demo script runs successfully"
    echo "📄 Output saved to results/demo_output.txt"
else
    echo "❌ Demo script failed - check the output"
fi

# Create backup of important files
echo "💾 Creating backup..."
cp -r "Model Development" backup/
cp -r "Data Processing" backup/
cp thesis_defense_demo.py backup/
cp THESIS_DEFENSE_GUIDE.md backup/
echo "✅ Backup created in backup/ directory"

echo ""
echo "🎯 Defense Environment Ready!"
echo "=============================="
echo "✅ Dependencies installed"
echo "✅ Demo script tested"
echo "✅ Sample data prepared"
echo "✅ Backup created"
echo ""
echo "🚀 You're ready for your thesis defense!"
echo "   Run: python thesis_defense_demo.py"
echo "   Read: THESIS_DEFENSE_GUIDE.md"
echo ""
echo "Good luck! 🍀"