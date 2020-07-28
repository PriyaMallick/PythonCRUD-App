import pyodbc
# connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-NL24SKCL;'
                      'Database=projecttest;'
                      'Trusted_Connection=yes;')
cur = conn.cursor()

#to view employee table
def allentries():
    try:
        cur.execute('SELECT * FROM dbo.EmployeeDetails')
        for row in cur:
            print(row)
    except:
        print("Something went wrong! Try again")

#to view employee details
def view():
    try:
        l = check()
        empid = input("enter the empid of employee: ")
        if int(empid) not in l:
            print("Wrong input! Please give the correct employee id")
        else:
            query = "SELECT * FROM dbo.EmployeeDetails where EmpId = ?"
            cur.execute(query, [str(empid)])
            for row in cur:
                print(row)
    except:
        print("Something went wrong! Try again")

#to add new employee
def add():
    try:
        empid = int(input("enter the employee id: "))
        empname = input("enter employee name: ")
        designation = input("enter the designation: ")
        salary = int(input("enter salary: "))
        query = "INSERT INTO dbo.EmployeeDetails (EmpId,EmpName,Designation,Salary) values (?,?,?,?)"
        cur.execute(query, [empid, empname, designation, salary])
        conn.commit()
        print("Employee Added")
    except:
        print("Something went wrong! Try again")

#to update records
def update():
    try:
        l=check()
        opt = int(input("enter empid of employee whose details need to be modified: "))
        if int(opt) not in l:
            print("Wrong input! Please give the correct employee id")
        else:
            print("options: ")
            print("1:Employee Name")
            print("2:Employee Designation")
            print("3:Employee ID")
            option = int(input('enter the field that needs to be modified: '))
            if (option == 1):
                newEmpName = input("enter modified employee name: ")
                query = "UPDATE dbo.EmployeeDetails SET EmpName = ? where EmpId = ?"
                cur.execute(query, [newEmpName, opt])
                conn.commit()
            elif (option == 2):
                newDesignation = input("enter designation: ")
                query = "UPDATE dbo.EmployeeDetails SET Designation = ? where EmpId = ?"
                cur.execute(query, [newDesignation, opt])
                conn.commit()
            elif (option == 3):
                newSalary = int(input("enter modified salary: "))
                query = "UPDATE dbo.EmployeeDetails SET Salary = ? where EmpId = ?"
                cur.execute(query, [newSalary, opt])
                conn.commit()
            else:
                print("invalid option")
            print("Updated")
    except:
        print("Something went wrong! Try again")
#to perform delete operation
def delete():
    try:
        l = check()
        deleteid = int(input("enter the employee id of employee to be removed: "))
        if int(deleteid) not in l:
            print("Wrong input! Please give the correct employee id")
        else:
            query = "DELETE FROM dbo.EmployeeDetails where EmpId = ?"
            cur.execute(query, [deleteid])
            conn.commit()
            print("Employee details deleted")
    except:
        print("Something went wrong! Try again")
#main function
def main():
    try:
        print("Operations:")
        print("0.View whole table")
        print("1. Add new employee")
        print("2. View an employee details")
        print("3. Update employee details")
        print("4. Delete employee details")
        a = int(input("Enter the operation to be performed: "))
        if (a == 0):
            allentries()
        elif (a == 1):
            add()
        elif (a == 2):
            view()
        elif (a == 3):
            update()
        elif (a == 4):
            delete()
        else:
            print("enter a valid option")
        x= input("Do you want to perform more operations (Yes/No) :  ")
        if (x.lower()=="yes"):
            main()
        else:
            print("Bye!")
    except:
        print("Something went wrong! Try again")
#to check employee id is present or not
def check():
    try:
        cur.execute("select EmpId from dbo.EmployeeDetails")
        list = []
        for row in cur:
            list.append(row[0])
        return list
    except:
        print("Something went wrong! Try again")
main()
