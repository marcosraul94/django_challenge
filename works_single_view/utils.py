import os
import csv
from django.db.models import Q
from typing import Union
from .models import MusicalWork as MusicalWorkClass


APP_PATH = os.path.dirname(os.path.dirname(__file__))
WORKS_METADATA_FILE_PATH = os.path.join(APP_PATH, 'instructions', 'works_metadata.csv')


def load_musical_works(file_path: str = WORKS_METADATA_FILE_PATH) -> list[dict]:
    with open(file_path) as works_metadata_file:
        reader = csv.DictReader(works_metadata_file)
        return list(reader)


def find_existing_musical_work(musical_work: dict, MusicalWork: MusicalWorkClass) -> Union[MusicalWorkClass, None]:
    """Find in the db another version of the musical work."""
    title = musical_work.get('title')
    iswc = musical_work.get('iswc')

    query = Q(title=title)
    if iswc:
        query.add(Q(iswc=iswc), Q.OR)

    db_musical_works: list[MusicalWork] = MusicalWorkClass.objects.filter(query)
    for db_musical_work in db_musical_works:
        if db_musical_work.is_another_version(musical_work):
            return db_musical_work

    return None
