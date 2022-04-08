from django.test import TestCase
from .models import MusicalWork


# Create your tests here.
class MusicalWorkTestCase(TestCase):
    def setUp(self):
        MusicalWork.objects.create(iswc='a', title='b', contributors='c|d')

    def test_inserts(self):
        test_musical_work: MusicalWork = MusicalWork.objects.get(iswc='a')

        self.assertEqual(test_musical_work.iswc, 'a')
        self.assertEqual(test_musical_work.title, 'b')
        self.assertEqual(test_musical_work.contributors, 'c|d')

    def test_to_json(self):
        test_musical_work: MusicalWork = MusicalWork.objects.get(iswc='a')
        generated_dict = test_musical_work.to_json()
        expected_dict = {
            'pk': test_musical_work.pk,
            'iswc': 'a',
            'title': 'b',
            'contributors': 'c|d'
        }

        self.assertEqual(generated_dict, expected_dict)

    def test_is_another_version_with_iscw(self):
        test_musical_work: MusicalWork = MusicalWork.objects.get(iswc='a')
        another_version = {'iscw': 'a'}
        is_another_version = test_musical_work.is_another_version(another_version)

        self.assertTrue(is_another_version)

    def test_is_another_version_without_iscw(self):
        test_musical_work: MusicalWork = MusicalWork.objects.get(iswc='a')
        another_version = {'title': 'b', 'contributors': 'd|e'}
        is_another_version = test_musical_work.is_another_version(another_version)

        self.assertTrue(is_another_version)

    def test_not_is_another_version_with_iscw(self):
        test_musical_work: MusicalWork = MusicalWork.objects.get(iswc='a')
        different_musical_work = {'iscw': 'e', 'title': 'b', 'contributors': 'd|e'}
        is_another_version = test_musical_work.is_another_version(different_musical_work)

        self.assertFalse(is_another_version)

    def test_not_is_another_version_without_iscw(self):
        test_musical_work: MusicalWork = MusicalWork.objects.get(iswc='a')
        different_musical_work = {'title': 'b', 'contributors': 'f'}
        is_another_version = test_musical_work.is_another_version(different_musical_work)

        self.assertFalse(is_another_version)

    def test_merge_with_iscw(self):
        test_musical_work: MusicalWork = MusicalWork.objects.get(iswc='a')
        another_version = {'contributors': 'f'}
        test_musical_work.merge(another_version)

        self.assertEqual(test_musical_work.contributors, 'c|d|f')
        self.assertEqual(test_musical_work.iswc, 'a')
        self.assertEqual(test_musical_work.title, 'b')

    def test_merge_without_iscw(self):
        test_musical_work: MusicalWork = MusicalWork.objects.get(iswc='a')
        test_musical_work.iswc = None

        another_version = {'iswc': 'h', 'contributors': 'f'}
        test_musical_work.merge(another_version)

        self.assertEqual(test_musical_work.iswc, 'h')

    def test_merge_with_duplicates(self):
        test_musical_work: MusicalWork = MusicalWork.objects.get(iswc='a')

        another_version = {'contributors': 'f|c|d'}
        test_musical_work.merge(another_version)

        self.assertEqual(test_musical_work.contributors, 'c|d|f')
