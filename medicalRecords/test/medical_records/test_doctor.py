from medical_records.doctor import Doctor
from unittest import TestCase

class TestDoctor(TestCase):
    doctor = Doctor(1, 'Emma', 'Adah', 'Cardiologist')

    def test_that_doctor_id_is_valid(self):
        self.assertEqual(2, self.doctor.validate_doctor_id(2))

    def test_that_doctor_id_is_not_valid(self):
        self.assertRaises(TypeError, self.doctor.validate_doctor_id, '')

    def test_that_first_name_is_valid(self):
        self.assertEqual("Emma", self.doctor.validate_first_name("emma"))

    def test_that_first_name_is_not_valid(self):
        self.assertRaises(ValueError, self.doctor.validate_first_name, '34hey')

    def test_that_last_name_is_valid(self):
        self.assertEqual("Adah", self.doctor.validate_last_name("adah"))

    def test_that_last_name_is_not_valid(self):
        self.assertRaises(ValueError, self.doctor.validate_last_name, 'adah0323')

    def test_that_speciality_is_valid(self):
        self.assertEqual("Cardiologist", self.doctor.validate_speciality("Cardiologist"))

    def test_that_speciality_is_not_valid(self):
        self.assertRaises(ValueError, self.doctor.validate_speciality, 'Doctor')