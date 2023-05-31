def get_college(marks):
    # Define college options and their respective criteria
    colleges = {
        "College A": {"CET": 90, "HSC": 95},
        "College B": {"CET": 85, "HSC": 90},
        "College C": {"CET": 80, "HSC": 85},
        "College D": {"CET": 75, "HSC": 80},
        "College E": {"CET": 70, "HSC": 75}
    }

    eligible_colleges = []

    # Check the eligibility of each college based on marks
    for college, criteria in colleges.items():
        if marks["CET"] >= criteria["CET"] and marks["HSC"] >= criteria["HSC"]:
            eligible_colleges.append(college)

    return eligible_colleges


def college_selection_chatbot():
    print("Welcome to the College Selection Chatbot!")

    while True:
        print("\nPlease enter your marks (enter 'q' to quit):")
        cet_marks = input("Enter your CET marks: ")
        if cet_marks == 'q':
            break
        hsc_marks = input("Enter your HSC marks: ")
        if hsc_marks == 'q':
            break

        try:
            cet_marks = float(cet_marks)
            hsc_marks = float(hsc_marks)
        except ValueError:
            print("Invalid input. Please enter a valid numerical value for marks.")
            continue

        # Create a dictionary of marks
        student_marks = {"CET": cet_marks, "HSC": hsc_marks}

        # Get eligible colleges based on the student's marks
        eligible_colleges = get_college(student_marks)

        # Display the eligible colleges to the student
        if eligible_colleges:
            print("\nCongratulations! You are eligible for the following colleges:")
            for college in eligible_colleges:
                print(college)
        else:
            print("\nSorry, based on your marks you are not eligible for any colleges.")

    print("\nThank you for using the College Selection Chatbot!")


# Run the chatbot
college_selection_chatbot()
