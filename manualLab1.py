import pandas as pd

df_can = pd.read_excel(
    "./Canada.xlsx",
    sheet_name="Canada by Citizenship",
    skiprows=range(20),
    skipfooter=2,
)

print("Data read into a pandas dataframe!")

print(df_can.head())
print(df_can.columns)
print(df_can.index)
print(df_can.columns.tolist())
print(df_can.tolist()columns)
print(df_can.index)
