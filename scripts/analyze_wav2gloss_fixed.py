#!/usr/bin/env python3
"""
WAV2GLOSS Recipe Analysis - Complete Pipeline
Step 3-4: Complete analysis with environment setup plan
"""
import os
from pathlib import Path

def analyze_wav2gloss_structure(recipe_path):
    """Analyze the WAV2GLOSS recipe structure"""
    print("=" * 60)
    print("WAV2GLOSS RECIPE ANALYSIS")
    print("=" * 60)
    
    recipe_path = Path(recipe_path)
    
    if not recipe_path.exists():
        print(f"❌ WAV2GLOSS recipe not found at: {recipe_path}")
        return False
    
    print(f"📁 Recipe location: {recipe_path}")
    print("🔍 Note: This appears to be only ASR implementation")
    print("   The full WAV2GLOSS might need other components\n")
    
    # 1. List main recipe contents
    print("📋 MAIN RECIPE STRUCTURE:")
    print("-" * 40)
    
    items = list(recipe_path.iterdir())
    for item in sorted(items, key=lambda x: (x.is_file(), x.name)):
        if item.is_dir():
            print(f"📁 {item.name}/")
        else:
            print(f"📄 {item.name}")
    
    return True

def analyze_data_preparation(recipe_path):
    """Analyze data preparation scripts"""
    print("\n" + "=" * 60)
    print("DATA PREPARATION ANALYSIS")
    print("=" * 60)
    
    recipe_path = Path(recipe_path)
    local_path = recipe_path / "asr1" / "local"
    
    if local_path.exists():
        print("✅ Found local data preparation directory:")
        local_files = list(local_path.iterdir())
        for file in local_files:
            print(f"   📄 {file.name}")
            
            # Read data preparation scripts
            if file.name in ["data.sh", "data_prep.py"]:
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        lines = content.split('\n')
                        print(f"      First 10 lines of {file.name}:")
                        for i, line in enumerate(lines[:10]):
                            if line.strip() and not line.strip().startswith('#'):
                                print(f"        {i+1}: {line.strip()}")
                except Exception as e:
                    print(f"      Error reading: {e}")
    else:
        print("❌ No local data preparation directory found")

def analyze_configurations(recipe_path):
    """Analyze configuration files"""
    print("\n" + "=" * 60)
    print("CONFIGURATION ANALYSIS")
    print("=" * 60)
    
    recipe_path = Path(recipe_path)
    conf_path = recipe_path / "asr1" / "conf"
    
    if conf_path.exists():
        print("✅ Found configuration directory:")
        
        # Main conf files
        conf_files = list(conf_path.iterdir())
        for file in conf_files:
            if file.is_file():
                print(f"   📄 {file.name}")
        
        # Tuning configurations
        tuning_path = conf_path / "tuning"
        if tuning_path.exists():
            print(f"\n   🎛️  Tuning configurations:")
            tuning_files = list(tuning_path.glob("*.yaml"))
            for file in tuning_files:
                print(f"      📄 {file.name}")
                
                # Read config to understand model architecture
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'transformer' in content.lower() or 'conformer' in content.lower():
                            print(f"        └── Contains transformer/conformer architecture")
                        if 'xls' in content.lower() or 'wavlm' in content.lower():
                            print(f"        └── Uses pre-trained model: {file.name}")
                        if 'lang' in content.lower():
                            print(f"        └── Contains language settings")
                except:
                    pass

