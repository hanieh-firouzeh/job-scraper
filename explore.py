import pandas as pd

df = pd.read_csv("jobs.csv")

print(df.head())
print(df.shape)
print(df.columns)

print(df["Company"])
print(df["Location"].value_counts())

print(df["Title"].str.contains("python", case=False).sum())

python_jobs = df[df["Title"].str.contains("python", case=False)]
print(python_jobs)
print(python_jobs.shape)