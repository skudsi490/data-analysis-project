import pandas as pd
import random
from prettytable import PrettyTable
from colorama import Fore, Style

# הגדרת נתותנים
customers = [f'Customer{i+1}' for i in range(20)]
persons = [random.randint(1, 5) for _ in range(20)]
days = [random.randint(2, 10) for _ in range(20)]
extras = [random.randint(400, 1800) for _ in range(20)]
before_vat = [300 * persons[i] + 400 * days[i] + extras[i] for i in range(20)]
pay = [1.17 * before_vat[i] for i in range(20)]

# Creating DataFrame
df = pd.DataFrame({
    'Customer': customers,
    'Persons': persons,
    'Days': days,
    'Extras': extras,
    'Before VAT': before_vat,
    'Pay': pay
})

# Display data using PrettyTable
table = PrettyTable()
table.field_names = df.columns.tolist()

for _, row in df.iterrows():
    table.add_row(row.tolist())

print(table)


# 1. מצאו את התוספת הגבוהה ביותר
highest_addition = df['Extras'].max()
print(Fore.GREEN + f'Highest Addition: {highest_addition}' + Style.RESET_ALL)

# 2. מצאו את מספר הימים הנמוך ביותר
lowest_days = df['Days'].min()
print(Fore.BLUE + f'Lowest Number of Days: {lowest_days}' + Style.RESET_ALL)

# 3. כמה עסקאות מכילות אדם אחד בחדר
one_person_transactions = df[df['Persons'] == 1].shape[0]
print(Fore.CYAN + f'Transactions with One Person: {one_person_transactions}' + Style.RESET_ALL)

# 4. הציגו את שם הלקוח וכמות האנשים בחדר, עבור כלל העיסקאות אשר סכום העיסקאות שלהם גבוה מ 4000
transactions_above_4000 = df[df['Before VAT'] > 4000][['Customer', 'Persons']]
print(Fore.MAGENTA + 'Transactions Above 4000 Before VAT:' + Style.RESET_ALL)
for _, row in transactions_above_4000.iterrows():
    print(f"{row['Customer']} with {row['Persons']} persons")

# 5. מה ממוצע המחיר לפני מע"מ של כלל העיסקאות
average_before_vat = df['Before VAT'].mean()
print(Fore.YELLOW + f'Average Price Before VAT: {round(average_before_vat, 2)}' + Style.RESET_ALL)
