

class MedicalHistory:
    def __init__(self, id: int, past_illness: str, current_illness: str, allergies: str, medication: str):
        self.patient_id = self.validate_patient_id(id)
        self.past_illness = past_illness
        self.present_illness = current_illness
        self.allergies = []
        self.medications = []

    @staticmethod
    def validate_patient_id(patient_id: int):
        if 0 > patient_id:
            raise ValueError('Patient ID must be greater than 0')
        return patient_id

    def add_allergies(self, allergy: str):
        self.allergies.append(allergy)

    def delete_allergies(self, allergy: str):
        if allergy not in self.allergies:
            raise ValueError("Allergy not found")
        self.allergies.pop(allergy)

    def __str__(self) -> str:
        return (f'Past illnesses: {self.past_illness}\nCurrent Illnesses: {self.present_illness}'
                f'Allergies: {self.allergies}\nMedications: {self.medications}')