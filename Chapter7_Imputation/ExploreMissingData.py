import pandas as pd

df = pd.read_csv("alkane_dataset.csv")
print(df.head())
print("\nMissing values by column:")
print(df.isnull().sum())
print("\nPercentage of missing data:")
print((df.isnull().sum() / len(df) * 100).round(2))
clean_df = df.dropna()

print("\nOriginal molecules:", len(df))
print("Molecules remaining:", len(clean_df))
print("Molecules removed:", len(df) - len(clean_df))
print("Percentage removed:", round((1 - len(clean_df) / len(df)) * 100, 2))
print("\nAverage carbon count before deletion:")
print(df["carbons"].mean())

print("\nAverage carbon count after deletion:")
print(clean_df["carbons"].mean())
import matplotlib.pyplot as plt

plt.hist(df["carbons"], bins=12, alpha=0.5, label="Original")
plt.hist(clean_df["carbons"], bins=12, alpha=0.5, label="After deletion")

plt.xlabel("Number of Carbon Atoms")
plt.ylabel("Number of Molecules")
plt.title("Carbon Distribution Before and After Deletion")
plt.legend()
plt.show()
plt.hist(df["carbons"], bins=12, density=True,
         alpha=0.5, label="Original")

plt.hist(clean_df["carbons"], bins=12, density=True,
         alpha=0.5, label="After deletion")

plt.xlabel("Number of Carbon Atoms")
plt.ylabel("Relative Frequency")
plt.title("Carbon Distribution: Relative Frequency")
plt.legend()
plt.show()
print("\nBranch distribution BEFORE deletion:")
print((df["branch number"].value_counts(normalize=True) * 100).round(2))

print("\nBranch distribution AFTER deletion:")
print((clean_df["branch number"].value_counts(normalize=True) * 100).round(2))
before = df["branch number"].value_counts(normalize=True).sort_index() * 100
after = clean_df["branch number"].value_counts(normalize=True).sort_index() * 100

comparison = pd.DataFrame({
    "Before deletion": before,
    "After deletion": after
}).fillna(0)

comparison.plot(kind="bar", figsize=(10, 5))

plt.xlabel("Number of Branches")
plt.ylabel("Percentage of Molecules")
plt.title("Branch Distribution Before and After Deletion")
plt.tight_layout()
plt.show()