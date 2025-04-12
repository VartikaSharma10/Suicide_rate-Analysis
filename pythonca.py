import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv")
df = df[df["ESTIMATE"].notna()]

keywords = ['White', 'Black', 'Asian', 'American Indian', 'Hispanic']
race_df = df[df["STUB_LABEL"].str.contains('|'.join(keywords), case=False, na=False)].copy()
race_df["RACE_GROUP"] = race_df["STUB_LABEL"].str.extract(r"(White|Black.*?|Asian.*?|American Indian.*?|Hispanic.*?)", expand=False)
race_df["RACE_GROUP"] = race_df["RACE_GROUP"].str.strip()

# 1. Bar Graph – Average suicide rate by race/ethnicity
plt.figure(figsize=(8,5))
race_avg = race_df.groupby("RACE_GROUP")["ESTIMATE"].mean().sort_values()
race_avg.plot(kind='bar', title="Avg Suicide Rate by Racial/Ethnic Group", color='skyblue')
plt.ylabel("Death Rate per 100,000")
plt.tight_layout()
plt.show()

# 2. Heatmap – Rates over time by race
heat_data = race_df.groupby(["YEAR", "RACE_GROUP"])["ESTIMATE"].mean().unstack()
plt.figure(figsize=(10,6))
sns.heatmap(heat_data.T, cmap="YlOrBr", annot=True, fmt=".1f")
plt.title("Suicide Rates Over Time by Racial/Ethnic Group")
plt.tight_layout()
plt.show()

# 3. Line Graph – Suicide trends by race
plt.figure(figsize=(10,5))
for race in race_df["RACE_GROUP"].unique():
    trend = race_df[race_df["RACE_GROUP"] == race].groupby("YEAR")["ESTIMATE"].mean()
    plt.plot(trend, label=race)
plt.title("Suicide Rate Trends by Race")
plt.ylabel("Death Rate")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Pie Chart – Proportion of avg suicide rates by race
plt.figure(figsize=(6,6))
plt.pie(race_avg, labels=race_avg.index, autopct='%1.1f%%', startangle=140)
plt.title("Share of Avg Suicide Rates by Race/Ethnicity")
plt.tight_layout()
plt.show()

# 5. Scatter Plot – Suicide rate by year for each race
plt.figure(figsize=(10,5))
sns.scatterplot(data=race_df, x="YEAR", y="ESTIMATE", hue="RACE_GROUP", alpha=0.6)
plt.title("Scatter: Suicide Rates Across Years by Race")
plt.ylabel("Death Rate")
plt.tight_layout()
plt.show()

# 6. Histogram – Distribution of suicide rates by race
plt.figure(figsize=(10,5))
sns.histplot(data=race_df, x="ESTIMATE", hue="RACE_GROUP", element="step", kde=True, bins=30)
plt.title("Distribution of Suicide Rates by Race")
plt.xlabel("Death Rate per 100,000")
plt.tight_layout()
plt.show()

# 7. Pair Plot – Suicide rates vs year by race
sns.pairplot(race_df, vars=["YEAR", "ESTIMATE"], hue="RACE_GROUP", palette="tab10")
plt.suptitle("Pair Plot: Suicide Estimate vs Year by Race", y=1.02)
plt.tight_layout()
plt.show()
