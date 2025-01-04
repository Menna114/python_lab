from inputs_module import passwordCheck, phoneCheck, emailCheck, validateStringInput, dateCheck, checkIfEmailExists, checkIntInput, checkOwner, checkIdExists
from file_operations import registered_users, generate_id, read_all_users, generate_project_id ,registered_projects, view_projects ,edit_title, edit_details, edit_total_target, edit_start_date, edit_end_date,delete_project_from_file
def Registration():
    try:
        first_Name = input("Enter your First name: ")
        validateStringInput(first_Name)

        last_Name = input("Enter your Last name: ")
        validateStringInput(last_Name)

        email = input("Enter your email: ")
        emailCheck(email)
        checkIfEmailExists(email)

        phone = input("Enter your phone: ")
        phoneCheck(phone)

        password = input("Enter your password: ")
        confirmationPassword = input("Confirm your password: ")
        passwordCheck(password, confirmationPassword)
        user_id = generate_id()
        Registration_data = {
            "id": user_id,
            "first_name": first_Name,
            "last_name": last_Name,
            "email": email,
            "phone": phone,
            "password": password
        }

        #print(f"User Data: {Registration_data}")
        print("Registration successful")
        saved=registered_users(Registration_data)
    
    except ValueError as e:
        print(f"Error: {e}")

def login():
    try:
        email = input("Enter your email: ")
        emailCheck(email)

        password = input("Enter your password: ")
        validateStringInput(password)
        
        users_list = read_all_users()
        for user in users_list:
            if user["email"] == email and user["password"] == password:
                print("Login successful")
                return user["id"]
        else:
            print("Invalid email or password")
            return False
    except ValueError as e:
        print(f"Error: {e}")


def create_project(user_id):
    try:
        title = input("Enter project title: ")
        details = input("Enter project details: ")
        totalTarget = input("Enter total target: ")
        checkIntInput(totalTarget)
        startDate= input("Enter the project start date: ")
        dateCheck(startDate)
        endDate= input("Enter the project end date: ")
        dateCheck(endDate)
        project_id=generate_project_id()
        project_data = {
            "id": project_id,
            "user_id": user_id,
            "title": title,
            "details": details,
            "total_target": totalTarget,
            "start_date": startDate,
            "end_date": endDate
        }
        #print(f"Project Data: {project_data}")
        print("Project created successfully")
        saved = registered_projects(project_data)
    except ValueError as e:
        print(f"Error: {e}")

def view_all_projects():
    view_projects()

def edit_project(user_id):
    try:
        project_id=input("Enter the project id you want to edit : ")
        checkIntInput(project_id)
        project_id=int(project_id)
        flag2=checkIdExists(project_id)
        if flag2 == True:
            flag=checkOwner(user_id,project_id)
            if flag ==True:
                choice=input("What do you want to edit? \n1- Title \n2- Details \n3- Total Target \n4- Start Date \n5- End Date \n6- Cancel \n")
                if choice == "1":
                    title=input("Enter the new title: ")
                    edit_title(project_id,title)
                if choice == "2":
                    details=input("Enter the new details: ")
                    edit_details(project_id,details)
                if choice == "3":
                    totalTarget=input("Enter the new total target: ")
                    checkIntInput(totalTarget)
                    edit_total_target(project_id,totalTarget)
                if choice == "4":
                    startDate=input("Enter the new start date: ")
                    dateCheck(startDate)
                    edit_start_date(project_id,startDate)
                if choice == "5":
                    endDate=input("Enter the new end date: ")
                    dateCheck(endDate)
                    edit_end_date(project_id,endDate)
                if choice == "6":
                    return
    except ValueError as e:
        print(f"Error: {e}")


def delete_project(user_id):
    try:
        project_id=input("Enter the project you want to delete : ")
        checkIntInput(project_id)
        project_id=int(project_id)
        flag2=checkIdExists(project_id)
        if flag2 == True:
            flag=checkOwner(user_id,project_id)
            if flag ==True:
                delete_project_from_file(user_id,project_id)

    except ValueError as e:
        print(f"Error: {e}")

def search_project():
    pass
