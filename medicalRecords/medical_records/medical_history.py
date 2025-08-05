

class MedicalHistory:
    def __init__(self, id: int, past_illness: str, current_illness: str, allergies: str, medication: str):
        self.patient_id = self.validate_patient_id(id)
        self.past_illness = past_illness
        self.present_illness = current_illness
        self.allergies = allergies
        self.medications = medication

    @staticmethod
    def validate_patient_id(patient_id: int):
        if 0 > patient_id:
            raise ValueError('Patient ID must be greater than 0')
        return patient_id

    def add_allergies(self, allergies: str):
        self.allergies += f',{allergies}'

    def delete_allergies(self, current_allergy: str):
        if current_allergy not in self.allergies:
            raise ValueError("All allergies must have been removed")
        self.allergies.replace(allergy, "")

    def get_past_illness(self) -> str:
        return self.past_illness

    def get_present_illness(self) -> str:
        return self.present_illness

    def get_allergies(self) -> str:
        return self.allergies

    def get_medication(self) -> str:
        return self.medications

    def __str__(self) -> str:
        return (f'Past illnesses: {get_past_illness()}\nCurrent Illnesses: {get_present_illness()}'
                f'Allergies: {get_allergies()}\nMedications: {get_medication()}')