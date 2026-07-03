student_grades = {}

while True:
    print("\n--- Student Grades ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    # 1. Add a new student and grade
    if choice == '1':
        name = input("Enter student name: ").strip()
        # check if student already exists using 'if'
        if name in student_grades:
            print(f"'{name}' already exists! Use the update option instead.")
        else:
            grade = input(f"Enter grade for {name}: ")
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")
            
    # 2. Update an existing student's grade
    elif choice == '2':
        name = input("Enter the student's name to update: ").strip()
        # verify the student exists before updating
        if name in student_grades:
            new_grade = input(f"Enter new grade for {name}: ")
            student_grades[name] = new_grade
            print(f"Updated {name}'s grade to {new_grade}.")
        else:
            print(f"Student '{name}' not found.")
            
    # 3. Print all student grades
    elif choice == '3':
        if len(student_grades) == 0:
            print("No student grades recorded yet.")
        else:
            print("\n--- Current Student Grades ---")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")
                
    # 4. Exit the loop
    elif choice == '4':
        print("Exiting program.!")
        break
        
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")