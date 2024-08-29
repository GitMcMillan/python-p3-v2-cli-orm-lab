from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
# get all departments stored in the database. Print each on a new line
    # create a variable to store get_all() result    
    departments = Department.get_all() 
    # loop over every department in departments
    for department in departments:
        #and print them
        print(department)   


def find_department_by_name():
    #create variable to print enter name query
    name = input("Enter the department's name: ")
    # create variable to store named department
    department = Department.find_by_name(name)
    #print department if it exists
    print(department) if department else print(
        #else print not found message
        f'Department {name} not found'
    )


def find_department_by_id():
    #create variable to print name query
     # use a trailing underscore not to override the built-in id function
    id_ = input("Enter Department Id: ")
    #create variable to store found id
    department_id = Department.find_by_id(id_)
    # print department if it exists:
    print(department_id) if department_id else print(
    #else print no id found message
        f'Department {id_} not found'
    )


def create_department():
    # create variable to print prompts for name/location
    name = input("Enter Department name: ")
    location = input("Enter Department location: ")
    #create try/except block in case of exception
    try:
        #try creating department with name/location
        department = Department.create(name, location)
        #print success if successful
        print(f'Success: {department}')
    #create exception for try 
    except Exception as exc:
        #print the exception error
        print("Error creating department: ", exc)



def update_department():
    #create variable for input asking for id
    id_ = input("Enter the department's id: ")
    #check if id exists
    if department := Department.find_by_id(id_):
        #try name/location input
        try:
            name = input("enter the department's new name: ")
            # give department.name a name variable
            department.name = name
            location = input("enter the department's new location: ")
            # give department.location a location variable
            department.location = location

            #run update method
            department.update()
            #print if successful
            print(f'Success: {department}')
        #create exception if error
        except Exception as exc:
            #print err exception
            print("Error updating department: ", exc)
        #print else not found
    else:
        print(f'Department {id_} not found')


def delete_department():
    #prompt for id
    id_ = input("Enter Department Id: ")
    #If Id exists, store it
    if department := Department.find_by_id(id_):
        #delete it
        department.delete()
        #print success
        print(f'Department {id} deleted')
    #else print not found
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    # create variable to store employees
    employees = Employee.get_all()
    #loop over employees 
    for employee in employees:
        #print each employee
        print(employee)




def find_employee_by_name():
    # create input for name
    name = input("Enter employee's name: ")
    # search for name and store it
    employee = Employee.find_by_name(name)
    #print employee if exists
    print(employee) if employee else print(
        #else print does not found
        f'Employee {name} not found'
    )



def find_employee_by_id():
    # create variable for input prompt
    id_ = input("Enter Employee Id: ")
    # if id exists, store it
    employee_id = Employee.find_by_id(id_)
    # if it exists, print it
    print(employee_id) if employee_id else print(
        #print id does not exists
        f'Employee {id_} not found'
    )


def create_employee():
    #create input prompt for name, job title and department id
    name = input("Enter Employee name: ")
    job_title = input("Enter employee job title: ")
    department_id = int(input("Enter Department Id: "))
    #try/except for the values
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f'Success {employee}')
    except Exception as exc:
        #print the exception error
        print("Error creating employee", exc)

    

def update_employee():
    #create the input
    id_ = input("Enter employee Id: ")
    #capture the employee id
    if employee := Employee.find_by_id(id_):
        #try/else capture attributes with input
        try:
            #capture employee name
            name = input("Enter employee name: ")
            # update employee.name to new name value
            employee.name = name
            #capture employee job title
            job_title = input("Enter employee job title: ")
            #update employee.job_title to new value
            employee.job_title = job_title
            #capture employee department id
            department_id = int(input("Enter employee Department Id: "))
            #update department id to new value from input
            employee.department_id = department_id 

            #run employee update method:
            employee.update()
            #print success
            print(f"Employee {name} updated successfully")
            #make exception for error
        except Exception as exc:
            #print error
            print(f"Error updating employee: {name}", exc)
        #else print not found
    else:
            print(f'Employee {id_} not found')



   
     



def delete_employee():
    #input capture employee id
    id_ = input("Enter employee id: ")
    #store value from input
    employee = find_employee_by_id(id_)
    #if employee exists delete that employee id
    if employee := employee.delete(employee):
        #print success
        print(f'{employee} deleted')
    #else print not found
    else:
        print(f'{id_} not found')



def list_department_employees():
    #capture department id with input
    id_ = input("Enter Department id: ")
    #store id as department
    department = Department.find_by_id(id_)
    # get all employees from department if it exists
    if department:
        employees = Employee.get_all()
        #loop over department employees
        for employee in employees:
            #print out each employee
            print(employee)
    else:
        print(f'{id_} not found')
