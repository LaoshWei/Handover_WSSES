import os
import json

folder = './photos'
files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

with open(os.path.join(folder, 'photos.json'), 'w', encoding='utf-8') as f:
    json.dump(files, f, ensure_ascii=False, indent=2)