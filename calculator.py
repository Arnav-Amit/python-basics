# Student Grade Calculator 

results = []   # List to store student results

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+", "Outstanding performance!"
    elif percentage >= 80:
        return "A", "Excellent work!"
    elif percentage >= 70:
        return "B", "Good job, keep improving!"
    elif percentage >= 60:
        return "C", "Satisfactory, needs more effort."
    elif percentage >= 50:
        return "D", "Just passed, needs improvement."
    else:
        return "F", "Failed — work harder next time."

# --- Input Section ---
name = input("Enter student name: ")

# You can change or add more subjects
subjects = ["Math", "Science", "English"]

marks = []
for sub in subjects:
    score = float(input(f"Enter marks for {sub}: "))
    marks.append(score)

# --- Calculation ---
total = sum(marks)
percentage = total / len(marks)

grade, comment = calculate_grade(percentage)

# --- Store result in list ---
student_data = {
    "name": name,
    "marks": marks,
    "total": total,
    "percentage": percentage,
    "grade": grade,
    "comment": comment
}

results.append(student_data)

# --- Output ---
print("\n--- Student Report ---")
print("Name:", name)
for i, sub in enumerate(subjects):
    print(f"{sub}: {marks[i]}")

print("Total:", total)
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
print("Comment:", comment)

print("\nStored Results:", results)
