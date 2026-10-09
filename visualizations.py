
import os
import matplotlib.pyplot as plt
import pandas as pd

# Create screenshots folder if it does not exist
os.makedirs("screenshots", exist_ok=True)

# Load student dataset
df = pd.read_csv("data/students.csv")

subjects = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "English",
    "Hindi"
]

# Calculate each student's average marks
df["Average"] = df[subjects].mean(axis=1)

# Chart 1: Subject-wise Average Marks
subject_averages = df[subjects].mean()

plt.figure(figsize=(9, 5))
subject_averages.plot(kind="bar")
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("screenshots/subject_averages.png", dpi=300)
plt.close()

# Chart 2: Top 5 Students
top_students = df.nlargest(5, "Average").sort_values("Average")

plt.figure(figsize=(9, 5))
plt.barh(top_students["Name"], top_students["Average"])
plt.title("Top 5 Student Performers")
plt.xlabel("Average Marks")
plt.ylabel("Student")
plt.xlim(0, 100)

for index, value in enumerate(top_students["Average"]):
    plt.text(value + 0.5, index, f"{value:.1f}", va="center")

plt.tight_layout()
plt.savefig("screenshots/top_5_students.png", dpi=300)
plt.close()

# Chart 3: Pass vs Fail
# Pass is based on average marks >= 40, matching functions.py
pass_count = (df["Average"] >= 40).sum()
fail_count = (df["Average"] < 40).sum()

plt.figure(figsize=(6, 6))
plt.pie(
    [pass_count, fail_count],
    labels=["Pass", "Fail"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Student Pass vs Fail")
plt.tight_layout()
plt.savefig("screenshots/pass_fail.png", dpi=300)
plt.close()

# Chart 4: Distribution of Average Marks
plt.figure(figsize=(9, 5))
plt.hist(df["Average"], bins=8, edgecolor="black")
plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("screenshots/marks_distribution.png", dpi=300)
plt.close()

print("All 4 charts created successfully!")
print("Check the screenshots folder.")
