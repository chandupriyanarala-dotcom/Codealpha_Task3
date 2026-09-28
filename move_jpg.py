import os
import shutil

source_folder = r"C:\Users\chand\Desktop\source"
destination_folder = r"C:\Users\chand\Desktop\Destination"

os.makedirs(destination_folder, exist_ok=True)

print("Files found:", os.listdir(source_folder))

for file in os.listdir(source_folder):
    if file.lower().endswith((".jpg", ".jpeg")):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print("Moved:", file)

print("Done!")
