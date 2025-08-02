from medical_records.specialty import Specialty

class Doctor:
    def __init__(self, id: int, first_name: str, last_name: str, speciality: str):
        self.doctor_id = self.validate_doctor_id(id)
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.speciality = Specialty

    @staticmethod
    def validate_doctor_id(doctor_id: int):
        if not doctor_id.isdigit():
            raise ValueError("Invalid doctor_id")
        return doctor_id

    @staticmethod
    def validate_first_name(first_name):
        if first_name.strip() == "" and not first_name.isalpha():
            raise ValueError("Invalid first name")
        return first_name

    @staticmethod
    def validate_last_name(last_name):
        if not last_name.isalpha():
            raise ValueError("Name must be letters")
        return last_name

    @staticmethod
    def validate_speciality(speciality):
        for speciality in Speciality:

    def __str__(self):
        return f'Doctor\'s ID: {doctor_id} \nDoctor\'s name: {first_name.title()} {last_name.title()}\nSpeciality: {speciality.title()}'