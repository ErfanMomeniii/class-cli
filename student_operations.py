from os import system
from datetime import datetime
from datetime import date
clear = lambda : system("cls")
global active_students
global graduated_students

from pickle import load
try :
    with open("ActiveStudents.db","rb") as active_students_arr :
       active_students = load(active_students_arr)
except(FileNotFoundError) :
    active_students=[]
try :
    with open("GraduatedStudents.db","rb") as graduated_students_arr :
        graduated_students = load(graduated_students_arr)
except(FileNotFoundError) :
    graduated_students=[]

def find_average(lis):
    res = 0
    for li in lis:
        res +=li
    res /=len(lis)
    return res    

def find_max(lis):
    res = lis[0]
    for li in lis:
        if li > res:
            res= li
    return res    


def find_min(lis):
    res = lis[0]
    for li in lis:
        if li < res:
            res= li
    return res    


def check_duplicate_code_melli(number) :
    for student in active_students :
        if number == student["code_melli"] :
            return False
    return True
def check_duplicate_student_code(number) :
    for student in active_students :
        if number == student["student_code"] :
            return False
    return True

def add_student() :
    clear()
    student = dict()
    student["first_name"] = input("Enter student first name : ")
    student["last_name"] = input("Enter student last name : ")
    student["birthday"] = input("Enter student birthday (yyyy/mm/dd) : ")
    if student["birthday"] != datetime.strptime(student["birthday"], "%Y/%m/%d").strftime('%Y/%m/%d'):
        input("This is the incorrect date string format. It should be YYYY/MM/DD")
        input("Press any key ...")
        return
    code_melli = input("Enter code melli (10 digit number) : ")
    if len(code_melli) != 10 or check_duplicate_code_melli(code_melli) == False :
        print("Code Melli is a 10 Unique Characters code like : xxxxxxxxxx")
        input("Press any key ...")
        return 
    else :
        student["code_melli"] = code_melli
    

    student_code = input("Enter student code (5 digit number) : ")
    if len(student_code) != 5 or check_duplicate_student_code(student_code) == False :
        print("Student Code is a 5 Unique Characters code like : xxxxx")
        input("Press any key ...")
        return 
    else :
        student["student_code"] = student_code
    student["courses"] = list()
    student["grades"]= list()
    while True:    
        student["courses"].append(input("Enter course name : "))
        student["grades"].append(float(input("Enter grades : ")))
        l = input("Do you want to add more?(Y/N):")
        if l == "N":
            break
    active_students.append(student)

def find_student() :
    clear()
    student_code = input("Enter student code to find student : ")
    for student in active_students :
        if student ["student_code"] == student_code :
            print(f"first name : {student['first_name']}")
            print(f"last name : {student['last_name']}")
            print(f"birthday : {student['birthday']}")
            print(f"code melli : {student['code_melli']}")
            print(f"student code : {student['student_code']}")
            print(f"student average grade : {find_average(student['grades'])}")
            print(f"student max grade : {find_max(student['grades'])}")
            print(f"student min grade : {find_min(student['grades'])}")
            print(f"student age : {int(date.today().strftime('%Y'))-int(datetime.strptime(student['birthday'], '%Y/%m/%d').strftime('%Y'))}")
            print("--------------------------------------")
            input()
            return     
    print("Not Found !")    
    input()
    return          

def delete_student() :
    clear()
    student_code = input("Enter student code to find student : ")
    for student in active_students :
        if student ["student_code"] == student_code :
            print(f"first name : {student['first_name']}")
            print(f"last name : {student['last_name']}")
            print(f"birthday : {student['birthday']}")
            print(f"code melli : {student['code_melli']}")
            print(f"student code : {student['student_code']}")
            print(f"student average grade : {find_average(student['grades'])}")
            print(f"student max grade : {find_max(student['grades'])}")
            print(f"student min grade : {find_min(student['grades'])}")
            print(f"student age : {int(date.today().strftime('%Y'))-int(datetime.strptime(student['birthday'], '%Y/%m/%d').strftime('%Y'))}")
            print("--------------------------------------")
            l = input("Do you want to completely delete or move?(D/M):")
            if l == "D":
                active_students.remove(student)
                print("Done!")
            elif l == "M":
                graduated_students.append(student)
                active_students.remove(student)
                print("Done!")
            else   :
                print("Try again") 
                return         
            input()
            return   
    print("Not Found !")    
    input()
