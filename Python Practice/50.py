import os
import shutil

os.makedirs("data/archive",exist_ok=True)
os.rename("data/archive","data/old_archive")
shutil.copytree("data/old_archive","data/backup_archive")
shutil.rmtree("data/backup_archive")
