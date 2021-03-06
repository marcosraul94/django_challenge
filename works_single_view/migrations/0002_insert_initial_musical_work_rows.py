# Generated by Django 4.0.3 on 2022-04-07 18:03

from django.db import migrations
from ..models import MusicalWork as MusicalWorkClass
from ..utils import load_musical_works, find_existing_musical_work

APP_NAME = 'works_single_view'
MODEL_NAME = 'MusicalWork'


def forwards_func(apps, schema_editor):
    """Insert records from works_metadata.csv"""
    MusicalWork: MusicalWorkClass = apps.get_model(APP_NAME, MODEL_NAME)
    musical_works_to_insert = load_musical_works()

    for musical_work_to_insert in musical_works_to_insert:
        existing_musical_work = find_existing_musical_work(musical_work_to_insert, MusicalWork)
        if existing_musical_work:
            existing_musical_work.merge(musical_work_to_insert)
            existing_musical_work.save()
        else:
            new_musical_work = MusicalWork(**musical_work_to_insert)
            new_musical_work.save()


def backwards_func(apps, schema_editor):
    """Rollback inserted musical works records."""
    MusicalWork: MusicalWorkClass = apps.get_model(APP_NAME, MODEL_NAME)
    MusicalWork.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('works_single_view', '0001_create_musical_work_model'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func)
    ]
