import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('academic_journey_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Set style
sns.set_theme(style="whitegrid")

# 1. Study Hours vs Sleep Hours over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Study_Hours'], marker='o', label='Study Hours')
plt.plot(df['Date'], df['Sleep_Hours'], marker='s', label='Sleep Hours')
plt.title('Study vs Sleep Hours Over Time')
plt.xlabel('Date')
plt.ylabel('Hours')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('study_vs_sleep.png')
plt.close()

# 2. Stress Level vs Productivity Level
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Stress_Level', y='Productivity_Level', hue='Semester', size='Course_Load', sizes=(50, 200))
plt.title('Stress Level vs Productivity Level')
plt.xlabel('Stress Level (1-5)')
plt.ylabel('Productivity Level (1-5)')
plt.tight_layout()
plt.savefig('stress_vs_productivity.png')
plt.close()

# 3. Assignment Scores Trend
plt.figure(figsize=(12, 6))
df_scores = df.dropna(subset=['Assignment_Score'])
plt.plot(df_scores['Date'], df_scores['Assignment_Score'], marker='D', color='green')
plt.title('Assignment Scores Trend')
plt.xlabel('Date')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('assignment_scores.png')
plt.close()

# 4. Study Hours: Weekday vs Weekend
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Is_Weekend', y='Study_Hours')
plt.title('Study Hours: Weekday vs Weekend')
plt.xlabel('Is Weekend')
plt.ylabel('Study Hours')
plt.tight_layout()
plt.savefig('weekday_vs_weekend.png')
plt.close()

print("EDA visualizations generated successfully.")
