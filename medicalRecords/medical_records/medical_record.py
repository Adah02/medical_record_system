from medical_records import patient
from medical_records.medical_history import MedicalHistory
from medical_records.patient import Patient
from medical_records.doctor import Doctor
from medical_records.appointment import Appointment

class Admin:
    def __init__(self):
        self.__doctors = list()
        self.__patients = list()
        self.__medical_history = list()
        self.__appointments = list()
        self.__login_details = [{'username': "admin", 'password': "admin"}]

    def set_login(self, username, password):
        self.__login_details.append({'username': username, 'password': password})

    def login(self, username, password):
        is_found = False
        for login in self.__login_details:
            if username in login['username'] and password in login['password']:
                return True;  is_found = True
        if not is_found:
            raise ValueError('Login failed')

    def get_doctors_list(self):
        return len(self.__doctors)

    def add_doctor_to_list(self, id_number: int, first_name: str, last_name: str, speciality: str) -> None:
        self.__doctors.append(Doctor(id_number, first_name, last_name, speciality))

    def delete_doctor_from_list(self, id_number: int, name: str) -> none:
        isFound = False
        for doctor in self.__doctors:
            if doctor.doctor_id == id_number and doctor.first_name == name:
                self.__doctors.remove(doctor)
                isFound = True
        if not isFound:
            raise Exception("Doctor not found")

    def view_doctors_detail_in_list(self, id_number: int, name: str) -> str:
        if len(self.__doctors) == 0:
            raise Exception("Doctor not found")
        for doctor in self.__doctors:
            if doctor.doctor_id == id_number and doctor.first_name.lower() == name.lower():
                return f"{str(doctor)}"

    def view_doctors(self):
        for doctor in self.__doctors:
            return f"{str(doctor)}"
        if len(self.__doctors) == 0:
            return 'No doctors found'

    def register_a_patient(self, patient_id: int,first_name: str, last_name: str, gender, dob, phone: str) -> None:
        self.__patients.append(Patient(patient_id, first_name, last_name, gender, dob, phone))

    def delete_patient_from_list(self, id_number: int, first_name: str) -> None:
        isFound = False
        for patient in self.__patients:
            if patient.patient_id == id_number and patient.first_name == first_name:
                self.__patients.remove(patient)
                isFound = True
        if not isFound:
            raise ValueError('Patient not found')

    def view_patient_record(self, patient_id: int, first_name: str) -> str:
        for patient, history, appointment in zip_longest(self.__patients, self.__medical_history, self.__appointments, fillvalue=''):
            if patient.patient_id == patient_id and patient.first_name.lower() == first_name.lower():
                return f'{str(patient)}\n\n{str(appointment)}\n'
            if history.patient_id == patient_id:
                return f'{str(history)}'
            if appointment.patient_id == patient_id:
                return f'{str(appointment)}'

    def create_medical_history(self, record_id: int, past_illness: str, present_illness: str, allergies: str, medications: str) -> None:
        self.__medical_history.append(MedicalHistory(record_id, past_illness, present_illness, allergies, medications))

    def update_medical_history(self,record_id: int, past_illness: str, present_illness: str, allergies: str, medications: str ) -> None:
        for record in self.__medical_history:
            if record.record_id == record_id:
                record.medical_history = MedicalHistory(record_id, past_illness, present_illness, allergies, medications)

    def find_patient(self, patient_id: int) -> Patient:
        if patient_id in self.__patients:
            return true

    def generate_appointment(self,patient_id, date: str, time: str, status: str, reason: str, doctors_id, location: str ) -> None:
        self.patient.__appointments.append(Appointment(patient_id, date, time, status, reason, doctors_id, location))

    def view_appointment(self, patient_id):
        for appointment in self.__appointments:
            if appointment.patient_id == patient_id:
                return f"{str(appointment)}"
        if patient_id in self.__appointments:
            return "No appointment found for patient"


    def get_patient_list(self) -> int:
        return len(self.__patients)

    def get_appointment_list(self) -> int:
        return len(self.__appointments)