import pandas as pd

df = pd.read_csv("data/raw/students_ai_usage.csv")

df["ai_tools_used"] = df["ai_tools_used"].fillna("None")
df["purpose_of_ai"] = df["purpose_of_ai"].fillna("None")

# Improvement in grades after using AI
df["grade_improvement"] = df["grades_after_ai"] - df["grades_before_ai"]

# NEW CHANGE (v2)
df["study_hours_normalized"] = df["study_hours_per_day"] / df["study_hours_per_day"].max()

# Binary encoding for AI usage
df["uses_ai_binary"] = df["uses_ai"].map({"Yes": 1, "No": 0})

df.to_csv("data/processed/students_ai_usage.csv", index=False)

print("Dataset modified successfully")
