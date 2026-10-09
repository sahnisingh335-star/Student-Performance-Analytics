
import pandas as pd
import numpy as np

from functions import (
    calculate_total,
    calculate_average,
    calculate_grade,
    calculate_result
)

# Step 1: Read the dataset
df = pd.read_csv("data/students.csv")

print("\n===== STUDENT DATA =====")
print(df.head())

# Step 2: Basic dataset information
print("\n===== DATASET INFORMATION =====")
print("Total rows and columns:", df.shape)
print("Column names:", df.columns.tolist())
df.info()

# Step 3: Define subjects
subjects = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "English",
    "Hindi"
]

# Step 4: Calculate total and average marks
df["Total"] = df[subjects].apply(
    lambda row: calculate_total(row.tolist()),
    axis=1
)

df["Average"] = df[subjects].apply(
    lambda row: calculate_average(row.tolist()),
    axis=1
).round(2)

# Step 5: Calculate grades and results
df["Grade"] = df["Average"].apply(calculate_grade)
df["Result"] = df["Average"].apply(calculate_result)

print("\n===== STUDENT PERFORMANCE =====")
print(
    df[
        ["Student_ID", "Name", "Total",
         "Average", "Grade", "Result"]
    ].to_string(index=False)
)

# Step 6: Overall performance analysis
print("\n===== OVERALL PERFORMANCE =====")
print("Total Students:", len(df))
print("Class Average:", round(np.mean(df["Average"]), 2))
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())

# Step 7: Pass and fail analysis
print("\n===== PASS AND FAIL ANALYSIS =====")
print(df["Result"].value_counts())

# Step 8: Subject-wise performance
print("\n===== SUBJECT-WISE AVERAGE =====")
subject_averages = df[subjects].mean().round(2)
print(subject_averages)

print(
    "Best Performing Subject:",
    subject_averages.idxmax()
)

print(
    "Lowest Performing Subject:",
    subject_averages.idxmin()
)

# Step 9: Top 5 performers
print("\n===== TOP 5 STUDENTS =====")
top_students = df.sort_values(
    by="Average",
    ascending=False
).head(5)

print(
    top_students[
        ["Student_ID", "Name", "Average", "Grade"]
    ].to_string(index=False)
)

# Step 10: Subject averages using a loop
print("\n===== SUBJECT AVERAGES USING LOOP =====")

for subject in subjects:
    average_marks = df[subject].mean()
    print(f"{subject}: {average_marks:.2f}")

print("\n===== ANALYSIS COMPLETED =====")
