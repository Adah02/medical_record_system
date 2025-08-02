from medical_records.doctor import Doctor
from unittest import TestCase

class TestDoctor(TestCase):
    doct = Doctor(1, 'Emma', 'Adah', 'Cadiologist')

    def test_that_doctor_id_is_valid(self):
        self.assertEqual(2, self.doct.validate_doctor_id(2))

    def test_that_doctor_id_is_not_valid(self):
        self.assertRaises(ValueError, self.doct.validate_doctor_id, '')