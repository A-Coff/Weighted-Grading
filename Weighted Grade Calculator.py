# Alex Coffman 13/JUL/23
# CMIS 102/6980 Week 5 Assignment
# This program computes the weighted average grades for a list of students and determines the student with the highest average

def weighted_average_grade(studentName):
    print(f"\nEnter grades for {studentName}") # used the f-string to better format the print string when calling the variable studentName
    while True:
        try: # prompts the user to enter the three grades for each student by name. Added while true statement to make sure the inputs are valid, will loop the request until the input is within parameters below
            discussionGrade = eval(input("Discussion grade: "))
            quizGrade = eval(input("Enter quiz grade: "))
            programAssignment_grade = eval(input("Enter programming assignment grade: "))
            if 0 <= discussionGrade <= 100 and 0 <= quizGrade <= 100 and 0 <= programAssignment_grade <= 100:
                break
            else:
                print("Invalid value. Grades should be between 0 and 100.")
        # required for the try statement 
        except ValueError:
            print("Invalid value. Grades should be in numeric and between 0 and 100") 
       # actual formual to calaculate the weighted averagae for each students grades     
    wtAvgGrade = round(discussionGrade * 0.15 + quizGrade * 0.35 + programAssignment_grade * 0.5, 2) # rounded the wtAvgGrade to two decimal places
    return wtAvgGrade

def main():
    students = ["George", "Mikey", "Sam", "Linda"]
    highestGrade = 0
    highestGrade_Student = ""
    # iterative student list
    for student in students: 
        averageGrade = weighted_average_grade(student) # calls the function for each student 
        # compares the students average grade with the highest grade which is pulled from the function
        if averageGrade > highestGrade:
            highestGrade = averageGrade
            highestGrade_Student = student
        elif averageGrade == highestGrade and highestGrade_Student == '': # this checks to see if more than one student's highestGRade and highestGrade_student variables match, if so it will use the first student as the one with highestGrade
            highestGrade_Student = student
     # Prints the name of the student with the highest grade       
    print(f"\nThe student with the highest grade is {highestGrade_Student} with a {highestGrade}.") # used the f-string to better format the print string when calling the two variables (highestGrade_student and highestGrade)

main()