import csv
import time
from user import User
from student import Student
from lecturer import Lecturer
from module import Module
from gradecalc import GradeCalculator


# MAIN PROGRAM
menuOption = 0

# open and read modules file
with open("csv/modules.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader, None) 

    # for every row in the csv, make it a Module object and append it to moduleList list
    moduleList = []
    for row in csv_reader:
        module = Module(module_id=row[0], module_name=row[1], course_code=row[2], department=row[3], lecturer=Lecturer(email_address=row[4],name=row[5],staff_id=row[6],speciality=row[7],qualification=row[8]),class_list=[])
        moduleList.append(module)

while menuOption >= 0 and menuOption < 7:

    # DISPLAY MAIN MENU
    print()
    print(" -------------------------- ")
    print("|       Module Menu        |")
    print("|--------------------------|")
    print("|  1) Add Module           |")
    print("|  2) Add Students         |")
    print("|  3) Add Student Grades   |")
    print("|  4) Display All Modules  |")
    print("|  5) Display All Students |")
    print("|  6) Display All Grades   |")
    print("|  7) Exit                 |")
    print(" -------------------------- ")

    # get user menu choice
    menuOption = int(input("\nPlease enter menu option: "))

    if menuOption == 1:

        # get details from user
        module_id = input("Enter Module ID: ")
        module_name =input("Enter Module Name: ")
        course_code =input("Enter Course Code: ")
        department = input("Enter Department: ")
        lecturer_email = input("Enter Lecturer Email: ")
        lecturer_name = input("Enter Lecturer Name: ")
        lecturer_staff_id = input("Enter Staff ID: ")
        lecturer_speciality = input("Enter Lecturer Speciality: ")
        lecturer_qualification = input("Enter Lecturer Qualification: ")
        class_list = []

        # take user data, create a new list called newModuleItem
        newModuleItem = [module_id,module_name,course_code,department,Lecturer(email_address=lecturer_email,name=lecturer_name,staff_id=lecturer_staff_id,speciality=lecturer_speciality,qualification=lecturer_qualification),class_list]

        # for every module in moduleList, declare it as a Module object
        for module in moduleList:
            module : Module
            # if module in list is equal to the module_id provided by the user, 
            # don't add it to moduleList as it already exists
            if module.getModuleID() == newModuleItem[0]:
                print("-> Module ID", newModuleItem[0],"has not been added as it already exists.")
                break
        else:
            # otherwise, it doesn't exist, so append it to the moduleList
            newModuleItem = Module(module_id=module_id,module_name=module_name,course_code=course_code,department=department,lecturer=Lecturer(email_address=lecturer_email,name=lecturer_name,staff_id=lecturer_staff_id,speciality=lecturer_speciality,qualification=lecturer_qualification), class_list=class_list)
            moduleList.append(newModuleItem)
            print("-> Added... module ID", module_id)

        # wait 3 seconds before showing the main menu
        time.sleep(3)

    elif menuOption == 2:

        # get user to specify which module they want to act on
        module_id = input("What module would you like to add students to? ")

        # only proceed if user module_id matches what we have in our system
        for module in moduleList:
            module : Module
            if module.getModuleID() == module_id:
                add_student_choice = input("Add student(s) by File or by Manual Input? ")

                # if user wants to upload students by file
                if add_student_choice == "File":
                    add_student_file = input("What is the CSV file called? ")
                    add_student_file = "csv/" + add_student_file

                    module.auto_add_classlist(add_student_file)
                    print("-> Added to class list.")

                # if user wants to manually type in student information
                elif add_student_choice == "Manual Input":
                    # take user input for all required information    
                    email_address = input("Enter student email address: ")
                    name = input("Enter student name: ")
                    student_number = int(input("Enter student number: "))
                    programme_code = input("Enter programme code: ")
                    programme_year = input("Enter programme year: ")
                    student_type = input("Enter student type (FT or PT): ")

                    # store input in a student object
                    a_student = Student(email_address=email_address, name=name, student_number=student_number, programme_code=programme_code, programme_year=programme_year, student_type=student_type,list_of_grades="")

                    # call method that appends the object to the module
                    module.append_to_class_list(a_student)
                    print("-> Added to class list.")

                # information to the user about how many students objects were created
                print("Student users:", Student.count_student_users())
                time.sleep(3)
                break
        else:
            # if user enters a module_id that doesn't fit our requirements, send them back to the main menu
            print("Module ID {0} is not valid. \nBack to Main Menu...\n".format(module_id))
            time.sleep(3)

    elif menuOption == 3:
        
        # get user to specify which module to act on
        module_id = input("Enter module ID to add assessment list: ")
        for module in moduleList:
            module : Module
            if module.getModuleID() == module_id:
                # ask user how many students' assessments they want to input to the system
                students = int(input("Enter the amount of students you're inputting for: "))

                # create empty list
                assessments = []
                # loop through the amount of students the user wants to input for
                for student in range(students):
                    # get student number, assessment name, percent achieved information, then convert the percent into a letter grade
                    student_number = input("Enter student number: ")
                    assessment_name = input("Enter assessment name: ")
                    percent_achieved = input("Enter percent achieved: ")
                    convert_to_grade = GradeCalculator.percentageToGrade(percent_achieved)
                    print()

                    # for every iteration, put the student information into it's own one dimensional list
                    individual_assessment = [student_number,assessment_name,percent_achieved,convert_to_grade]
                    # append that individual assessment to the assessments list we initialised earlier
                    assessments.append(individual_assessment)

                # then call this append method to append the assessement to this specific module
                module.append_to_assessment_list(assessments)
                print("-> Added assessments.")

    elif menuOption == 4:

        # iterate through all modules, printing their details
        for mod in moduleList:
            mod : Module
            mod.print_module_details()
            print()

        # department variables to increment by how many times they appear in the moduleList
        marketing = 0
        computing = 0
        science = 0
        business = 0
        art = 0

        # loop through all modules, use the department getter to get the department name, if it matches the hardcoded string, update department variable counters above
        for module in moduleList:
            module: Module
            if module.getModuleDepartment() == "Marketing":
                marketing += 1
            elif module.getModuleDepartment() == "Computing":
                computing += 1
            elif module.getModuleDepartment() == "Science":
                science += 1
            elif module.getModuleDepartment() == "Business":
                business += 1
            elif module.getModuleDepartment() == "Art":
                art += 1

        # output results to get birdseye view of system
        print("Total number of modules in system: ", Module.count_all_modules())
        print("Total number of students in system: ", Student.count_student_users())
        print("Total number of modules in the system, by department:\n")
        print("\t-> Marketing:\t {0}\n\t-> Computing:\t {1}\n\t-> Science:\t {2}\n\t-> Business:\t {3}\n\t-> Art:\t\t {4}".format(marketing, computing, science, business, art))
        
        # wait three seconds before showing main menu
        time.sleep(3)

    elif menuOption == 5:
 
        # get user to specify which module they want information on
        module_id = input("Enter module_id to check student list: ")

        for module in moduleList:
            if module.getModuleID() == module_id:
                # if the module has no students, output that information
                if len(module.getModuleStudentClassList()) == 0:
                    print("No students listed.")
                else:
                    # otherwise, loop through the students in the student list of that specific module and output the information to the user
                    for student in module.getModuleStudentClassList():
                        student : Student
                        student.print()
                        print()
        time.sleep(3)

    elif menuOption == 6:

        # ask user to specify the module containing the student grades they want to see
        module_id = input("Enter module ID to see students grades: ")
        for module in moduleList:
            module : Module
            if module.getModuleID() == module_id:
                # if the module has no assessments, output this information to the user
                if len(module.getModuleAssessmentList()) == 0:
                    print("No assessments listed.")
                    break
                else:
                    # otherwise, loop through all the student assessments pertaining to the specific module the user specified
                    print("----------------------------")
                    print("{0} Assessment List Details".format(module.getModuleID()))
                    print("----------------------------")
                    for item in module.getModuleAssessmentList():
                        print("Student Number: \t", item[0])
                        print("Assessment Name: \t", item[1])
                        print("Percentage: \t\t", item[2])
                        print("Grade: \t\t\t", item[3])
                        print()

            # grade all letter grades and store in new variable
            grades = [row[3] for row in module.getModuleAssessmentList()]

            # initialise new variables for letter grades, so we can count how many there are
            grade_A = 0
            grade_Bplus = 0
            grade_B = 0
            grade_Bminus = 0
            grade_Cplus = 0
            grade_C = 0
            grade_D = 0
            grade_F = 0

            total = len(grades)

            # loop through all grades in the grades list, incrementing the counter variables by 1 every time there is an instance of the corresponding letter
            for grade in grades:
                if grade == "A":
                    grade_A += 1
                elif grade == "B+":
                    grade_Bplus += 1
                elif grade == "B":
                    grade_B += 1
                elif grade == "B-":
                    grade_Bminus += 1
                elif grade == "C+":
                    grade_Cplus += 1
                elif grade == "C":
                    grade_C += 1
                elif grade == "D":
                    grade_D += 1
                elif grade == "F":
                    grade_F += 1

        # output grade information
        print("-----------------------------")
        print("\tList of grades")
        print("-----------------------------")
        print("| Total       | {0}           |".format(total)) 
        print("| A           | {0}           |".format(grade_A)) 
        print("| B+          | {0}           |".format(grade_Bplus)) 
        print("| B           | {0}           |".format(grade_B)) 
        print("| B-          | {0}           |".format(grade_Bminus)) 
        print("| C+          | {0}           |".format(grade_Cplus)) 
        print("| C           | {0}           |".format(grade_C)) 
        print("| D           | {0}           |".format(grade_D)) 
        print("| F           | {0}           |".format(grade_F)) 
        print("-----------------------------")
        
        # wait three seconds before showing the main menu again
        time.sleep(3)

    elif menuOption == 7:
        # the user wants to exit, show them this
        print("-> Exiting...")
    else:
        # if user enters any other number than 1-7, break out of the program
        print("-> {0} is not a valid menu option. Goodbye.".format(menuOption))