import pandas as pd
from matplotlib import pyplot as plt

# Set style theme
plt.style.use('seaborn-v0_8-pastel')
print(plt.style.available)

# Read CSV into DataFrame
df = pd.read_csv('class-data-v1.csv')
print(df.info())

# Bar charts are great for COUNTS
# often use String data for the labels
df_sorted = df.sort_values(by='', ascending=False)

colors = ['']
plt.bar(df_sorted['Name'], df_sorted['WebDev Rating'], color=colors, width=0.6)

# Often need to rotate labels on x acis for readability
plt.xticks(rotation=45)
plt.savefig('barchart.png', bbox_inches='tight')
plt.close()