import pandas as pd

url = "https://raw.githubusercontent.com/datasets/harmonized-system/main/data/harmonized-system.csv"
df = pd.read_csv(url)

print("📋 Columns in CSV:", df.columns.tolist())

df.rename(columns={"hscode": "HS Code", "description": "Description"}, inplace=True)

df["Chapter"] = df["HS Code"].where(df["HS Code"].str.len() == 2)
df["Heading"] = df["HS Code"].where(df["HS Code"].str.len() == 4)
df["Subheading"] = df["HS Code"].where(df["HS Code"].str.len() == 6)

df = df[["Chapter", "Heading", "Subheading", "HS Code", "Description"]]

df.to_excel("HS_from_GitHub.xlsx", index=False)
print("✅ Exported: HS_from_GitHub.xlsx")
 