from medical_records import medical_record
from medical_records.doctor import Doctor
from medical_records import medical_record

admin = Admin()

users = '''
    Welcome to Specialist Hospital
    Press:-
    1 -> Admin
    2 -> Doctor
    3 -> Patient
    '''
while True:
    choice_ = input(users + "\n Enter choice: ")
    match choice_:
        case '1':
            login_username = input("Enter your login username: ")
            login_password = input("Enter your login password: ")
            admin.login(login_username, login_password)

            medical_menu = '''
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
            10 -> Logout
            '''

            while True:
                print(medical_menu)
                choice = input('Enter your choice: ')
                match choice:
                    case '1':
                        try:
                            log_username = input("Enter new login username: ")
                            Doctor.validate_username(log_username)

                            log_password = input("Enter new login password: ")
                            Doctor.validate_password(log_password)

                            doctors_id = int(input('Enter doctor id: '))
                            Doctor.validate_doctor_id(doctors_id)

                            first_name = input('Enter first name: ')
                            Doctor.validate_first_name(first_name)

                            last_name = input('Enter last name: ')
                            Doctor.validate_last_name(last_name)

                            speciality = input('Enter speciality: ')
                            Doctor.validate_speciality(speciality)

                            admin.add_doctor_to_list(log_username, log_password, doctors_id, first_name, last_name, speciality)
                            print('Doctor Added successfully!...')
                        except ValueError:
                            print("Invalid input, please try again")

                    case '2':
                        doctors_id = int(input('Enter doctor id: '))
                        first_name = input('Enter first name: ')
                        admin.delete_doctor_from_list(doctors_id, first_name)

                    case '3':
                        users_choice = input(f'Press:- \n 1 -> View all doctors \n 2 -> View a doctor\'s record \n 0 -> Back')
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
                        admin.register_a_patient(user_name, patient_id, pass_word, first_name, last_name, gender, date_of_birth, phone_number)

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

        case '2':
            doc_username = input("Enter your login username: ")
            doc_password = input("Enter your login password: ")
            admin.doctor_login(user_name, pass_key)

            doctors_menu = '''
                    Press:-
                    1 -> view personal information
                    2 -> View Appointments
                    3 -> View patient\'s medical records 
                    '''
            choice = input(doctors_menu +"\nEnter your choice: ")
            match choice:
                case '1':
                    id = int(input('Enter your ID: '))
                    first_name = input('Enter first name: ')
                    print(admin.view_doctors_detail_in_list(id, first_name))

        case '3':
            patient_username = input("Enter your login username: ")
            admin.validate_login_username(patient_username)
            patient_password = input("Enter your login password: ")

            admin.login(patient_username, patient_password)