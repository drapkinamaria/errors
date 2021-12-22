import os
import shutil
import unicodedata
import zipfile
import subprocess
from pathspec.compat import unicode

path = input()
for char in path:
    new_char = unicodedata.normalize("NFKD", char)
    make_path = "".join(new_char)
folder_list = [".vscode", "__pycache__"]
new_new_path = make_path + "\\"
for list in range(0, len(folder_list)):
    new_path = new_new_path + folder_list[list]
    if os.path.exists(new_path):
        shutil.rmtree(new_path)
    new_path = ""

subprocess.run(
    ["black", r"C:\Users\Пользователь\PycharmProjects\pythonProject"],
    stdout=True,
    check=True,
)

so_new_path = make_path + "\\errors.zip"
if os.path.exists("errors.zip") == "False":
    fantasy_zip = zipfile.ZipFile(so_new_path, "w")
    for folder, subfolders, files in os.walk(path):
        if folder != ".idea" or folder != "venv":
            for file in files:
                if file.endswith(".txt") or file.endswith(".py"):
                    fantasy_zip.write(
                        os.path.join(folder, file),
                        os.path.relpath(os.path.join(folder, file), path),
                        compress_type=zipfile.ZIP_DEFLATED,
                    )
    fantasy_zip.close()
