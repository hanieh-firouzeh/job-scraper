import pandas as pd

df = pd.read_csv("jobs.csv")


df["Region"] = df["Location"].str.split(", ").str[-1]
print(df["Region"].value_counts())

python_jobs = df[df["Title"].str.contains("python", case=False)]
print(python_jobs["Region"].value_counts())

print(df["Region"].value_counts(normalize=True))
print(python_jobs["Region"].value_counts(normalize=True))

print(df["Title"].value_counts().head(5))

# print(df.head())
# print(df.shape)
# print(df.columns)

# print(df["Company"])
# print(df["Location"].value_counts())

# print(df["Title"].str.contains("python", case=False).sum())

# python_jobs = df[df["Title"].str.contains("python", case=False)]
# print(python_jobs)
# print(python_jobs.shape)