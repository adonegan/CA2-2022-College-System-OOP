from user import User
from lecturer import Lecturer
from student import Student
import csv

# MODULE SUPERCLASS
class Module:

    # CLASS VARIABLES
    __mod_id = ""
    __mod_name = ""
    __mod_course_code = ""
    __mod_department = ""
    __mod_lecturer = ""
    __mod_student_class_list = []
    __mod_assessment_list = []

    # instance counter
    count_modules = 0

    # INITIALISER
    def __init__(self, module_id="", module_name="Unknown", course_code="", department="Computing", lecturer="", class_list=[], assessment_list=[]):
        try:
            self.setModuleID(module_id)
            self.setModuleName(module_name)
            self.setModuleCourseCode(course_code)
            self.setModuleDepartment(department)
            self.setModuleLecturer(lecturer)
            self.setModuleStudentClassList(class_list)
            self.setModuleAssessmentList(assessment_list)
        except Exception as e:
            raise Exception("The Module object has not been created.")
        # increment every time an object is created from this class
        Module.count_modules += 1

# call this method in main.py to see how many objects are created   
    @classmethod
    def count_all_modules(cls):
        return cls.count_modules

    # GETTERS
    # to call and return information
    def getModuleID(self):
        return self.__mod_id

    def getModuleName(self):
        return self.__mod_name

    def getModuleCourseCode(self):
        return self.__mod_course_code

    def getModuleDepartment(self):
        return self.__mod_department

    def getModuleLecturer(self):
        return self.__mod_lecturer.getName()
    
    def getModuleStudentClassList(self):
        return self.__mod_student_class_list
    
    def getModuleAssessmentList(self):
        return self.__mod_assessment_list

    # SETTERS
    # to change, update and user error check
    def setModuleID(self, module_id):
        if module_id == "":
            raise Exception("Module ID cannot be blank.")
        else:
            self.__mod_id = module_id

    def setModuleName(self, module_name):
        self.__mod_name = module_name

    def setModuleCourseCode(self, course_code):
        self.__mod_course_code = course_code

    def setModuleDepartment(self, department):
        if department in User.possible_departments:
            self.__mod_department = department
        else:
            raise Exception("{0} is not a valid department.".format(department))

    def setModuleLecturer(self, lecturer):
        if isinstance(lecturer, Lecturer):
            self.__mod_lecturer = lecturer
        else:
            raise Exception("{0} is not a valid instance.".format(lecturer))

    def setModuleStudentClassList(self, class_list):
        self.__mod_student_class_list = class_list

    def setModuleAssessmentList(self, assessment_list):
        self.__mod_assessment_list = assessment_list 

    def auto_add_classlist(self, filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader, None) 

            # works as well.
            class_list = []
            for row in reader:
                student = Student(email_address=row[0], name=row[1], student_number=row[2], programme_code=row[3], programme_year=row[4], student_type=row[5],list_of_grades=[])
                class_list.append(student)
            self.setModuleStudentClassList(class_list)

    def append_to_class_list(self,student):
        return self.__mod_student_class_list.append(student)
    
    # call this in main.py, with the argument from main.py as the parameter, so the result is assigned to the right module ID (self)
    def append_to_assessment_list(self,assessment):
        self.setModuleAssessmentList(assessment)

    # PRINT MODULE DETAILS
    def print_module_details(self):
        print("-"*40)
        print("\tFull Module Details")
        print("-"*40)
        print("Module ID: \t\t", self.getModuleID())
        print("Module Name: \t\t", self.getModuleName())
        print("Course Code: \t\t", self.getModuleCourseCode())
        print("Department:\t\t", self.getModuleDepartment())
        print("Lecturer:\t\t", self.getModuleLecturer())
        print()
        print("\tStudent Class List")
        print("\t------------------")
        # loop through class list
        for student in self.getModuleStudentClassList():
            student : Student
            student.print()
            print()
        # loop through assessment list
        print("\tModule Assessment List")
        print("\t-----------------------")
        for item in self.getModuleAssessmentList():
            item : Module
            print("Student Number: \t", item[0])
            print("Assessment Name: \t", item[1])
            print("Percentage: \t\t", item[2])
            print("Grade: \t\t\t", item[3])
            print()




