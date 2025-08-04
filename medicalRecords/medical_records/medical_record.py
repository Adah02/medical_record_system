from medical_records import patient
from medical_records.medical_history import MedicalHistory
from medical_records.patient import Patient
from medical_records.doctor import Doctor
from medical_records.appointment import Appointment

class Admin:
    def __init__(self):
        self.user_name = "admin"
        self.pass_word = "admin"
        self.__doctors = list()
        self.__patients = list()
        self.__appointments = list()


    def admin_login(self, username, password):
        if self.user_name == username and self.pass_word == password:
            return True
        raise ValueError('Invalid username or password')


    @staticmethod
    def validate_login_username(username):
        if username == '' or len(username) > 15:
            raise ValueError("Username cannot be empty or greater than 15 characters")
        return username

    @staticmethod
    def validate_login_password(pass_key):
        if pass_key == '' or len(pass_key) > 15:
            raise ValueError("Password cannot be empty or greater than 15 characters")
        return pass_key

    def set_login(self, username, password):
        self.validate_login_username(username)
        self.validate_login_password(password)
        self.user_name = username
        self.pass_word = password


    @staticmethod
    def logout():
        return False

    def doctor_login(self, user_name, pass_key):
        for doctor in self.__doctors:
            if doctor.username == user_name and doctor.password == pass_key:
                return True
        raise ValueError('Invalid username or password')

    def patient_login(self, username, pass_key):
        for patient in self.__patients:
            if patient.username == username and patient.password == pass_key:
                return True
        raise ValueError('Invalid username or password')

    def get_doctors_list(self):
        return len(self.__doctors)

    def add_doctor_to_list(self,username: str, password: str, id_number: int, first_name: str, last_name: str, speciality: str) -> None:
        self.__doctors.append(Doctor(username, password, id_number, first_name, last_name, speciality))

    def delete_doctor_from_list(self, id_number: int, name: str) -> none:
        isFound = False
        for doctor in self.__doctors:
            if doctor.doctor_id == id_number and doctor.first_name == name:
                self.__doctors.remove(doctor); isFound = True
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

    def register_a_patient(self,user_name: str, pass_word: str, patient_id: int,first_name: str, last_name: str, gender, dob, phone: str) -> None:
        self.__patients.append(Patient(user_name, pass_word, patient_id, first_name, last_name, gender, dob, phone))

    def delete_patient_from_list(self, id_number: int, first_name: str) -> None:
        isFound = False
        for patient in self.__patients:
            if patient.patient_id == id_number and patient.first_name == first_name:
                self.__patients.remove(patient); isFound = True
        if not isFound:
            raise ValueError('Patient not found')

    def view_patient_record(self, patient_id: int, first_name: str) -> str:
        for patient, history, appointment in zip_longest(self.__patients, self.__medical_history, self.__appointments, fillvalue=''):
            if patient.patient_id == patient_id and patient.first_name.lower() == first_name.lower():
                print(f'{str(patient)}\n')
                continue
            if history.patient_id == patient_id:
                print(f'{str(history)}\n')
                continue
            if appointment.patient_id == patient_id:
                print(f'{str(appointment)}')
                continue

    def find_patient(self, patient_id: int) -> Patient:
        if patient_id in self.__patients:
            return true

    def generate_appointment(self,patient_id, date: str, time: str, status: str, reason: str, doctors_id, location: str ) -> None:
        self.patient.__appointments.append(Appointment(patient_id, date, time, status, reason, doctors_id, location))

    def view_appointment(self, patient_id):
        if not patient_id in self.__appointments:
            raise ValueError("No appointment found for patient")
        for appointment in self.__appointments:
            if appointment.patient_id == patient_id:
                return f"{str(appointment)}"

    def get_patient_list(self) -> int:
        return len(self.__patients)

    def get_appointment_list(self) -> int:
        return len(self.__appointments)