import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("jobs.csv")


df["Region"] = df["Location"].str.split(", ").str[-1]
print(df["Region"].value_counts())

python_jobs = df[df["Title"].str.contains("python", case=False)]
print(python_jobs["Region"].value_counts())

print(df["Region"].value_counts(normalize=True))
print(python_jobs["Region"].value_counts(normalize=True))

print(df["Title"].value_counts().head(5))

df["Region"].value_counts().plot(kind="bar")
plt.title("Listings per region")
plt.show()

df.to_csv("jobs_with_region.csv", index=False, encoding="utf-8-sig")
df["Region"].value_counts().to_csv("region_counts.csv", encoding="utf-8-sig")

# print(df.head())
# print(df.shape)
# print(df.columns)

# print(df["Company"])
# print(df["Location"].value_counts())

# print(df["Title"].str.contains("python", case=False).sum())

# python_jobs = df[df["Title"].str.contains("python", case=False)]
# print(python_jobs)
# print(python_jobs.shape)