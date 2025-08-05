from medical_records.specialty import Specialty

class Doctor:
    def __init__(self, user_name: str, pass_word: str,id: int, first_name: str, last_name: str, speciality: str):
        self.username = self.validate_username(user_name)
        self.password = self.validate_password(pass_word)
        self.doctor_id = self.validate_doctor_id(id)
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.speciality = self.validate_speciality(speciality)

    @staticmethod
    def validate_username(user_name):
        if user_name == '' or len(user_name) > 10:
            raise ValueError("Username cannot be empty or greater than 10 characters")
        return user_name

    @staticmethod
    def validate_password(pass_word):
        if len(pass_word) < 6 or len(pass_word) > 15:
            raise ValueError("Password must have at least 6 characters but max 15 characters")
        return pass_word

    @staticmethod
    def validate_doctor_id(doctor_id: int):
        if not isinstance(doctor_id, int):
            raise TypeError("doctor_id must be an integer")
        return doctor_id

    @staticmethod
    def validate_first_name(first_name: str):
        if first_name.strip() == "" or not first_name.isalpha():
            raise ValueError("First name must contain only letters")
        return first_name.title()

    @staticmethod
    def validate_last_name(last_name: str):
        if not last_name.isalpha():
            raise ValueError("Last name must be letters")
        return last_name.title()

    @staticmethod
    def validate_speciality(specialization: str):
        is_found = False
        for spec in Specialty:
            if spec.value.lower() == specialization.lower():
                return spec.value;  is_found = True
        if not is_found:
            raise ValueError("Invalid speciality")

    def get_doctor_id(self) -> int:
        return self.doctor_id

    def get_first_name(self) -> str:
        return self.first_name.title()

    def get_last_name(self) -> str:
        return self.last_name.title()

    def get_speciality(self) -> str:
        return self.speciality

    def __str__(self):
        return (f'Username: {self.username} \nDoctor\'s ID: {self.get_doctor_id()} \nDoctor\'s name: '
                f'{self.get_first_name()} {self.get_last_name()}\nSpeciality: {self.get_speciality()}')