def change_courses() :
    clear()
    student_code = input("Enter student code to find student : ")
    for student in active_students :
        if student ["student_code"] == student_code :
            l = input("Do you want to change first_name?(Y/N):")
            if l == "Y" :
                student["first_name"] = input("Enter student first name : ")
            l = input("Do you want to change last_name?(Y/N):")
            if l == "Y" :
                student["last_name"] = input("Enter student last name : ")
            l = input("Do you want to change birthday?(Y/N):")
            if l == "Y":
                bir = input("Enter student birthday (yyyy/mm/dd) : ")
                if bir != datetime.strptime(bir, "%Y/%m/%d").strftime('%Y/%m/%d'):
                    input("This is the incorrect date string format. It should be YYYY/MM/DD")
                    input("Press any key ...")
                else : 
                    student["birthday"]=bir
            l = input("Do you want to change code melli?(Y/N):")
            if l == "Y":
                code_melli = input("Enter code melli (10 digit number) : ")
                if len(code_melli) != 10 or check_duplicate_code_melli(code_melli) == False :
                    print("Code Melli is a 10 Unique Characters code like : xxxxxxxxxx\nCode melli did not change")
                else :
                    student["code_melli"] = code_melli
            l = input("Do you want to change student code?(Y/N):")
            if l == "Y":
                student_code = input("Enter student code (5 digit number) : ")
                if len(student_code) != 5 or check_duplicate_student_code(student_code) == False :
                    print("Student Code is a 5 Unique Characters code like : xxxxx\nstudent code did not change")
                else :
                    student["student_code"] = student_code
            l = input("Do you want to add or remove grades?(Y/N)")
            if l=="Y":  
                l = input("Add or Remove?(A/R)")  
                if l == "A":
                    while True:    
                        student["courses"].append(input("Enter course name : "))
                        student["grades"].append(float(input("Enter grades : ")))
                        l = input("Do you want to add more?(Y/N):")
                        if l == "N":
                            break
                elif l == "R":
                    course_input = input("Enter course name:")
                    ind = 0
                    for course in student["courses"]:
                        if course == course_input:
                            student["courses"].pop(ind)
                            student["grades"].pop(ind)
                            print("Done!")
                            input()
                            return 
                    print("Not Found !")
                    input()
                    return 
            print("Done!")        
            input()
            return      
    print("Not Found !")    
    input()

def list_students() :
    print("-----------ACTIVE  STUDENTS-----------")
    for student in active_students :
        print(f"first name : {student['first_name']}")
        print(f"last name : {student['last_name']}")
        print(f"birthday : {student['birthday']}")
        print(f"code melli : {student['code_melli']}")
        print(f"student code : {student['student_code']}")
        print(f"student average grade : {find_average(student['grades'])}")
        print(f"student max grade : {find_max(student['grades'])}")
        print(f"student min grade : {find_min(student['grades'])}")
        print(f"student age : {int(date.today().strftime('%Y'))-int(datetime.strptime(student['birthday'], '%Y/%m/%d').strftime('%Y'))}")
        print("--------------------------------------")
    print("----------GRADUATED STUDENTS----------")
    for student in graduated_students :
        print(f"first name : {student['first_name']}")
        print(f"last name : {student['last_name']}")
        print(f"birthday : {student['birthday']}")
        print(f"code melli : {student['code_melli']}")
        print(f"student code : {student['student_code']}")
        print(f"student average grade : {find_average(student['grades'])}")
        print(f"student max grade : {find_max(student['grades'])}")
        print(f"student min grade : {find_min(student['grades'])}")
        print(f"student age : {int(date.today().strftime('%Y'))-int(datetime.strptime(student['birthday'], '%Y/%m/%d').strftime('%Y'))}")
        print("--------------------------------------")
    input("Press any key ...")

def save_students() :    
    from pickle import dump
    try :
        with open("ActiveStudents.db","wb") as  active_students_arr:
            dump(active_students,active_students_arr)
        with open("GraduatedStudents.db","wb") as graduated_students_arr :
            dump(graduated_students,graduated_students_arr)
            print("File has been saved succesfuly")
            input("Press any key ...")
    except(PermissionError) :
        print("File can not be save due to Operating System Permissions")
        input("Press any key ...")
        return 
    except :
        print("Save Error !")
        input("Press any key ...")
        return
