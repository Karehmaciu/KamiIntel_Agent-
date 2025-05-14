import os
from train_handler import train_on_any_file

folder = "chat_data/uploads"
if not os.path.exists(folder):
    print("⚠️ Folder not found.")
    exit()

for fname in os.listdir(folder):
    path = os.path.join(folder, fname)
    if os.path.isfile(path):
        print(f"📂 Training on {fname}...")
        try:
            train_on_any_file(path)
            print("✅ Success")
        except Exception as e:
            print(f"❌ Failed: {e}")
