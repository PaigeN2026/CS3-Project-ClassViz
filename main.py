import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Set style theme
plt.style.use('seaborn-v0_8-pastel')
print(plt.style.available)

# Read CSV into DataFrame
df = pd.read_csv('class-data-v1.csv')
print(df.info())

barWidth = 0.2
r1 = np.arange(8)
r2 = r1 + barWidth
r3 = r2 + barWidth

colors = df['Hex Color'].dropna().tolist()

fig, ax = plt.subplots(dpi=300)
ax.bar(r1, df['Webdev Rating'].dropna(), color=colors, width=barWidth, edgecolor='#ffffff', label='WebDev')
ax.bar(r2, df['Java Rating'].dropna(), color=colors, width=barWidth, edgecolor='#ffffff', label='Java')
ax.bar(r3, df['Python Rating'].dropna(), color=colors, width=barWidth, edgecolor='#ffffff', label='Python}')


ax.set_xticks(r1 + barWidth)
ax.set_xticklabels(df['Name'].head(8))
ax.legend() # TODO: fix legend to show language names 
plt.title('Programming Language Ratings by Student')
plt.savefig('barchart.png', bbox_inches='tight')
plt.close()