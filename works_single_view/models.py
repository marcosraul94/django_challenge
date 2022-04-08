import json
from django.db import models
from django.core import serializers


# Create your models here.
class MusicalWork(models.Model):
    iswc: str = models.CharField(max_length=11, null=True, unique=True)
    title: str = models.CharField(max_length=100)
    contributors: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str({'pk': self.pk, 'iswc': self.iswc, 'contributors': self.contributors})

    def to_json(self) -> dict:
        serialized_instance: str = serializers.serialize('json', [self], ensure_ascii=False)
        model_dict: dict = json.loads(serialized_instance)[0]
        return {'pk': model_dict['pk'], **model_dict['fields']}

    def is_another_version(self, a: dict) -> bool:
        """Compare it with another musical work data to figure out if it's another version of it."""
        iswc = a.get('iscw')

        if iswc and iswc == self.iswc:
            return True

        if a.get('title') != self.title:
            return False

        a_contributors = a.get('contributors').split('|')
        self_contributors = self.contributors.split('|')
        intersection = set(a_contributors).intersection(set(self_contributors))

        return len(intersection) != 0

    def merge(self, a: dict) -> None:
        """Merge another version of the musical work into it."""
        iswc = a.get('iswc')

        # update missing iswc
        if not self.iswc and iswc:
            self.iswc = iswc

        # if there are new contributors add them
        a_contributors = a.get('contributors').split('|')
        self_contributors = self.contributors.split('|')
        contributors_set = {*a_contributors, *self_contributors}
        self.contributors = '|'.join(sorted(contributors_set))

        self.save()
