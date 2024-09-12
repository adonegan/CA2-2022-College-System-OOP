from user import User

# LECTURER SUBCLASS
class Lecturer(User):

    # CLASS VARIABLES
    staff_id = ""
    speciality = ""
    qualification = ""

    # INITIALISER
    def __init__(self, email_address, name, staff_id, speciality, qualification):
        super().__init__(email_address, name)
        try:
            self.setStaffID(staff_id)
            self.setSpeciality(speciality)
            self.setQualifications(qualification)
        except Exception as e:
            raise Exception("The Lecturer object has not been created.")

    # GETTERS
    # to call and return information
    def getStaffID(self):
        return self.staff_id
    
    def getSpeciality(self):
        return self.speciality
    
    def getQualifications(self):
        return self.qualification
    
    # SETTERS
    # to change, update and user error check
    def setStaffID(self, staff_id):
        staff_id = str(staff_id)
        if len(staff_id) > 6:
            raise Exception("Staff ID is not long enough.")
        elif len(staff_id) > 6:
            raise Exception("Staff ID is too long.")
        else:
            self.staff_id = staff_id

    def setSpeciality(self, speciality):
        if speciality == "":
            raise Exception("Speciality field cannot be blank.")
        else:
            self.speciality = speciality

    def setQualifications(self, qualification):
        if qualification == "BA" or qualification == "BSC" or qualification == "MA" or qualification == "MSC" or qualification == "PHD":
            self.qualification = qualification
        else:
            raise Exception("{0} is not a valid qualification.".format(qualification))

    # PRINT LECTURER DETAILS
    def print(self):
        User.print(self)
        print("Lecturer ID: \t\t", self.staff_id)
        print("Speciality: \t\t", self.speciality)
        print("Qualification: \t\t", self.qualification)
