import pandas as pd

# Load the original student dataset
df = pd.read_csv("student_dropout_behavior_dataset.csv")

# Create a new binary dataset
binary_df = pd.DataFrame()

# Gender
binary_df["Female"] = (
    df["gender"].str.lower() == "female"
).astype(int)

binary_df["Male"] = (
    df["gender"].str.lower() == "male"
).astype(int)

# Age
binary_df["Age_Above_21"] = (
    df["age"] > 21
).astype(int)

# Quiz marks: scale is 0–10
binary_df["Quiz1_High"] = (
    df["quiz1_marks"] >= 7
).astype(int)

binary_df["Quiz2_High"] = (
    df["quiz2_marks"] >= 6
).astype(int)

binary_df["Quiz3_High"] = (
    df["quiz3_marks"] >= 6
).astype(int)

# Examination marks: use the actual scale in the dataset
binary_df["Midterm_High"] = (
    df["midterm_marks"] >= df["midterm_marks"].median()
).astype(int)

binary_df["Final_High"] = (
    df["final_marks"] >= df["final_marks"].median()
).astype(int)

# Previous GPA: scale is approximately 0–4
binary_df["GPA_High"] = (
    df["previous_gpa"] >= 3
).astype(int)

# Lecture attendance
binary_df["Lecture_Attendance_High"] = (
    df["lectures_attended"] /
    df["total_lectures"].replace(0, pd.NA) >= 0.75
).fillna(False).astype(int)

# Remove attributes that have no variation
binary_df = binary_df.loc[
    :, binary_df.nunique() > 1
]

# Save the binary dataset
binary_df.to_csv("student_binary_data.csv", index=False)

print("Binary dataset created successfully!")
print("Total students:", len(binary_df))
print("Total binary attributes:", len(binary_df.columns))

print("\nNumber of students with value 1:")
print(binary_df.sum())

print("\nNumber of distinct values per attribute:")
print(binary_df.nunique())
