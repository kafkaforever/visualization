import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set_style("whitegrid")

df = pd.read_csv("train.csv")


# Create age groups for the bar chart
def categorize_age(age):
    if pd.isna(age):
        return 'Unknown'
    elif age < 18:
        return 'Teenage (0-18)'
    elif age < 40:
        return 'Young Adults (18-39)'
    elif age < 60:
        return 'Mid Adults (40-59)'
    else:
        return 'Senior Adults (60+)'


df['Age_Group'] = df['Age'].apply(categorize_age)

# Create subplots - Simple version

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Plot 1: Age distribution with seaborn
sns.histplot(df['Age'].dropna(), bins='auto', ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Age Distribution (Seaborn)')

# Plot 2: Sex distribution with seaborn
sns.countplot(x='Sex', data=df, ax=axes[0, 1], palette=['gray', 'darkgoldenrod'])
axes[0, 1].set_title('Sex Distribution (Seaborn)')

# Plot 3: Survival by sex with seaborn
sns.countplot(x='Sex', hue='Survived', data=df, ax=axes[1, 0])
axes[1, 0].set_title('Survival by Sex')
axes[1, 0].legend(title='Survived', labels=['Died', 'Survived'])

# Plot 4: Age vs Survival boxplot
sns.boxplot(x='Survived', y='Age', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Age Distribution by Survival')
axes[1, 1].set_xticklabels(['Died', 'Survived'])

plt.tight_layout()
plt.show()
