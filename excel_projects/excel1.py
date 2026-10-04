import pandas as pd

input_file = "input.xlsx"
df = pd.read_excel(input_file)
print("data read from excel")
print(df)
output_file = "output.xlsx"
df.to_excel(output_file, index=False)
print("Data written to excel successfully")
