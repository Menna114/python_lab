import re ,datetime
from file_operations import read_all_users , read_all_projects

def validateStringInput(inputString):
    if not inputString:
        raise ValueError("Input cannot be empty")
    if not inputString.isalpha():
        raise ValueError("Input must be a string")
    
def passwordCheck(password, confirmationPassword):
    if password == confirmationPassword:
        return True 
    else:
        raise ValueError("password does not match")

        
def phoneCheck(phone):
    pattern = r"^20\d{10}$"
    if not re.match(pattern,phone):
        raise ValueError("Invalid phone number")
    

def emailCheck(email):

    pattern = r"^[a-zA-Z0-9._%+-]+@(?:gmail|yahoo|email|net)\.com$"
    if not re.match(pattern,email):
        raise ValueError("Invalid email format")
    
def dateCheck(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    
def checkIfEmailExists(email):
    users_list = read_all_users()
    for user in users_list:
        if user["email"] == email:
            raise ValueError("Email already exists")
        
def checkIntInput(inputString):
    if not inputString:
        raise ValueError("Input cannot be empty")
    if not inputString.isdigit():
        raise ValueError("Input must be a number")
    
def checkOwner(project_id, user_id):
    projects_list = read_all_projects()
    for project in projects_list:
        if project["id"] == project_id and project["user_id"] == user_id:
            return True
    else:
        print("You are not the owner of this project")
        return False
