lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

#Function to find the average grade for a set of numbers
def average(numbers):
    total = float(sum(numbers))
    return total/len(numbers)

#Function to get the average hw, quiz, and test scores for a given student, and convert that into a total weighted number grade for that student
def get_average(student):
    homework = average(student["homework"]) * 0.1
    quizzes = average(student["quizzes"]) * 0.3
    tests = average(student["tests"]) * 0.6
    return float(homework + quizzes + tests)

#Function to convert a student's weighted number grade into a letter grade
def get_letter_grade(score):
    if score >= 90:
        print "A"
        return "A"
    elif score >= 80:
        print "B"
        return "B"
    elif score >= 70:
        print "C"
        return "C"
    elif score >= 60:
        print "D"
        return "D"
    else:
        print "F"
        return "F"
    print(score)

#Function to get the average grade of all students in the class
def get_class_average(students):
    results = []
    for student in students:
        avg = get_average(student)
        results.append(avg)
    print average(results)
    return average(results)

#Calling the functions with the students in our class to get a total average letter grade.
students = [lloyd, alice, tyler]
class_average = get_class_average(students)
get_letter_grade(class_average)
