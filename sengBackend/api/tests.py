from api.serializers import RecordSerializer
from api import models
import unittest

## test file


class TestRecords(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    # Create your tests here.
    def setUp(self):
        self.record_attributes = {
            "illness": "flu",
            "description": "bad flu!",
        }

        self.serializer_data = {
            "illness": "flu",
            "description": "bad flu!",
        }

        self.record = models.Record.objects.create(**self.record_attributes)
        self.serializer = RecordSerializer(instance=self.record)

    def test_record_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(["id", "illness", "description"]))

    def test_record_illness_field(self):
        data = self.serializer.data

        self.assertEqual(data["illness"], self.record_attributes["illness"])

    def test_record_description_field(self):
        data = self.serializer.data

        self.assertEqual(data["description"], self.record_attributes["description"])
