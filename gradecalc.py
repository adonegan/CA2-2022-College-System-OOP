# STATIC CLASS
class GradeCalculator:

    @staticmethod
    # when called, take in the percentage, if it's within a specific range (noted below) set the corresponding letter grade and output it
    def percentageToGrade(percentage):
        percentage = int(percentage)
        if percentage in range(80,100):
            return "A"
        elif percentage in range(70,80):
            return "B+"
        elif percentage in range(60,70):
            return "B"
        elif percentage in range(55,60):
            return "B-"
        elif percentage in range(50,55):
            return "C+"
        elif percentage in range(40,50):
            return "C"
        elif percentage in range(35,40):
            return "D"
        elif percentage in range(0,35):
            return "F"
        else:
            return " -> {0} is not a valid percentage.".format(percentage)