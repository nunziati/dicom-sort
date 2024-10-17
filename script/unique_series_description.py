import os
from pathlib import Path

from dicomselect import Database

root = Path("/data/pelvis/projects/giacomo/dicom_datasets")

dataset_path = root / "dicom_dataset" / "RUMC"

db_path = Path('./')

db = Database(db_path / "archive.db")
db.create(dataset_path, max_workers=4, max_rows=1000)