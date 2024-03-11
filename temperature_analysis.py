import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from colorama import Fore, Style

# ייבא את קובץ הטמפרטורות ל DF
wb = pd.read_excel('Temp.xlsx', engine='openpyxl')

# הציגו את ה DF
print(wb)

# להתעלם מעמודת העיר
numeric_columns = wb.select_dtypes(include='number').columns
avg_temps = wb[numeric_columns].mean()
max_temps = wb[numeric_columns].max()

# יצירת טבלאות
avg_table = PrettyTable()
max_table = PrettyTable()

avg_table.field_names = ["Month", "Average Temp (°C)"]
max_table.field_names = ["Month", "Max Temp (°C)"]

for month in numeric_columns:
    avg_table.add_row([month, round(avg_temps[month], 2)])
    max_table.add_row([month, max_temps[month]])

print(Fore.CYAN + "Average Temperatures Per Month" + Style.RESET_ALL)
print(avg_table)
print(Fore.MAGENTA + "\nMaximum Temperatures Per Month" + Style.RESET_ALL)
print(max_table)

# מצאו ממוצע ומקסימום לכל עמודה והצגת גרף כפול
fig, axs = plt.subplots(2, 1, figsize=(10, 10))
axs[0].bar(avg_temps.index, avg_temps.values, color='skyblue')
axs[0].set_title('Average Temperatures')
axs[0].set_ylabel('Temperature (°C)')
axs[1].bar(max_temps.index, max_temps.values, color='orange')
axs[1].set_title('Maximum Temperatures')
axs[1].set_ylabel('Temperature (°C)')
plt.tight_layout()

# מצא את כמות הטמפרטורות בטבלה
total_temps = wb[numeric_columns].count().sum()
print(f"\nTotal number of temperature entries: {total_temps}")

# מצאו את כמות הטמפרטורות בטווחים : 0-10,10-20,20-30
temperature_values = wb[numeric_columns].values.flatten()
ranges = {"0-10": 0, "10-20": 0, "20-30": 0}

for temp in temperature_values:
    if 0 <= temp < 10:
        ranges["0-10"] += 1
    elif 10 <= temp < 20:
        ranges["10-20"] += 1
    elif 20 <= temp < 30:
        ranges["20-30"] += 1

range_table = PrettyTable()
range_table.field_names = ["Temperature Range (°C)", "Count"]
for range, count in ranges.items():
    range_table.add_row([range, count])

print(Fore.YELLOW + "\nTemperature Ranges Count" + Style.RESET_ALL)
print(range_table)

# צרו גרף עוגה אשר יראה לנו באחוזים מה החלק באחוזים של כל אחד מהטווחים.
labels = list(ranges.keys())
sizes = list(ranges.values())
colors = ['#ff9999', '#66b3ff', '#99ff99']
explode = (0.1, 0, 0)

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Temperature Ranges Distribution')
plt.show()
