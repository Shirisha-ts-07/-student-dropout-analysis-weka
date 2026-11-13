import pandas as pd

# Load the original student dataset
df = pd.read_csv("student_dropout_behavior_dataset.csv")

# Create a binary dataset
binary_df = pd.DataFrame()

# Gender
binary_df["Female"] = (df["gender"].str.lower() == "female").astype(int)
binary_df["Male"] = (df["gender"].str.lower() == "male").astype(int)

# Age
binary_df["Age_Above_21"] = (df["age"] > 21).astype(int)

# Quiz marks
binary_df["Quiz1_High"] = (df["quiz1_marks"] >= 50).astype(int)
binary_df["Quiz2_High"] = (df["quiz2_marks"] >= 50).astype(int)
binary_df["Quiz3_High"] = (df["quiz3_marks"] >= 50).astype(int)

# Exam marks
binary_df["Midterm_High"] = (df["midterm_marks"] >= 50).astype(int)
binary_df["Final_High"] = (df["final_marks"] >= 50).astype(int)

# Previous GPA
binary_df["GPA_High"] = (df["previous_gpa"] >= 7).astype(int)

# Attendance
binary_df["Lecture_Attendance_High"] = (
    df["lectures_attended"] / df["total_lectures"] >= 0.75
).astype(int)

# Assignment completion
binary_df["Assignments_Completed"] = (
    df["assignments_submitted"] >= df["total_assignments"]
).astype(int)

# Save the binary dataset
binary_df.to_csv("student_binary_data.csv", index=False)

print("Binary dataset created successfully!")
print("Total students:", len(binary_df))
print("Total binary attributes:", len(binary_df.columns))
print("\nFirst five rows:")
print(binary_df.head())

