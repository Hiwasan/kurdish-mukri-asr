#!/usr/bin/env python3
"""
WAV2GLOSS Recipe Analysis Pipeline
Step 3: Analyze the WAV2GLOSS specific implementation
"""
import os
import yaml
from pathlib import Path

def analyze_wav2gloss_recipe(recipe_path):
    """Analyze the WAV2GLOSS recipe structure"""
    print("=" * 60)
    print("WAV2GLOSS RECIPE ANALYSIS")
    print("=" * 60)
    
    recipe_path = Path(recipe_path)
    
    if not recipe_path.exists():
        print(f"❌ WAV2GLOSS recipe not found at: {recipe_path}")
        return False
    
    print(f"📁 Recipe location: {recipe_path}")
    print(f"🔍 Analyzing WAV2GLOSS implementation...\n")
    
    # 1. List main recipe contents
    print("📋 RECIPE DIRECTORY STRUCTURE:")
    print("-" * 40)
    
    items = list(recipe_path.iterdir())
    for item in sorted(items, key=lambda x: (x.is_file(), x.name)):
        if item.is_dir():
            print(f"📁 {item.name}/")
            # Show contents of important subdirectories
            if item.name in ["asr1", "gloss1", "translation1", "local", "scripts"]:
                try:
                    sub_items = list(item.iterdir())[:5]
                    for sub_item in sub_items:
                        item_type = "📁" if sub_item.is_dir() else "📄"
                        print(f"   └── {item_type} {sub_item.name}")
                except Exception as e:
                    print(f"   └── (Error reading: {e})")
        else:
            print(f"📄 {item.name}")
    
    # 2. Look for configuration files
    print("\n🔧 CONFIGURATION FILES:")
    print("-" * 40)
    
    config_files = list(recipe_path.rglob("*.yaml")) + list(recipe_path.rglob("*.yml"))
    for config_file in config_files[:10]:  # Show first 10 configs
        print(f"   - {config_file.relative_to(recipe_path)}")
    
    # 3. Look for data preparation scripts
    print("\n📊 DATA PREPARATION SCRIPTS:")
    print("-" * 40)
    
    data_scripts = list(recipe_path.rglob("*data*.sh")) + list(recipe_path.rglob("*prep*.sh"))
    for script in data_scripts:
        print(f"   - {script.relative_to(recipe_path)}")
    
    # 4. Look for training scripts
    print("\n🚀 TRAINING SCRIPTS:")
    print("-" * 40)
    
    train_scripts = list(recipe_path.rglob("*train*.sh")) + list(recipe_path.rglob("*run*.sh"))
    for script in train_scripts:
        print(f"   - {script.relative_to(recipe_path)}")
    
    # 5. Check for language configurations
    print("\n🔤 LANGUAGE CONFIGURATIONS:")
    print("-" * 40)
    
    # Look in config files for language settings
    for config_file in config_files[:5]:
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'lang' in content.lower() or 'language' in content.lower():
                    print(f"   📄 {config_file.relative_to(recipe_path)}")
                    # Extract language related lines
                    lines = content.split('\n')
                    for line in lines:
                        if 'lang' in line.lower() and len(line.strip()) < 100:
                            print(f"      └── {line.strip()}")
        except Exception as e:
            pass
    
    return True

