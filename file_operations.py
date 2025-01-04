import json


def read_all_users():
    try:
        fileobj = open("users.txt", "r")
        users_list= json.load(fileobj)
    except ValueError as e:
        return []
    return users_list

def register_all_users(user_data):
    try:
        fileobj = open("users.txt", "w")
    except ValueError as e:
        print(f"Error: {e}")
        return False
    else:
        json.dump(user_data, fileobj,indent=4)
        fileobj.close()
        return True

def registered_users(user_data):
    users_list = read_all_users()
    users_list.append(user_data)
    saved = register_all_users(users_list)
    return saved

def generate_id():
    try:
        fileobj = open("id", "r")
        id = int(fileobj.read())
        id += 1
        fileobj.close()
        fileobj = open("id", "w")
        fileobj.write(str(id))
        fileobj.close()
    except ValueError as e:
        return 1
    else:
        return id
    
def generate_project_id():
    try:
        fileobj = open("project_id", "r")
        id = int(fileobj.read())
        id += 1
        fileobj.close()
        fileobj = open("project_id", "w")
        fileobj.write(str(id))
        fileobj.close()
    except ValueError as e:
        return 1
    else:
        return id
    
def read_all_projects():
    try:
        fileobj = open("projects.txt", "r")
        projects_list= json.load(fileobj)
    except ValueError as e:
        return []
    return projects_list

def register_all_projects(project_data):
    try:
        fileobj = open("projects.txt", "w")
    except ValueError as e:
        print(f"Error: {e}")
        return False
    else:
        json.dump(project_data, fileobj,indent=4)
        fileobj.close()
        return True
    
def registered_projects(project_data):
    projects_list = read_all_projects()
    projects_list.append(project_data)
    saved = register_all_projects(projects_list)
    return saved

def view_projects():
    projects_list = read_all_projects()
    if projects_list == []:
        print("No projects available")
        return
    for project in projects_list:
        print(f"Project ID: {project['id']}")
        print(f"Project Title: {project['title']}")
        print(f"Project Details: {project['details']}")
        print(f"Project Total Target: {project['total_target']}")
        print(f"Project Start Date: {project['start_date']}")
        print(f"Project End Date: {project['end_date']}")
        print("=====================================")

def edit_title(project_id, title):
    projects_list = read_all_projects()
    flag = False
    for project in projects_list:
        if project["id"] == project_id:
            project["title"] = title
            flag = True
            print("Title edited successfully")
            register_all_projects(projects_list)
            break
    else:
        print("Project not found")


def edit_details(project_id, details):
    projects_list = read_all_projects()
    for project in projects_list:
        if project["id"] == project_id:
            project["details"] = details
            saved = register_all_projects(projects_list)
            if saved:
                print("Details edited successfully")
                return
    else:
        print("Project not found")

def edit_total_target(project_id, total_target):
    projects_list = read_all_projects()
    for project in projects_list:
        if project["id"] == project_id:
            project["total_target"] = total_target
            saved = register_all_projects(projects_list)
            if saved:
                print("Total target edited successfully")
                return
    else:
        print("Project not found")

def edit_start_date(project_id, start_date):
    projects_list = read_all_projects()
    for project in projects_list:
        if project["id"] == project_id:
            project["start_date"] = start_date
            saved = register_all_projects(projects_list)
            if saved:
                print("Start date edited successfully")
                return
    else:
        print("Project not found")

def edit_end_date(project_id, end_date):
    projects_list = read_all_projects()
    for project in projects_list:
        if project["id"] == project_id:
            project["end_date"] = end_date
            saved = register_all_projects(projects_list)
            if saved:
                print("End date edited successfully")
                return
    else:
        print("Project not found")

def delete_project_from_file(user_id,project_id):
    project_list = read_all_projects()
    for project in project_list:
        if project["id"] == project_id and project["user_id"] == user_id:
            project_list.remove(project)
            saved = register_all_projects(project_list)
            if saved:
                print("Project deleted successfully")
                return
    else:
        print("Project not found")
