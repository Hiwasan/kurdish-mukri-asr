#!/usr/bin/env python3
"""
ESPNet WAV2GLOSS Detailed Analysis Pipeline
Step 2: Explore Nested Structure and Find Real Project
"""
import os
import glob
import json
from pathlib import Path

def find_real_espnet_structure(base_path):
    """Find the actual ESPNet project structure"""
    print("=" * 60)
    print("FINDING REAL ESPNET STRUCTURE")
    print("=" * 60)
    
    base_path = Path(base_path)
    espnet_path = base_path / "espnet-wav2gloss"
    
    print("🔍 Exploring nested structure...")
    
    # Check what's inside espnet-wav2gloss
    nested_items = list(espnet_path.iterdir())
    print(f"\n📁 Contents of 'espnet-wav2gloss':")
    print("-" * 40)
    
    for item in nested_items:
        if item.is_dir():
            print(f"📁 {item.name}/")
            # Show first few items in subdirectories
            try:
                sub_items = list(item.iterdir())[:3]
                for sub_item in sub_items:
                    item_type = "📁" if sub_item.is_dir() else "📄"
                    print(f"   └── {item_type} {sub_item.name}")
            except Exception as e:
                print(f"   └── (Error reading: {e})")
        else:
            print(f"📄 {item.name}")
    
    # Look for the actual ESPNet structure
    possible_paths = [
        espnet_path / "espnet-wav2gloss",
        espnet_path / "espnet",
        espnet_path / "EGS",
        espnet_path / "egs2",
    ]
    
    actual_path = None
    for path in possible_paths:
        if path.exists():
            actual_path = path
            print(f"\n✅ Found actual project at: {path}")
            break
    
    if actual_path:
        return analyze_actual_espnet(actual_path)
    else:
        print("\n❌ Could not find standard ESPNet structure")
        print("Let's explore all subdirectories to find the real project...")
        return explore_all_subdirectories(espnet_path)

def explore_all_subdirectories(project_path):
    """Explore all subdirectories to find the real project structure"""
    print("\n" + "=" * 60)
    print("DEEP EXPLORATION OF ALL SUBDIRECTORIES")
    print("=" * 60)
    
    # Look for common ESPNet directories
    target_dirs = ["egs2", "egs", "espnet", "src", "scripts", "tools"]
    
    found_dirs = {}
    for target in target_dirs:
        matches = list(project_path.rglob(target))
        if matches:
            found_dirs[target] = matches
            print(f"✅ Found '{target}':")
            for match in matches[:2]:  # Show first 2 matches
                print(f"   - {match.relative_to(project_path)}")
    
    # Also look for any README files to understand the structure
    readme_files = list(project_path.rglob("README*"))
    print(f"\n📚 README files found: {len(readme_files)}")
    for readme in readme_files[:3]:  # Show first 3 READMEs
        print(f"   - {readme.relative_to(project_path)}")
    
    return found_dirs

def analyze_actual_espnet(project_path):
    """Analyze the actual ESPNet project structure"""
    print("\n" + "=" * 60)
    print("ANALYZING ACTUAL ESPNET STRUCTURE")
    print("=" * 60)
    
    print(f"📁 Project location: {project_path}")
    
    # List main contents
    print("\n📋 MAIN DIRECTORY CONTENTS:")
    print("-" * 40)
    
    items = list(project_path.iterdir())
    for item in sorted(items, key=lambda x: (x.is_file(), x.name)):
        if item.is_dir():
            print(f"📁 {item.name}/")
        else:
            print(f"📄 {item.name}")
    
    # Look for WAV2GLOSS specific content
    print("\n🔍 SEARCHING FOR WAV2GLOSS CONTENT:")
    print("-" * 40)
    
    # Search for wav2gloss related files
    wav2gloss_patterns = ["*wav2gloss*", "*fieldwork*", "*gloss*"]
    for pattern in wav2gloss_patterns:
        matches = list(project_path.rglob(pattern))
        if matches:
            print(f"✅ Found '{pattern}':")
            for match in matches[:5]:  # Show first 5 matches
                print(f"   - {match.relative_to(project_path)}")
    
    # Check for recipe directories (common in ESPNet)
    recipe_dirs = list(project_path.rglob("egs2/*")) + list(project_path.rglob("egs/*"))
    if recipe_dirs:
        print(f"\n🍳 Recipe directories found: {len(recipe_dirs)}")
        for recipe in recipe_dirs[:5]:  # Show first 5 recipes
            if recipe.is_dir():
                print(f"   - {recipe.relative_to(project_path)}")
    
    return True

def check_readme_for_instructions(project_path):
    """Check README files for setup instructions"""
    print("\n" + "=" * 60)
    print("READING README FOR INSTRUCTIONS")
    print("=" * 60)
    
    readme_files = list(project_path.rglob("README*"))
    
    if not readme_files:
        print("❌ No README files found")
        return
    
    # Read the main README
    main_readme = None
    for readme in readme_files:
        if "espnet-wav2gloss" in str(readme) or readme.parent == project_path:
            main_readme = readme
            break
    
    if main_readme and main_readme.exists():
        print(f"📖 Reading: {main_readme.relative_to(project_path)}")
        try:
            with open(main_readme, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract key sections
                lines = content.split('\n')
                print("\n🔍 Key sections found:")
                print("-" * 40)
                
                key_sections = ["install", "setup", "requirement", "usage", "train", "data"]
                for i, line in enumerate(lines):
                    line_lower = line.lower()
                    if any(section in line_lower for section in key_sections) and len(line.strip()) > 0:
                        # Check if it's a header (starts with # or has --- underneath)
                        if line.startswith('#') or (i < len(lines)-1 and '---' in lines[i+1]):
                            print(f"\n📌 {line.strip()}")
                        elif len(line.strip()) < 100:  # Not too long
                            print(f"   {line.strip()}")
        except Exception as e:
            print(f"❌ Error reading README: {e}")

if __name__ == "__main__":
    base_path = r"C:\CRF"
    
    print("🚀 Step 2: Finding Real ESPNet Structure...")
    print("💡 We need to locate the actual project files\n")
    
    # Find the real structure
    result = find_real_espnet_structure(base_path)
    
    # Check README for instructions
    espnet_main_path = Path(r"C:\CRF\espnet-wav2gloss")
    check_readme_for_instructions(espnet_main_path)
    
    print("\n🎯 NEXT STEPS:")
    print("-" * 40)
    print("1. ✅ Identify the real project structure")
    print("2. 📚 Understand installation from README") 
    print("3. 🐍 Check Python environment requirements")
    print("4. 🔍 Locate WAV2GLOSS specific recipes/training scripts")
    print("5. 💾 Find data preparation pipelines")
    
    print("\n📝 Based on what we found, we'll need to:")
    print("   - Navigate to the correct subdirectory")
    print("   - Find the egs2/ or egs/ folder with recipes")
    print("   - Locate the wav2gloss specific implementation")