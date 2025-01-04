
from operations import Registration, login, create_project, view_all_projects,edit_project,delete_project

def main_menu():
    while True:
        choice = input("""
                       1- Login 
                       2- Register 
                       3- Exit
                       """)
        if choice == "1":
            user_id=login()
            print(user_id)
            if user_id:
                while True:
                    choice2=input("""
                            1- Create project
                            2- View all projects
                            3- Edit your project
                            4- Delete your project
                            5- Search for a project
                            6- Exit   
                            """)
                    if choice2 == "1":
                        create_project(user_id)
                    elif choice2 == "2":
                        view_all_projects()
                    elif choice2 == "3":
                        edit_project(user_id)
                    elif choice2 == "4":
                        delete_project(user_id) 
                    elif choice2 == "5":
                        print("Search for a project")
                    elif choice2 == "6":
                        break
                    else:
                        print("Invalid choice")
        elif choice == "2":
            Registration()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice")
            continue

if __name__ == "__main__":
        main_menu()

