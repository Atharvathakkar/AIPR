import random

def chatbot():
    print("Welcome to College Selection Chatbot!")
    print("Please provide your marks for CET and HSC exams.")
    cet_marks = float(input("Enter your CET marks: "))
    hsc_marks = float(input("Enter your HSC marks: "))

    # College data with cutoff marks
    colleges = {
        "KKW College": {"cet_cutoff": random.uniform(50, 80), "hsc_cutoff": random.uniform(60, 90)},
        "College Set": {"cet_cutoff": random.uniform(60, 90), "hsc_cutoff": random.uniform(70, 95)},
        "Random College": {"cet_cutoff": random.uniform(40, 70), "hsc_cutoff": random.uniform(50, 80)}
    }

    # Add additional colleges and random amounts
    colleges["MET College"] = {"cet_cutoff": random.uniform(55, 85), "hsc_cutoff": random.uniform(65, 90)}
    colleges["NDVP College"] = {"cet_cutoff": random.uniform(45, 75), "hsc_cutoff": random.uniform(55, 85)}
    colleges["Add College"] = {"cet_cutoff": random.uniform(50, 80), "hsc_cutoff": random.uniform(60, 90)}

    # Find suitable colleges based on marks
    suitable_colleges = []
    for college, cutoffs in colleges.items():
        if cet_marks >= cutoffs["cet_cutoff"] and hsc_marks >= cutoffs["hsc_cutoff"]:
            suitable_colleges.append(college)

    # Provide college recommendations
    if suitable_colleges:
        print("Based on your marks, the following colleges are suitable for you:")
        for college in suitable_colleges:
            print(college)
    else:
        print("Sorry, based on your marks, there are no suitable colleges.")

    print("Thank you for using the College Selection Chatbot!")

# Run the chatbot
chatbot()
