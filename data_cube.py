import pandas as pd
# Load the student dataset
df = pd.read_csv("student_dropout_behavior_dataset.csv")
print("STUDENT DATASET")
print("----------------")
print("Total students:", len(df))
print("Total attributes:", len(df.columns))
# Convert required columns to numeric values
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["final_marks"] = pd.to_numeric(
    df["final_marks"], errors="coerce"
)
# Create age groups
df["age_group"] = pd.cut(
    df["age"],
    bins=[17, 20, 23, 26],
    labels=["18-20", "21-23", "24-25"],
    include_lowest=True
)
# Create a two-dimensional data cube
# Dimensions: Gender and Age Group
# Measures: Count and Average Final Marks
cube = pd.pivot_table(
    df,
    index=["gender", "age_group"],
    values="final_marks",
    aggfunc=["count", "mean"],
    observed=False
)
print("\nSTUDENT DATA CUBE")
print("-----------------")
print(cube)
# Correct the column names
cube.columns = ["count", "mean"]
# Convert index into regular columns
cube = cube.reset_index()
# Save the cleaned Data Cube
cube.to_csv("student_data_cube.csv", index=False)
print("\nData cube saved successfully!")
# 1. ROLL-UP
print("\n========== ROLL-UP ==========")

rollup = df.groupby("gender").agg(
    Total_Students=("final_marks", "count"),
    Average_Marks=("final_marks", "mean")
)

print(rollup)
# 2. DRILL-DOWN
print("\n========== DRILL-DOWN ==========")

drilldown = df.groupby(
    ["gender", "age_group"]
).agg(
    Total_Students=("final_marks", "count"),
    Average_Marks=("final_marks", "mean")
)

print(drilldown)
# 3. SLICE
print("\n========== SLICE ==========")

slice_data = df[df["gender"] == "Female"]

print(slice_data)

print("Total Female Students:", len(slice_data))
# 4. DICE
print("\n========== DICE ==========")

dice_data = df[
    (df["gender"] == "Female") &
    (df["age_group"] == "21-23")
]

print(dice_data)

print("Selected Students:", len(dice_data))
# 5. PIVOT
print("\n========== PIVOT ==========")

pivot = pd.pivot_table(
    df,
    index="gender",
    columns="age_group",
    values="final_marks",
    aggfunc="mean"
)

print(pivot)
