

class Appointment:
    def __init__(self,patient_id, date: str, time: str, status: str, reason: str, doctor_id, location: str ) -> None:
        self.patient_id = patient_id
        self.date_time = datetime.now()
        self.status = status
        self.reason = reason
        self.doctor_id = doctor_id
        self.location = location

    def appointment_date(self):
        self.date_time = self.datetime.strftime = f"%m %d %Y %I:%M %p"
        return self.date_time

    def __str__(self):
        return f'{self.patient_id}\n{self.date_time}\n{self.status}\n{self.reason}\n{self.doctor_id}\n{self.location}'