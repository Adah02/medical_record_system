from random import choice

from medical_records import medical_record
admin = medical_record.Admin()

login_username = input("Enter your login username: ")
login_password = input("Enter your login password: ")
admin.login(login_username, login_password)

medical_menu = '''
    Welcome to Specialist Hospital
    press:-
    1 -> Add doctor
    2 -> Delete record
    3 -> View doctors
    4 -> Edit record
    5 -> Register patient
    6 -> View patient's record
    7 -> Edit patient's record
    8 -> Delete patient's record
    9 -> Book appointment
    10 -> Quit
'''
while True:
    print(medical_menu)
    choice = input('Enter your choice: ')
    match choice:
        case '1':
            log_user = input("Enter new login username: ")
            log_password = input("Enter new login password: ")
            admin.set_login(log_user, log_password)
            doctors_id = int(input('Enter doctor id: '))
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            speciality = input('Enter speciality: ')
            admin.add_doctor_to_list(doctors_id, first_name, last_name, speciality)
            print('Doctor Added successfully!...')
        case '2':
            doctors_id = int(input('Enter doctor id: '))
            first_name = input('Enter first name: ')
            admin.delete_doctor_from_list(doctors_id, first_name)
        case '3':
            users_choice = input(f'Press:- \n 1 -> View all doctors \n 2 -> View a doctor\'s record \n')
            match users_choice:
                case '1':
                    print(admin.view_doctors())
                case '2':
                    doctors_id = int(input('Enter doctor id: '))
                    first_name = input('Enter first name: ')
                    print(admin.view_doctors_detail_in_list(doctors_id, first_name))
                case _:
                    print('Invalid input')
        case '4':
            doctors_id = int(input('Enter doctor id: '))

        case '5':
            user_name = input('Enter new login username: ')
            pass_word = input('Enter new login password: ')
            admin.set_login(user_name, pass_word)

            patient_id = int(input('Enter doctor id: '))
            first_name = str(input('Enter first name: '))
            last_name = str(input('Enter last name: '))
            gender = str(input('Enter gender: '))
            date_of_birth = str(input('Enter date of birth in (DD, MM, YYYY) format: '))
            phone_number = str(input('Enter phone number: '))
            admin.register_a_patient(patient_id, first_name, last_name, gender, date_of_birth, phone_number)

        case '6':
            patient_id = int(input('Enter doctor id: '))
            first_name = input('Enter first name: ')
            print(admin.view_patient_record(patient_id, first_name))

        case '8':
            patient_id = int(input('Enter doctor id: '))
            first_name = input('Enter first name: ')
            admin.delete_patient_from_list(patient_id, first_name)

        case '9':
            patient_id = int(input('Enter patient id: '))
            found_id = admin.find_patient(patient_id)

            if found_id:
                date_time = input('Enter date and time in (DD,MM,YYYY hh:mm): ')
                status = input('Enter patient status: ')
                reason = input('Enter patient reason for appointment: ')
                doctors_id = int(input('Enter doctor id: '))
                location = str(input('Enter location: '))
                admin.generate_appointment(patient_id, date, time, status, reason, doctors_id, location)
            else:
                print('patient not found')

        case '10': break
