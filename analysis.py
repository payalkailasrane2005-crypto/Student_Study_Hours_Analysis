import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Student CSV Data
data = pd.read_csv("student_data.csv")

# Display Student Data
print("\nSTUDENT DATA")
print(data)

# Basic Analysis
print("\nBASIC ANALYSIS")

print("Total Students:", len(data))
print("Average Study Hours:", data["Study_Hours"].mean())
print("Average Marks:", data["Marks"].mean())
print("Maximum Study Hours:", data["Study_Hours"].max())
print("Minimum Study Hours:", data["Study_Hours"].min())

# Subject-wise Analysis
print("\nSUBJECT-WISE ANALYSIS")

subject_analysis = data.groupby("Subject").agg({
    "Study_Hours": "mean",
    "Marks": "mean"
})

print(subject_analysis)

# Chart 1: Subject-wise Marks
plt.figure(figsize=(8, 5))
plt.bar(subject_analysis.index, subject_analysis["Marks"])
plt.title("Subject-Wise Marks Analysis")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# Chart 2: Study Hours vs Marks
plt.figure(figsize=(8, 5))
plt.scatter(data["Study_Hours"], data["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.show()

# Chart 3: Study Hours Trend
plt.figure(figsize=(8, 5))
plt.plot(data["Study_Hours"], data["Marks"], marker="o")
plt.title("Study Hours Trend")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nSTUDENT STUDY HOURS ANALYSIS COMPLETED!")