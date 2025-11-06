#!/usr/bin/env python3
"""
Create Sample Iranian Language Data for WAV2GLOSS
"""
import json
import os
from pathlib import Path

def create_sample_data_structure():
    """Create sample FIELDWORK-style data structure for Iranian languages"""
    print("=" * 60)
    print("CREATING SAMPLE IRANIAN LANGUAGE DATA")
    print("=" * 60)
    
    # Base directory for sample data
    sample_data_dir = Path(r"C:\CRF\sample_iranian_data")
    sample_data_dir.mkdir(exist_ok=True)
    
    # Iranian languages to add
    iranian_languages = ["balochi", "kurdish_sorani", "kurdish_kurmanji"]
    
    print("📁 Creating sample data structure...")
    
    for lang in iranian_languages:
        lang_dir = sample_data_dir / lang
        lang_dir.mkdir(exist_ok=True)
        
        # Create splits (train, dev, test)
        for split in ["train", "dev", "test"]:
            split_dir = lang_dir / split
            split_dir.mkdir(exist_ok=True)
            
            # Create JSON metadata file
            create_sample_json(split_dir, lang, split)
            
            print(f"✅ Created: {lang}/{split}/")
    
    print(f"\n🎉 Sample data structure created at: {sample_data_dir}")

def create_sample_json(split_dir, lang, split):
    """Create sample JSON metadata file"""
    
    sample_data = {
        "balochi": [
            {
                "utterance_id": f"{lang}_{split}_001",
                "audio_path": f"audio/{lang}_{split}_001.wav",
                "transcription": "من شهْرِ ستّار ءَ",
                "underlying_form": "man šahre stār a",
                "gloss": "1SG city Star COP",
                "translation": "I am from Star City",
                "translation_language": "en"
            }
        ],
        "kurdish_sorani": [
            {
                "utterance_id": f"{lang}_{split}_001",
                "audio_path": f"audio/{lang}_{split}_001.wav", 
                "transcription": "من له شاری هەولێرم",
                "underlying_form": "min le sharî hewlêrim",
                "gloss": "1SG from city Hawler COP",
                "translation": "I am from Hawler city",
                "translation_language": "en"
            }
        ],
        "kurdish_kurmanji": [
            {
                "utterance_id": f"{lang}_{split}_001",
                "audio_path": f"audio/{lang}_{split}_001.wav",
                "transcription": "Ez ji Amedê me",
                "underlying_form": "ez ji Amedê me", 
                "gloss": "1SG from Diyarbakir COP",
                "translation": "I am from Diyarbakir",
                "translation_language": "en"
            }
        ]
    }
    
    json_file = split_dir / f"{split}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(sample_data[lang], f, ensure_ascii=False, indent=2)
    
    # Create placeholder audio directory
    audio_dir = split_dir / "audio"
    audio_dir.mkdir(exist_ok=True)

if __name__ == "__main__":
    create_sample_data_structure()
    print("\n📝 Sample data ready for testing!")
