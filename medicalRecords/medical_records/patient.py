import re
import sys
from medical_records.gender import Gender
from medical_records.medical_history import MedicalHistory
from datetime import datetime

class Patient:
    def __init__(self, user_name: str, pass_word: str, id: int, firstname: str, lastname: str, sex: str, dob: str, phone: str):
        self.username = user_name
        self.password = pass_word
        self.patient_id = self.patient_id_validation(id)
        self.first_name = self.validate_first_name(firstname)
        self.last_name = self.validate_last_name(lastname)
        self.gender = self.validate_gender(sex)
        self.date_of_birth = dob
        self.phone_number = self.validate_phone_number(phone)
        self.__medical_history = list()

    def create_medical_history(self, record_id: int, past_illness: str, present_illness: str, allergies: str, medications: str) -> None:
        self.__medical_history.append(MedicalHistory(record_id, past_illness, present_illness, allergies, medications))

    def update_medical_history(self,record_id: int, past_illness: str, present_illness: str, allergies: str, medications: str ) -> None:
        for record in self.patient.__medical_history:
            if record.record_id == record_id:
                record.patient.__medical_history = MedicalHistory(record_id, past_illness, present_illness, allergies, medications)

    @staticmethod
    def patient_id_validation(id_number):
        if  0 > id_number > sys.maxsize:
            raise ValueError("Patient ID number must be greater than zero.")
        return id_number

    @staticmethod
    def validate_first_name(firstname: str) -> str:
        if not firstname.isalpha():
            raise ValueError("Firstname must be alphabets.")
        return firstname.title()

    @staticmethod
    def validate_last_name(last_name: str) -> str:
        if not last_name.isalpha():
            raise ValueError("Lastname must contain only alphabets")
        return last_name.title()

    @staticmethod
    def validate_gender(gender):
        if not gender.lower() in [x.value.lower() for x in Gender]:
            raise ValueError("Gender must Male or Female.")
        return gender.title()

    @staticmethod
    def validate_phone_number(phone: str) -> str:
        number_format = re.findall(r'(0)([7-9])(0)([0-9]+)', phone)
        if not phone.isdigit() or 10 < len(phone) > 11:
            raise ValueError("Phone number must be between 10 and 11")
        return phone

    def get_medical_history(self):
        return len(self.__medical_history)

    def __str__(self):
        return f'{self.patient_id}\n{self.first_name.title()} {self.last_name.title()}\n{self.date_of_birth}\n{self.phone_number}'