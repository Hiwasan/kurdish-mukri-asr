#!/usr/bin/env python3
"""
Deep Analysis of data_prep.py for Iranian Language Adaptation
"""
from pathlib import Path

def analyze_data_prep_structure():
    """Analyze the data preparation script in detail"""
    print("=" * 60)
    print("DEEP DATA_PREP.PY ANALYSIS")
    print("=" * 60)
    
    data_prep_path = Path(r"C:\CRF\espnet-wav2gloss\espnet-wav2gloss\egs2\wav2gloss\asr1\local\data_prep.py")
    
    if not data_prep_path.exists():
        print("❌ data_prep.py not found")
        return
    
    print("📖 Reading data_prep.py...")
    
    with open(data_prep_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Analyze language list
    print("\n🔤 LANGUAGES SUPPORTED:")
    print("-" * 40)
    
    # Extract the LANGUAGES tuple
    lines = content.split('\n')
    in_languages = False
    languages = []
    
    for line in lines:
        if 'LANGUAGES = (' in line:
            in_languages = True
            continue
        if in_languages:
            if ')' in line:
                break
            if '"' in line or "'" in line:
                lang = line.strip().strip('",')
                if lang:
                    languages.append(lang)
    
    print(f"📊 Total languages: {len(languages)}")
    print("📋 Sample languages:")
    for i, lang in enumerate(languages[:10]):
        print(f"   {i+1:2d}. {lang}")
    print(f"   ... and {len(languages)-10} more")
    
    # 2. Analyze data structure and functions
    print("\n🔧 DATA PREPARATION FUNCTIONS:")
    print("-" * 40)
    
    functions = []
    for i, line in enumerate(lines):
        if line.strip().startswith('def '):
            func_name = line.strip().split('def ')[1].split('(')[0]
            functions.append(func_name)
            # Get function purpose from docstring or comments
            for j in range(i+1, min(i+5, len(lines))):
                if '"""' in lines[j] or "'''" in lines[j] or '#' in lines[j]:
                    doc_line = lines[j].strip()
                    if doc_line and not doc_line.startswith('def '):
                        print(f"   📝 {func_name}: {doc_line}")
                        break
            else:
                print(f"   📝 {func_name}")
    
    # 3. Look for FIELDWORK dataset structure
    print("\n📚 FIELDWORK DATASET STRUCTURE:")
    print("-" * 40)
    
    fieldwork_refs = [line for line in lines if 'fieldwork' in line.lower()]
    if fieldwork_refs:
        for ref in fieldwork_refs[:10]:
            if len(ref.strip()) < 100:
                print(f"   🔍 {ref.strip()}")
    else:
        print("   ❌ No explicit FIELDWORK references found")
    
    # 4. Analyze data format expectations
    print("\n💾 EXPECTED DATA FORMAT:")
    print("-" * 40)
    
    # Look for file extensions and data structure
    key_terms = ['.wav', '.txt', 'json', 'utterance', 'transcription', 'gloss', 'translation']
    for term in key_terms:
        term_refs = [line for line in lines if term in line.lower()]
        if term_refs:
            print(f"   📄 {term.upper()}:")
            for ref in term_refs[:2]:
                clean_ref = ref.strip()
                if len(clean_ref) < 80 and not clean_ref.startswith('#'):
                    print(f"      - {clean_ref}")
    
    # 5. Iranian language adaptation plan
    print("\n🎯 IRANIAN LANGUAGE ADAPTATION PLAN:")
    print("-" * 40)
    
    adaptation_steps = [
        "1. ADD LANGUAGE CODES: Add 'balochi', 'kurdish_sorani', 'kurdish_kurmanji' to LANGUAGES tuple",
        "2. PREPARE DATA: Create FIELDWORK-style data directories with:",
        "   - WAV files (audio)",
        "   - JSON files with transcriptions, glosses, translations", 
        "   - Proper train/dev/test splits",
        "3. HANDLE SCRIPT: Ensure proper handling of Persian/Arabic script if needed",
        "4. TOKENIZATION: May need custom tokenization for Kurdish/Balochi",
        "5. TEST PIPELINE: Run data preparation with sample data first"
    ]
    
    for step in adaptation_steps:
        print(f"   {step}")

def generate_iranian_language_template():
    """Generate a template for adding Iranian languages"""
    print("\n" + "=" * 60)
    print("IRANIAN LANGUAGE TEMPLATE")
    print("=" * 60)
    
    template = """
# Template for adding Iranian languages to data_prep.py

# 1. Add to LANGUAGES tuple (around line 7):
LANGUAGES = (
    # ... existing languages ...
    "balochi",
    "kurdish_sorani", 
    "kurdish_kurmanji",
    # ... rest of existing languages ...
)

# 2. Expected directory structure for each language:
# fieldwork_data/
# ├── balochi/
# │   ├── train/
# │   │   ├── audio/
# │   │   │   └── *.wav files
# │   │   ├── transcription.txt
# │   │   ├── gloss.txt  
# │   │   └── translation.txt
# │   ├── dev/
# │   └── test/
# ├── kurdish_sorani/
# └── kurdish_kurmanji/

# 3. Data format example (JSON):
# {
#   "utterance_id": "balochi_train_001",
#   "audio_path": "audio/balochi_train_001.wav",
#   "transcription": "من شهْرِ ستّار ءَ",
#   "underlying_form": "man šahre stār a",
#   "gloss": "1SG city Star COP",
#   "translation": "I am from Star City"
# }

# 4. Special considerations for Iranian languages:
#    - Right-to-left script (Persian/Arabic) for some transcriptions
#    - Possible need for custom tokenization
#    - Dialect variations (especially for Kurdish)
"""
    
    print(template)

def check_current_data_structure():
    """Check if there's any existing data structure"""
    print("\n" + "=" * 60)
    print("CURRENT DATA STRUCTURE CHECK")
    print("=" * 60)
    
    # Check if there's a data directory or sample data
    base_path = Path(r"C:\CRF\espnet-wav2gloss\espnet-wav2gloss\egs2\wav2gloss")
    
    data_dirs = list(base_path.rglob("data*")) + list(base_path.rglob("*fieldwork*"))
    
    if data_dirs:
        print("✅ Found potential data directories:")
        for dir_path in data_dirs[:5]:
            if dir_path.is_dir():
                print(f"   📁 {dir_path.relative_to(base_path)}")
                try:
                    items = list(dir_path.iterdir())[:3]
                    for item in items:
                        print(f"      └── {item.name}")
                except:
                    pass
    else:
        print("❌ No existing data directories found")
        print("   We'll need to create the FIELDWORK data structure from scratch")

def main():
    """Main analysis function"""
    print("🚀 STEP 5: DATA PREPARATION DEEP ANALYSIS")
    print("💡 Understanding how to adapt for Iranian languages\n")
    
    analyze_data_prep_structure()
    generate_iranian_language_template()
    check_current_data_structure()
    
    print("\n" + "=" * 60)
    print("🎯 NEXT ACTIONS")
    print("=" * 60)
    print("1. ✅ Set up environment (run setup_environment.ps1)")
    print("2. 📊 Study the actual FIELDWORK dataset format")
    print("3. 💾 Prepare sample Balochi/Kurdish data")
    print("4. 🔧 Modify data_prep.py for Iranian languages")
    print("5. 🧪 Test the data preparation pipeline")
    print("\n📝 We now understand exactly what needs to be modified!")

if __name__ == "__main__":
    main()