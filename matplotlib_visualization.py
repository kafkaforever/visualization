import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

# Figure with 3 subplots in one row
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot 1: Age distribution
age_data = df['Age']
q1 = np.percentile(age_data, 25)
q2 = np.percentile(age_data, 50)
q3 = np.percentile(age_data, 75)

axes[0].hist(age_data, bins='auto', edgecolor='black', alpha=0.7, label='Age Distribution')
axes[0].axvline(q1, color='red', linestyle='dashed', linewidth=2, label=f'Q1: {q1:.2f}')
axes[0].axvline(q2, color='green', linestyle='dashed', linewidth=2, label=f'Median: {q2:.2f}')
axes[0].axvline(q3, color='purple', linestyle='dashed', linewidth=2, label=f'Q3: {q3:.2f}')
axes[0].set_title('Age Distribution with Quartiles')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Count')
axes[0].legend()
axes[0].grid(axis='y', alpha=0.8)

# Plot 2: Pie chart for sex
sex_series = pd.Series(df['Sex'])
sex_counts = sex_series.value_counts()
labels = sex_counts.index
sizes = sex_counts.values

axes[1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
axes[1].set_title('Distribution of Sexes on Ship')

# Plot 3: Bar chart for survivors by age groups
age_group_labels = ['Teenage(0-18)', 'Young Adults(18-39)', 'Mid Adults(40-59)', 'Senior Adults(60+)']
categories = [1, 2, 3, 4]
survived_people = df[df['Survived'] == 1]

teenage_survivers = survived_people[survived_people['Age'] < 18].shape[0]
yadults_survivers = survived_people[(survived_people['Age'] > 18) & (survived_people['Age'] < 40)].shape[0]
madults_survivers = survived_people[(survived_people['Age'] > 40) & (survived_people['Age'] < 60)].shape[0]
sadults_survivers = survived_people[(survived_people['Age'] > 60)].shape[0]
data_by_categories = [teenage_survivers, yadults_survivers, madults_survivers, sadults_survivers]

bars = axes[2].bar(categories, data_by_categories, color='skyblue')
axes[2].set_xlabel('Age Group')
axes[2].set_ylabel('Number of Survived People')
axes[2].set_title('Survivors by Age Groups')
axes[2].set_xticks(categories)
axes[2].set_xticklabels(age_group_labels, rotation=45, ha='right')

legend_labels = [f'{cat}: {label}' for cat, label in zip(categories, age_group_labels)]
axes[2].legend(bars, legend_labels, loc='upper right', title='Categories')

plt.tight_layout()
plt.show()