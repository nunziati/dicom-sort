import os
from pathlib import Path

from dicomselect import Database

root = Path("/data/pelvis/projects/giacomo")

dataset_path = root / "dicom_dataset" / "RUMC"

db_path = Path('./')

# Clean the old db files
if db_path.exists():
    os.remove(db_path / 'archive.log')
    os.remove(db_path / 'archive.progress')
    os.remove(db_path / 'archive.pending.db')


db = Database(db_path / "archive.db")
db.create(dataset_path, max_workers=4, max_rows=1000)