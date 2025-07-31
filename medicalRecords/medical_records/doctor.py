class Doctor:
    def __init__(self, id: int, first_name: str, last_name: str, speciality: str):
        self.doctor_id = id
        self.first_name = first_name
        self.last_name = last_name
        self.speciality = speciality

        def validate_name(first_name, last_name):
            if first_name.isalpha() and last_name.isalpha():
                return first_name.isalpha() and last_name.isalpha()
            else:
                raise ValueError("Name must be letters")

        def __str__(self):
            return f'Doctor\'s ID: {doctor_id} \nDoctor\'s name: {first_name.title()} {last_name.title()}\nSpeciality: {speciality.title()}'