def analyze_implementation_details(recipe_path):
    """Analyze the implementation details for Iranian languages"""
    print("\n" + "=" * 60)
    print("IRANIAN LANGUAGE IMPLEMENTATION ANALYSIS")
    print("=" * 60)
    
    # Look for how new languages are added
    print("🔍 Searching for language addition patterns...")
    
    # Check local data preparation scripts
    local_dir = recipe_path / "local"
    if local_dir.exists():
        print(f"\n📝 Local data scripts:")
        local_scripts = list(local_dir.rglob("*.sh")) + list(local_dir.rglob("*.py"))
        for script in local_scripts:
            print(f"   - {script.relative_to(recipe_path)}")
    
    # Check for multi-language configurations
    print(f"\n🌍 Multi-language support analysis:")
    
    # Look in the main recipe directories
    task_dirs = ["asr1", "gloss1", "translation1"]
    for task_dir in task_dirs:
        task_path = recipe_path / task_dir
        if task_path.exists():
            print(f"\n✅ Found task directory: {task_dir}")
            # Look for config files in this task
            configs = list(task_path.rglob("*.yaml"))
            if configs:
                print(f"   Configurations:")
                for config in configs[:3]:
                    print(f"   - {config.relative_to(recipe_path)}")
    
    # Check for FIELDWORK dataset handling
    print(f"\n📚 FIELDWORK dataset integration:")
    fieldwork_refs = list(recipe_path.rglob("*fieldwork*"))
    if fieldwork_refs:
        for ref in fieldwork_refs:
            print(f"   - {ref.relative_to(recipe_path)}")
    else:
        print("   ❌ No FIELDWORK specific references found")

def generate_iranian_language_plan(recipe_path):
    """Generate a plan for adding Iranian language support"""
    print("\n" + "=" * 60)
    print("IRANIAN LANGUAGE IMPLEMENTATION PLAN")
    print("=" * 60)
    
    print("🎯 Based on the WAV2GLOSS structure, here's how to add Iranian languages:")
    
    steps = [
        "1. 📁 Identify data preparation scripts in 'local/' directory",
        "2. 📝 Create Balochi/Kurdish data preparation scripts",
        "3. ⚙️ Study existing configuration files for language settings", 
        "4. 🔧 Create new config files for Iranian languages",
        "5. 💾 Prepare FIELDWORK-style data for Balochi/Kurdish",
        "6. 🧪 Test data preparation pipeline",
        "7. 🚀 Run training with small dataset first",
        "8. 📊 Evaluate and iterate on model performance"
    ]
    
    for step in steps:
        print(f"   {step}")
    
    print(f"\n📋 Key directories to focus on:")
    key_dirs = ["local", "asr1", "gloss1", "scripts"]
    for dir_name in key_dirs:
        dir_path = recipe_path / dir_name
        if dir_path.exists():
            print(f"   ✅ {dir_name}/ - {len(list(dir_path.iterdir()))} items")
        else:
            print(f"   ❌ {dir_name}/ - Not found")

def check_dependencies(recipe_path):
    """Check for dependency requirements"""
    print("\n" + "=" * 60)
    print("DEPENDENCY CHECK")
    print("=" * 60)
    
    # Look for requirements files
    req_files = list(recipe_path.rglob("requirements*.txt")) + list(recipe_path.rglob("environment*.yml"))
    
    if req_files:
        print("✅ Found dependency files:")
        for req_file in req_files:
            print(f"   - {req_file.relative_to(recipe_path)}")
            try:
                with open(req_file, 'r') as f:
                    lines = f.readlines()
                    print(f"      Contains {len(lines)} dependency lines")
            except:
                pass
    else:
        print("❌ No specific dependency files found in recipe")
        print("   Will use main ESPNet requirements")

if __name__ == "__main__":
    wav2gloss_path = r"C:\CRF\espnet-wav2gloss\espnet-wav2gloss\egs2\wav2gloss"
    
    print("🚀 Step 3: Analyzing WAV2GLOSS Recipe...")
    print("💡 We'll now explore the specific implementation\n")
    
    success = analyze_wav2gloss_recipe(wav2gloss_path)
    
    if success:
        analyze_implementation_details(wav2gloss_path)
        check_dependencies(wav2gloss_path)
        generate_iranian_language_plan(wav2gloss_path)
        
        print("\n✅ Step 3 Complete! Ready for Step 4: Environment Setup")
        print("\n📝 NEXT ACTION: We'll set up the Python environment based on what we found")
    else:
        print("\n❌ Could not analyze WAV2GLOSS recipe")