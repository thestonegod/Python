print("University Classroom Attendance Tracker")
# Name of students
students = ["EL-SHADDAI", "MAABENA", "NATTY", "ADWOA KOSUA", "AKWASI SAMAN", "ATTAA ADWOA", "SERWAA AMPAAFO"]
days = ("Monday", "Wednesday", "Friday", "Saturday")

# Asks user to enter day plus no case sensitive issues 
day = input("Enter a day: ").strip().title()

# Checks if the day the user entered is in the tuple
if day in days:
    print("Class is in session today.")
    while True:
        try:
            present_count = int(input("How many students are present? "))
            if 0 <= present_count <= len(students):
                break
            else:
                print("Invalid number of students. Please enter a number between 0 and", len(students))
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Creates an empty list for students who are present
    present_students = []

    #Loop to collect present students data
    for i in range(present_count):
        while True:
            name = input(f"Enter student name {i+1}: ").strip().upper()
            if name in students and name not in present_students:
                present_students.append(name)
                break
            elif name in present_students:
                print("Student already marked present. Please enter a different student.")
            else:
                print("Invalid student name. Please enter a valid student name.")

    absent_students = [s for s in students if s not in present_students]
    print("Present students:", present_students)
    print("Total present:", len(present_students))
    print("Absent students:", absent_students)
    print("Total absent students:", len(absent_students))
else:
    print("No class today.")