credit = """
This project is licensed under MIT licensed
To view the github repo, please visit https://github.com/Andrewgxgx/bulk_converter#
This script is created by Andrew gx
You can support me by starring this repo!
"""
print(credit)
import os
import shutil
import subprocess

files_dir = "./input"
output_dir = "./output"

# Supported inputs
convert_formats = (".pdf", ".lit", ".mobi", ".fb2", "html", ".rtf", ".txt", ".doc", ".docx", ".odt")

# This makes sure if the directories exist or not
os.makedirs(output_dir, exist_ok=True)
os.makedirs(files_dir, exist_ok=True)

def process_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            print(credit)
            input_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, directory)
            output_folder = os.path.join(output_dir, relative_path)
            os.makedirs(output_folder, exist_ok=True)
            output_path = os.path.join(output_folder, file)

            # if the file is already in .epub it will just move it to the pdf folder
            if file.lower().endswith(".epub"):
                shutil.move(input_path, output_path)
                print(f"Moved EPUB to: {file}")

            # If its in other format, it will be converted to epub
            elif file.lower().endswith(convert_formats):
                output_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".epub")

                try:
                    subprocess.run(["ebook-convert", input_path, output_file], check=True)
                    print(f"Converted: {file} -> {output_file}")

                    # Remove these two lines if you dont want ur files to be deleted after conversion
                    os.remove(input_path)
                    print(f"Deleted: {input_path}")

                except subprocess.CalledProcessError as e:
                    print(f"Failed to convert {file}: {e}")

if not os.listdir(files_dir):
    print("No files to process.")
    exit(0)

process_files(files_dir)
print("All files processed.")
