

class Appointment:
    def __init__(self,patient_id, date: str, time: str, status: str, reason: str, doctor_id, location: str ) -> None:
        self.__patient_id = patient_id
        self.date_time = datetime.now()
        self.__status = status
        self.__reason = reason
        self.__doctor_id = doctor_id
        self.__location = location

    
    def appointment_date(self):
        self.date_time = self.datetime.strftime = f"%m %d %Y %I:%M %p"
        return self.date_time

    def get_patient_id(self):
        return self.__patient_id

    def get_status(self):
        return self.__status

    def get_reason(self):
        return self.__reason

    def get_doctor_id(self):
        return self.__doctor_id

    def get_location(self):
        return self.__location

    def __str__(self):
        return f'{get_patient_id()}\n{self.date_time}\n{get_status()}\n{get_reason()}\n{get_doctor_id()}\n{get_location()}'