def analyze_training_script(recipe_path):
    """Analyze the main training script"""
    print("\n" + "=" * 60)
    print("TRAINING SCRIPT ANALYSIS")
    print("=" * 60)
    
    recipe_path = Path(recipe_path)
    run_script = recipe_path / "asr1" / "run.sh"
    
    if run_script.exists():
        print("✅ Found main training script: run.sh")
        try:
            with open(run_script, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
                # Extract key information
                print("\n🔍 Key training configuration:")
                key_patterns = ["train_set", "lang", "task", "asr_config", "lm_config"]
                
                for line in lines:
                    line_lower = line.lower()
                    if any(pattern in line_lower for pattern in key_patterns):
                        if len(line.strip()) < 100:  # Not too long
                            print(f"   📝 {line.strip()}")
                            
                # Find language and task variables
                print(f"\n🌍 Language and task setup:")
                for line in lines:
                    if 'lang=' in line or 'task=' in line:
                        print(f"   🔧 {line.strip()}")
                        
        except Exception as e:
            print(f"❌ Error reading run.sh: {e}")
    else:
        print("❌ No run.sh script found")

def check_data_prep_script(recipe_path):
    """Check the data preparation Python script"""
    print("\n" + "=" * 60)
    print("DATA_PREP.PY ANALYSIS")
    print("=" * 60)
    
    recipe_path = Path(recipe_path)
    data_prep_file = recipe_path / "asr1" / "local" / "data_prep.py"
    
    if data_prep_file.exists():
        print("✅ Found data_prep.py - This is CRITICAL for Iranian languages")
        try:
            with open(data_prep_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Look for key functions and structure
                print("🔍 Key components found:")
                
                if 'def main' in content:
                    print("   📝 main() function - entry point")
                if 'FIELDWORK' in content:
                    print("   📚 FIELDWORK dataset handling")
                if 'import' in content:
                    # Extract imports
                    lines = content.split('\n')
                    imports = [line for line in lines if 'import' in line and '#' not in line][:5]
                    print("   📦 Key imports:")
                    for imp in imports:
                        print(f"      {imp.strip()}")
                        
                # Show function definitions
                lines = content.split('\n')
                functions = []
                for i, line in enumerate(lines):
                    if line.strip().startswith('def '):
                        func_name = line.strip().split('def ')[1].split('(')[0]
                        functions.append(func_name)
                
                if functions:
                    print(f"   🔧 Functions: {', '.join(functions)}")
                    
        except Exception as e:
            print(f"❌ Error reading data_prep.py: {e}")
    else:
        print("❌ data_prep.py not found")

def generate_iranian_implementation_plan():
    """Generate detailed plan for Iranian language implementation"""
    print("\n" + "=" * 60)
    print("IRANIAN LANGUAGE IMPLEMENTATION PLAN")
    print("=" * 60)
    
    print("🎯 COMPREHENSIVE IMPLEMENTATION STRATEGY:")
    
    phase1 = [
        "PHASE 1: ENVIRONMENT SETUP",
        "   1. 🐍 Create Python environment: conda create -n wav2gloss python=3.8",
        "   2. 📦 Install ESPNet: pip install espnet",
        "   3. 🔧 Install additional dependencies from requirements",
        "   4. ✅ Test installation with: python -c 'import espnet; print(espnet.__version__)'"
    ]
    
    phase2 = [
        "\nPHASE 2: DATA PREPARATION ANALYSIS", 
        "   1. 📊 Study data_prep.py to understand FIELDWORK format",
        "   2. 📝 Analyze how languages are currently handled",
        "   3. 🔍 Understand the data directory structure",
        "   4. 💾 Prepare sample Balochi/Kurdish data in FIELDWORK format"
    ]
    
    phase3 = [
        "\nPHASE 3: CONFIGURATION ADAPTATION",
        "   1. ⚙️ Create new config files for Iranian languages",
        "   2. 🔠 Handle Balochi/Kurdish text tokenization",
        "   3. 🗣️  Adapt for right-to-left script if needed",
        "   4. 📋 Modify run.sh for new language codes"
    ]
    
    phase4 = [
        "\nPHASE 4: TESTING & ITERATION",
        "   1. 🧪 Run small-scale training with sample data",
        "   2. 📈 Evaluate performance metrics",
        "   3. 🔄 Iterate on data preparation and configuration",
        "   4. 🚀 Scale up to full dataset"
    ]
    
    for phase in [phase1, phase2, phase3, phase4]:
        for step in phase:
            print(f"   {step}")

def generate_environment_setup_script():
    """Generate environment setup script"""
    print("\n" + "=" * 60)
    print("ENVIRONMENT SETUP SCRIPT")
    print("=" * 60)
    
    setup_script = """
# Save this as setup_environment.ps1 and run in PowerShell

# Create and activate conda environment
conda create -n wav2gloss python=3.8 -y
conda activate wav2gloss

# Install ESPNet and core dependencies
pip install espnet

# Install additional packages that might be needed
pip install soundfile
pip install librosa
pip install jiwer
pip install sentencepiece

# Install PyTorch (adjust based on your CUDA version)
# For CPU-only:
pip install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cpu
# For CUDA 11.8:
# pip install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cu118

# Test installation
python -c "import espnet; print('ESPNet version:', espnet.__version__)"
python -c "import torch; print('PyTorch version:', torch.__version__)"

echo "✅ Environment setup complete!"
"""
    
    print("📜 Save the following as 'setup_environment.ps1':")
    print(setup_script)

def main():
    """Main analysis function"""
    wav2gloss_path = r"C:\CRF\espnet-wav2gloss\espnet-wav2gloss\egs2\wav2gloss"
    
    print("🚀 COMPLETE WAV2GLOSS ANALYSIS PIPELINE")
    print("💡 Steps 3-4: Implementation Analysis & Environment Setup\n")
    
    success = analyze_wav2gloss_structure(wav2gloss_path)
    
    if success:
        analyze_data_preparation(wav2gloss_path)
        analyze_configurations(wav2gloss_path)
        analyze_training_script(wav2gloss_path)
        check_data_prep_script(wav2gloss_path)
        generate_iranian_implementation_plan()
        generate_environment_setup_script()
        
        print("\n" + "=" * 60)
        print("🎯 NEXT STEPS SUMMARY")
        print("=" * 60)
        print("1. ✅ Run the environment setup script")
        print("2. 📚 Study data_prep.py in detail") 
        print("3. 💾 Prepare sample Iranian language data")
        print("4. 🚀 Begin adaptation for Balochi/Kurdish")
        print("\n✅ Analysis Complete! Ready for implementation.")
    else:
        print("\n❌ Could not analyze WAV2GLOSS recipe")

if __name__ == "__main__":
    main()