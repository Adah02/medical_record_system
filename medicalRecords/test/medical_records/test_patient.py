from unittest import TestCase
from medical_records.patient import Patient

class TestPatient(TestCase):
    patient = Patient('adah02', '1234', 1, 'Emma',
                      'Adah', 'male', '17,04,1998', '08160509785')

    def test_that_medical_history_is_empty(self):
        self.assertEqual(0, self.patient.get_medical_history())

    def test_that_medical_history_is_not_empty(self):
        self.patient.create_medical_history(12, 'head-ache', 'Sneezing', 'ampecillin', 'chloramphenical')
        self.assertEqual(1, self.patient.get_medical_history())

    def test_that_first_name_is_valid(self):
        self.patient.validate_first_name("Emma")
        self.assertEqual('Emma', self.patient.validate_first_name("Emma"))

    def test_that_first_name_is_not_valid(self):
        self.assertRaises(ValueError, self.patient.validate_first_name, "Adah02")

    def test_that_last_name_is_valid(self):
        self.patient.validate_last_name("Adah")
        self.assertEqual('Adah', self.patient.validate_last_name("Adah"))

    def test_that_last_name_is_not_valid(self):
        self.assertRaises(ValueError, self.patient.validate_last_name, "Emma02")

    def test_that_gender_is_valid(self):
        self.patient.validate_gender("male")
        self.assertEqual('Male', self.patient.validate_gender("male"))

    def test_that_gender_is_not_valid(self):
        self.assertRaises(ValueError, self.patient.validate_gender, "ma")

    def test_that_phone_number_is_valid(self):
        print(self.patient.validate_phone_number("0123456789"))
        self.assertEqual('0123456789', self.patient.validate_phone_number("0123456789"))