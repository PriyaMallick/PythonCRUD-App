import pyodbc
#connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-NL24SKCL;'
                      'Database=projecttest;'
                      'Trusted_Connection=yes;')
cur = conn.cursor()
print("Operations:")
print("0.View whole table")
print("1. Add new employee")
print("2. View an employee details")
print("3. Update employee details")
print("4. Delete employee details")
a = int(input("Enter the operation to be performed: "))

#operations
def allentries():
    cur.execute('SELECT * FROM dbo.EmployeeDetails')
    for row in cur:
        print(row)
def view():
    empid = input("enter the empid of employee: ")
    query = "SELECT * FROM dbo.EmployeeDetails where EmpId = ?"
    cur.execute(query, [str(empid)])
    for row in cur:
        print(row)


def add():
    empid = int(input("enter the employee id: "))
    empname = input("enter employee name: ")
    designation = input("enter the designation: ")
    salary = int(input("enter salary: "))
    query = "INSERT INTO dbo.EmployeeDetails (EmpId,EmpName,Designation,Salary) values (?,?,?,?)"
    cur.execute(query, [empid, empname, designation, salary])
    conn.commit()
    print("Employee Added")


def update():
    opt = int(input("enter empid of employee whose details need to be modified: "))
    print("options: ")
    print("1:Employee Name")
    print("2:Employee Designation")
    print("3:Employee ID")
    option = int(input('enter the field that needs to be modified: '))
    if (option == 1):
        newEmpName = input("enter modified employee name: ")
        query = "UPDATE dbo.EmployeeDetails SET EmpName = ? where EmpId = ?"
        cur.execute(query, [newEmpName,opt])
        conn.commit()
    elif (option == 2):
        newDesignation = input("enter designation: ")
        query = "UPDATE dbo.EmployeeDetails SET Designation = ? where EmpId = ?"
        cur.execute(query, [newDesignation,opt])
        conn.commit()
    elif (option == 3):
        newSalary = int(input("enter modified salary: "))
        query = "UPDATE dbo.EmployeeDetails SET Salary = ? where EmpId = ?"
        cur.execute(query, [newSalary,opt])
        conn.commit()
    else:
        print("invalid option")
    print("Updated")


def delete():
    deleteid = int(input("enter the employee id of employee to be removed: "))
    query = "DELETE FROM dbo.EmployeeDetails where EmpId = ?"
    cur.execute(query, [deleteid])
    conn.commit()
    print("Employee details deleted")

if (a==0):
    allentries()
if(a==1):
    add()
elif(a==2):
    view()
elif(a==3):
    update()
elif(a==4):
    delete()
else:
    print("enter a valid option")
