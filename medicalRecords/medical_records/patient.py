from medical_records.gender import Gender
from datetime import datetime

class Patient:
    def __init__(self, id: int, first_name: str, last_name: str, gender: str, dob: str, phone_number: str):
        self.patient_id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = dob
        self.phone_number = phone_number

    @property
    def patient_id_validation(self):
        return self.patient_id

    @patient_id_validation.setter
    def patient_id_validation(self, id_number):
        if id_number.isdigit():
            if id_number <= 0:
                raise ValueError("Patient ID number must be greater than zero.")
            self.patient_id = id_number


    def validate_full_name(self, first_name: str, last_name: str) -> None:
        if first_name.isalpha and last_name.isalpha():
            self.first_name = first_name.title()
            self.last_name = last_name.title()
        else:
            raise ValueError("name must contain only alphabets")

    def validate_gender(self, gender):
        if gender.lower() in [x.value.lower() for x in Gender]:
            self.gender = gender
        else:
            return "gender must be MALE or FEMALE"


    def validate_date_of_birth(self, dob: str):
        date = datetime.now()
        day, month, year = dob.split(",")
        birth_date = ''
        if year <= date.year and month <= date.month:
            birth_date = f'{day},{month},{year}'
        try:
            datetime.strptime(birth_date, '%d,%m,%Y')
            self.date_of_birth = birth_date
        except ValueError:
            raise ValueError("Date of birth must be in format DD/MM/YYYY")

    def validate_phone_number(self, phone: str):
        if not phone.isdigit() and 10 < len(phone) > 11:
            raise ValueError("Phone number must be between 10 and 11")
        self.phone_number = phone

    @staticmethod
    def validate_patient_data(first_name, last_name, gender, dob, phone_number):
        validate_full_name(full_name, last_name)
        validate_date_of_birth(dob)
        patients_gender(gender)
        validate_phone_number(phone)

    def __str__(self):
        return f'{self.patient_id}\n{self.first_name.title()} {self.last_name.title()}\n{self.date_of_birth}\n{self.phone_number}'