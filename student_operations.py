
from os import system
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
        if student[number] == student["code_melli"] :
            return False
    return True
def check_duplicate_student_code(number) :
    for student in active_students :
        if student[number] == student["student_code"] :
            return False
    return True

def add_student() :
    clear()
    student = dict()
    student["first_name"] = input("Enter student first name : ")
    student["last_name"] = input("Enter student last name : ")
    student["birthday"] = input("Enter student birthday (yyyy/mm/dd) : ")


    code_melli = input("Enter code melli (10 digit number) : ")
    if len(code_melli) != 10 or check_duplicate_code_melli(code_melli) == False :
        print("Code Melli is a 10 Unique Characters code like : xxxxxxxxxx")
        input("Press any key ...")
        return 0
    else :
        student["code_melli"] = code_melli
    

    student_code = input("Enter student code (5 digit number) : ")
    if len(student_code) != 5 or check_duplicate_student_code(student_code) == False :
        print("Student Code is a 5 Unique Characters code like : xxxxx")
        input("Press any key ...")
        return 0
    else :
        student["student_code"] = student_code
        student["courses"] = list()
        student["grades"]= list()
    while True:    
        student["courses"].append(input("Enter course name : "))
        student["grades"].append(int(input("Enter grades : ")))
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
            print("student age : ")
            print("--------------------------------------")
            input()
            return True     
    print("Not Found !")    
    input()
    return False           





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
            print("student age : ")
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
            return True     
    print("Not Found !")    
    input()
def change_courses() :
    clear()
    student_code = input("Enter student code to find student : ")
    for student in active_students :
        if student ["student_code"] == student_code :
            input()
            //to do
            return True     
    print("Not Found !")    
    input()
def list_students() :
    pass
def save_students() :
    pass