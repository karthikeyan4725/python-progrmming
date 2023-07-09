
class NegativeAgeException(Exception):
    pass

def generate_student_details():
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    if age < 0:
        raise NegativeAgeException("Age cannot be negative")

    marks = []
    for i in range(6):
        subject = input("Enter marks for subject {}: ".format(i+1))
        marks.append(subject)

    student_details = {
        "Name": name,
        "Age": age,
        "Marks": marks
    }

    return student_details


try:
    student = generate_student_details()
    print("Student details:", student)
except NegativeAgeException as e:
    print("Error:", str(e))
