from user import User

# STUDENT SUBCLASS
class Student(User):

    # CLASS VARIABLES
    student_number = ""
    programme_code = ""
    programme_year = 0
    student_type = ""
    list_of_grades = []

    # instance counter
    count_students = 0

    # INITIALISER
    def __init__(self, email_address, name, student_number, programme_code, programme_year, student_type, list_of_grades):
        super().__init__(email_address, name)
        try:
            self.setStudentNumber(student_number)
            self.setProgrammeCode(programme_code)
            self.setProgrammeYear(programme_year)
            self.setStudentType(student_type)
            self.setListOfGrades(list_of_grades)
        except Exception as e:
            raise Exception("The Student object has not been created.")
        # increment every time an object is created from this class
        Student.count_students += 1

    # call this method in main.py to see how many objects are created
    @classmethod
    def count_student_users(cls):
        return cls.count_students
       
    # GETTERS
    # to call and return information
    def getStudentNumber(self):
        return self.student_number
    
    def getProgrammeCode(self):
        return self.programme_code
    
    def getProgrammeYear(self):
        return self.programme_year
    
    def getStudentType(self):
        return self.student_type
    
    def getListOfGrades(self):
        return self.list_of_grades

    # SETTERS
    # to change, update and user error check
    def setStudentNumber(self, student_number):
        student_number = str(student_number)
        if len(student_number) < 9:
            raise Exception("Student number is not long enough.")
        elif len(student_number) > 9:
            raise Exception("Student number is too long.")
        else:
            self.student_number = student_number

    def setProgrammeCode(self, programme_code):
        if programme_code == "":
            raise Exception("Programme code cannot be blank.")
        else:
            self.programme_code = programme_code

    def setProgrammeYear(self, programme_year):
        if programme_year == "1" or programme_year == "2" or programme_year == "3" or programme_year == "4" or programme_year == "5" or programme_year == "6":
            self.programme_year = programme_year
        else:
            raise Exception("{0} is not a valid year.".format(programme_year))
           
    def setStudentType(self, student_type):
        student_type_options = ["FT", "PT"]
        if student_type not in student_type_options:
            raise Exception("{0} is not a valid student type.".format(student_type))
        else:
            self.student_type = student_type

    def setListOfGrades(self, list_of_grades):
        self.list_of_grades = list_of_grades

    # PRINT STUDENT DETAILS
    def print(self):
        User.print(self)
        print("Student number: \t", self.getStudentNumber())
        print("Programme Code: \t", self.getProgrammeCode())
        print("Programme Year: \t", self.getProgrammeYear())
        print("Student Type:\t\t", self.getStudentType())
        print("List of Grades: \t", self.getListOfGrades())