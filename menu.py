
import student_operations as stoper

#================== MAIN =====================#

while True :
    stoper.clear()
    print("--------------------------------")
    print("Press 'A' to Add a student")
    print("Press 'F' to Find a student")
    print("Press 'D' to Delete a student")
    print("Press 'C' to Change Courses")
    print("Press 'L' to List students")
    print("Press 'S' to Save students")
    print("Press 'Q' to Quit Application")
    print("--------------------------------")
    choise = input("\nEnter your choise : ").upper()
    if choise == "A" :
        stoper.add_student()
    elif choise == "F" :
        stoper.find_student()
    elif choise == "D" :
        stoper.delete_student()
    elif choise == "C" :
        stoper.change_courses()
    elif choise == "L" :
        stoper.list_students()
    elif choise == "S" :
        stoper.save_students()
    elif choise == "Q" :
        exit_check = input("Do you want save books ? (y/n) : ").upper()
        if exit_check == "Y" :
            stoper.save_students()
            break
        else :
            break
    else :
        input("Wrong Choice ! Try Again ...")