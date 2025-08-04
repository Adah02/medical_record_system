

class MedicalHistory:
    def __init__(self,patient_id: int, past_illness: str, current_illness: str, allergies: str, medication: str):
        self.patient_id = patient_id
        self.past_illness = past_illness
        self.present_illness = current_illness
        self.allergies = allergies
        self.medications = medication

    @staticmethod
    def validate_patient_id(patient_id: int):
        if 0 > patient_id:
            raise ValueError('Patient ID must be greater than 0')
        self.patient_id = patient_id

