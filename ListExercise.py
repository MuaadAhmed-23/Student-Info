students = [("Khalil", "Aalab", 9),
            ("Muaad", "Ahmed", 9),
            ("Jalil", "Aalab", 9)]
inp = input("Please Enter firstName: ")
def studentInfo():
    for x in range(len(students)):
        if inp == students[x][0] or inp == students[x][1]:
            print(students[x])
studentInfo()