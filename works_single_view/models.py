import json
from django.db import models
from django.core import serializers


# Create your models here.
class MusicalWork(models.Model):
    iswc: str = models.CharField(max_length=11, null=True, unique=True)
    title: str = models.CharField(max_length=100)
    contributors: str = models.CharField(max_length=255)

    def __str__(self):
        return str({'pk': self.pk, 'iswc': self.iswc, 'contributors': self.contributors})

    def to_json(self) -> dict:
        serialized_instance: str = serializers.serialize('json', [self], ensure_ascii=False)
        model_dict: dict = json.loads(serialized_instance)[0]
        return {'pk': model_dict['pk'], **model_dict['fields']}

    def merge_contributors(self, other_contributors: str):
        raise not NotImplementedError()
