import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Set style theme
plt.style.use('seaborn-v0_8-pastel')
# print(plt.style.available)

# Read CSV into DataFrame
df = pd.read_csv('class-data-v1.csv')
# print(df.info())

# Catplot
barWidth = 0.2
r1 = np.arange(8)
r2 = r1 + barWidth
r3 = r2 + barWidth

colors = df['Hex Color'].dropna().tolist()

fig, ax = plt.subplots(dpi=300)
ax.bar(r1, df['Webdev Rating'].dropna(), color=colors, width=barWidth, edgecolor='#ffffff', label='WebDev')
ax.bar(r2, df['Java Rating'].dropna(), color=colors, width=barWidth, edgecolor='#ffffff', label='Java')
ax.bar(r3, df['Python Rating'].dropna(), color=colors, width=barWidth, edgecolor='#ffffff', label='Python')

ax.set_xticks(r1 + barWidth)
ax.set_xticklabels(df['Name'].head(8))
ax.legend() # TODO: fix legend to show language names 
plt.title('Programming Language Ratings by Student')
plt.savefig('barchart.png', bbox_inches='tight')
plt.close()

# convert string to datetime object
df['Wakeup Time Weekday'] = pd.to_datetime(df['Wakeup Time Weekday'], format='%H:%M').dt.time

# convert datetime object to float
df['Wakeup Time Weekday Float'] = df['Wakeup Time Weekday'].apply(
    lambda t: t.hour * 60 + t.minute
)
df['Wakeup Before School'] = (8 * 60 + 15) - df['Wakeup Time Weekday Float']
#df_sorted = df.sort_values(by='Wakeup Time Weekday', ascending=True)

# Scatterplot
plt.scatter(df['Wakeup Before School'].dropna(), 
            df['Temperature Preference'].dropna(), 
            s=df['Commute Time Minutes'].dropna() * 10, 
            c=colors, alpha=1)

for i, row in df.iterrows():
    plt.text(row['Wakeup Before School'] - 3.6, row['Temperature Preference'] + 2.2, row['Name'], fontsize=9)

plt.figtext(1, 0.02, 'Size of dots represent commute time', ha='center', fontsize=10, color='gray')

plt.title('Y-axis vs. X-axis')
plt.xlabel('Wakeup Time in Minutes Before School')
plt.ylabel('Temperature Preference')
plt.axis('equal') 


plt.savefig('scatterplot.png')
plt.close()