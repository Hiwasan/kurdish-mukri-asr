#!/usr/bin/env python3
"""
ESPNet WAV2GLOSS Project Analysis Pipeline
Step 1: Project Structure Exploration
Updated with correct folder names
"""
import os
import glob
import json
from pathlib import Path

def analyze_all_projects(base_path):
    """Analyze all three projects structure"""
    print("=" * 60)
    print("WAV2GLOSS PROJECTS ANALYSIS")
    print("=" * 60)
    
    base_path = Path(base_path)
    
    projects = {
        "espnet-wav2gloss": "Main ESPNet implementation (end-to-end models)",
        "finetune_owsm-main": "OWSM model fine-tuning", 
        "or-tools-stable": "Data splitting with knapsack solver"
    }
    
    print("📁 ALL PROJECTS OVERVIEW:")
    print("-" * 40)
    
    for project, description in projects.items():
        project_path = base_path / project
        if project_path.exists():
            print(f"✅ {project}: {description}")
            # Count main file types
            py_files = list(project_path.rglob("*.py"))
            yaml_files = list(project_path.rglob("*.yaml")) + list(project_path.rglob("*.yml"))
            print(f"   └── Python: {len(py_files)} files, Config: {len(yaml_files)} files")
        else:
            print(f"❌ {project}: NOT FOUND")
    
    return True

def analyze_espnet_structure(project_path):
    """Analyze the ESPNet project structure step by step"""
    print("\n" + "=" * 60)
    print("ESPNet WAV2GLOSS Detailed Analysis")
    print("=" * 60)
    
    project_path = Path(project_path)
    
    # 1. Check if path exists
    if not project_path.exists():
        print(f"❌ Error: Path {project_path} does not exist!")
        return False
    
    print(f"📁 Project location: {project_path}")
    print(f"🔍 Analyzing structure...\n")
    
    # 2. List main directory contents
    print("📋 MAIN DIRECTORY CONTENTS:")
    print("-" * 40)
    items = list(project_path.iterdir())
    for item in sorted(items, key=lambda x: (x.is_file(), x.name)):
        if item.is_dir():
            print(f"📁 {item.name}/")
        else:
            print(f"📄 {item.name}")
    
    # 3. Look for critical files
    print("\n🔍 KEY FILES SEARCH:")
    print("-" * 40)
    
    key_files = {
        "README": ["README.md", "README.txt", "README"],
        "Requirements": ["requirements.txt", "environment.yml", "setup.py", "pyproject.toml"],
        "Configuration": ["*.yaml", "*.yml", "*.json"],
        "Scripts": ["train*.py", "run*.py", "main*.py"]
    }
    
    found_files = {}
    
    for category, patterns in key_files.items():
        found_files[category] = []
        for pattern in patterns:
            matches = list(project_path.glob(pattern))
            found_files[category].extend(matches)
            
            # Also check first level of subdirectories
            subdir_matches = list(project_path.glob(f"*/{pattern}"))
            found_files[category].extend(subdir_matches)
    
    # Display found files
    for category, files in found_files.items():
        if files:
            print(f"\n✅ {category}:")
            for file in sorted(files):
                print(f"   - {file.relative_to(project_path)}")
        else:
            print(f"\n❌ {category}: No files found")
    
    # 4. Look for WAV2GLOSS specific directories
    print("\n🔍 WAV2GLOSS SPECIFIC DIRECTORIES:")
    print("-" * 40)
    
    wav2gloss_dirs = [
        "egs2", "egs", "examples",  # ESPNet typically uses egs2 for recipes
        "wav2gloss", "fieldwork",   # WAV2GLOSS specific
        "data", "datasets",         # Data directories
        "src", "espnet", "scripts"  # Source code directories
    ]
    
    for dir_name in wav2gloss_dirs:
        dir_path = project_path / dir_name
        if dir_path.exists():
            print(f"✅ Found: {dir_name}/")
            # Show first few items in this directory
            try:
                items = list(dir_path.iterdir())[:3]  # Show only first 3
                for item in items:
                    item_type = "📁" if item.is_dir() else "📄"
                    print(f"   {item_type} {item.name}")
            except Exception as e:
                print(f"   └── (Error reading: {e})")
        else:
            print(f"❌ Missing: {dir_name}/")
    
    # 5. Check for Iranian language support
    print("\n🔤 IRANIAN LANGUAGE SUPPORT CHECK:")
    print("-" * 40)
    
    iranian_languages = ["balochi", "kurdish", "kurmanji", "sorani", "persian", "farsi", "iranian"]
    found_languages = []
    
    # Search in configuration files
    config_files = list(project_path.rglob("*.yaml")) + list(project_path.rglob("*.yml"))
    
    for config_file in config_files[:5]:  # Check first 5 config files
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                for lang in iranian_languages:
                    if lang in content:
                        found_languages.append((lang, config_file.relative_to(project_path)))
        except Exception as e:
            pass
    
    if found_languages:
        print("✅ Found references to Iranian languages:")
        for lang, file_path in found_languages:
            print(f"   - '{lang}' in {file_path}")
    else:
        print("❌ No Iranian language references found in config files")
        print("   We'll need to add support for Balochi/Kurdish dialects")
    
    return True

def generate_next_steps():
    """Generate clear next steps based on analysis"""
    print("\n🎯 NEXT STEPS FOR IRANIAN LANGUAGES:")
    print("-" * 40)
    
    steps = [
        "1. ✅ Project Structure Analysis (Current Step)",
        "2. 📚 Read README files for installation instructions", 
        "3. 🐍 Set up Python environment with required dependencies",
        "4. 🔍 Locate data preparation scripts for FIELDWORK dataset",
        "5. 📝 Identify where to add Balochi/Kurdish language configurations",
        "6. 💾 Prepare sample data for Iranian languages",
        "7. 🚀 Test training pipeline with small dataset",
        "8. 🔧 Adapt model for low-resource language characteristics"
    ]
    
    for step in steps:
        print(step)

if __name__ == "__main__":
    # Set your base path
    base_path = r"C:\CRF"
    
    print("🚀 Starting WAV2GLOSS Projects Analysis...")
    print("💡 This is Step 1: Understanding All Project Structures")
    print("💡 We'll proceed step by step\n")
    
    # Analyze all projects first
    analyze_all_projects(base_path)
    
    # Then do detailed analysis of ESPNet
    espnet_path = r"C:\CRF\espnet-wav2gloss"
    success = analyze_espnet_structure(espnet_path)
    
    if success:
        generate_next_steps()
        print("\n✅ Step 1 Complete! Ready for Step 2: README Analysis")
    else:
        print("\n❌ Please check the project path and try again")