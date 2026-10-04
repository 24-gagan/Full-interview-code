import pandas as pd

# Read Excel
df = pd.read_excel("input.xlsx")

# Example: Add a new column
df["Status"] = "Processed"

# Example: Filter rows (optional)
filtered_df = df[df["Age"] > 25]  # suppose Age column exists

# Write modified data to new Excel
filtered_df.to_excel("processed_output.xlsx", index=False)

print("Processed data written to processed_output.xlsx")
