
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Crime_Data_2023.csv")  # Adjust path if needed
df.columns = df.columns.str.strip().str.lower()

# Analyze top 10 most frequent offenses
top_offenses = df['description'].value_counts().head(10)

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=top_offenses.values, y=top_offenses.index, palette="magma")
plt.xlabel("Number of Incidents")
plt.ylabel("Crime Type")
plt.title("Top 10 Most Common Crime Types in Syracuse (2023)")
plt.tight_layout()
plt.savefig("top_crime_types.png")
