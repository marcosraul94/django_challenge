import os
import csv


APP_PATH = os.path.dirname(os.path.dirname(__file__))
WORKS_METADATA_FILE_PATH = os.path.join(APP_PATH, 'instructions', 'works_metadata.csv')


def load_musical_works(file_path: str = WORKS_METADATA_FILE_PATH) -> list[dict]:
    with open(file_path) as works_metadata_file:
        reader = csv.DictReader(works_metadata_file)
        return list(reader)

