import os
import csv

# Paths relative to the /scripts folder
highlights_path = os.path.join('..', 'highlights')
data_folder = os.path.join('..', 'data')
manifest_path = os.path.join(data_folder, 'manifest.csv')

def sync():
    if not os.path.exists(highlights_path):
        print(f"Error: Could not find {highlights_path}")
        return

    # 1. Read existing captions so we don't lose them
    existing_data = {}
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) >= 2:
                    existing_data[row[0]] = row[1]

    # 2. Scan the highlights folder
    valid_extensions = ('.png', '.jpg', '.jpeg', '.webp')
    files = [f for f in os.listdir(highlights_path) if f.lower().endswith(valid_extensions)]
    
    # 3. Write the updated manifest
    os.makedirs(data_folder, exist_ok=True)
    with open(manifest_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['filename', 'caption']) # Ensure both columns exist
        
        for file in files:
            # Use existing caption if available, otherwise format filename as caption
            if file in existing_data:
                caption = existing_data[file]
            else:
                # Remove extension and replace underscores/dashes with spaces
                caption = os.path.splitext(file)[0].replace('_', ' ').replace('-', ' ').title()
            
            writer.writerow([file, caption])
            
    print(f"✅ Success: manifest.csv updated with {len(files)} images in /data folder.")

if __name__ == "__main__":
    sync()