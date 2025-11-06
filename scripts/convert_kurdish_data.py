import os
import json

def convert_json_to_espnet():
    # Map your Kurdish data splits to ESPNet data directories
    kurdish_base = "/c/Kurdish_WAV2GLOSS/clean_project/03_wav2gloss_input/sorani"
    espnet_data_dirs = {
        "train": "w2g_all_full_train",
        "dev": "w2g_all_full_dev", 
        "test": "w2g_all_full_test"
    }
    
    for split, espnet_dir in espnet_data_dirs.items():
        json_path = os.path.join(kurdish_base, split, "data.json")
        espnet_dir_path = os.path.join("data", espnet_dir)
        
        # Create ESPNet directory
        os.makedirs(espnet_dir_path, exist_ok=True)
        
        if os.path.exists(json_path):
            print(f"Processing {split} -> {espnet_dir}")
            
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Create ESPNet files
            wav_scp = []
            text = []
            utt2spk = []
            
            for item in data:
                utt_id = item["utterance_id"]
                audio_path = os.path.join(kurdish_base, split, "audio", item["audio_path"])
                transcription = item["transcription"]
                
                # Add to wav.scp
                wav_scp.append(f"{utt_id} {audio_path}\n")
                
                # Add to text
                text.append(f"{utt_id} {transcription}\n")
                
                # Add to utt2spk (use first part of utt_id as speaker)
                spk_id = utt_id.split('_')[0] if '_' in utt_id else 'spk1'
                utt2spk.append(f"{utt_id} {spk_id}\n")
            
            # Write files
            with open(os.path.join(espnet_dir_path, "wav.scp"), 'w', encoding='utf-8') as f:
                f.writelines(wav_scp)
            
            with open(os.path.join(espnet_dir_path, "text"), 'w', encoding='utf-8') as f:
                f.writelines(text)
            
            with open(os.path.join(espnet_dir_path, "utt2spk"), 'w', encoding='utf-8') as f:
                f.writelines(utt2spk)
            
            # Create spk2utt from utt2spk
            spk_utt_map = {}
            for line in utt2spk:
                utt_id, spk_id = line.strip().split()
                if spk_id not in spk_utt_map:
                    spk_utt_map[spk_id] = []
                spk_utt_map[spk_id].append(utt_id)
            
            with open(os.path.join(espnet_dir_path, "spk2utt"), 'w', encoding='utf-8') as f:
                for spk_id, utt_ids in spk_utt_map.items():
                    f.write(f"{spk_id} {' '.join(utt_ids)}\n")
            
            print(f"Created {len(wav_scp)} entries for {espnet_dir}")
        else:
            print(f"JSON file not found: {json_path}")

if __name__ == "__main__":
    convert_json_to_espnet()
    print("Kurdish data conversion completed!")
