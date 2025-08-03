from medical_records.specialty import Specialty

class Doctor:
    def __init__(self, id: int, first_name: str, last_name: str, speciality: str):
        self.doctor_id = self.validate_doctor_id(id)
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.speciality = self.validate_speciality(speciality)

    @staticmethod
    def validate_doctor_id(doctor_id: int):
        if not isinstance(doctor_id, int):
            raise TypeError("doctor_id must be an integer")
        return doctor_id

    @staticmethod
    def validate_first_name(first_name):
        if first_name.strip() == "" or not first_name.isalpha():
            raise ValueError("First name must contain only letters")
        return first_name.title()

    @staticmethod
    def validate_last_name(last_name):
        if not last_name.isalpha():
            raise ValueError("Last name must be letters")
        return last_name.title()

    @staticmethod
    def validate_speciality(specialization):
        is_found = False
        for spec in Specialty:
            if spec.value.lower() == specialization.lower():
                return spec.value;  is_found = True
        if not is_found:
            raise ValueError("Invalid speciality")

    def __str__(self):
        return f'Doctor\'s ID: {doctor_id} \nDoctor\'s name: {first_name.title()} {last_name.title()}\nSpeciality: {speciality}'