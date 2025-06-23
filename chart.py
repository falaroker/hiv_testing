import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/IT OFFICE/Desktop/testing.csv")

# Bar chart: Gender distribution
sns.countplot(data=df, x='SEX', palette='Set2')
plt.title('HIV Testing Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Individuals Tested')
plt.tight_layout()
plt.show()

# Bar chart: Age distribution
sns.countplot(data=df, x='AGE', palette='Set3')
plt.title('HIV Testing Count by Age')
plt.xlabel('Age')
plt.ylabel('Number of Individuals Tested')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
