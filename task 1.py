import csv

list_of_salary = []
start_date = []
employees=[]

with open("users1.csv", newline="") as users_csv:
    user_reader = csv.DictReader(users_csv)
    for row in user_reader:
        list_of_salary.append(int(row["Оклад"]))
        start_date.append(row["Дата найма"])
        employees.append(row["ФИО"])


list_of_award = []

for salary in list_of_salary:
    award = salary / 100 * 3  
    list_of_award.append(award)  

print(list_of_award)

from datetime import datetime


list_of_new_salary = []

for i in range(len(start_date)):
    date = datetime.strptime(start_date[i], "%d.%m.%Y")  
    if date < datetime(2015, 1, 1):
        new_salary = list_of_salary[i] + list_of_salary[i] / 100 * 7
    else:
        new_salary = list_of_salary[i] + list_of_salary[i] / 100 * 5
    list_of_new_salary.append(new_salary)

print(list_of_new_salary)   


old_employees=[]

for i in range(len(start_date)):
    date = datetime.strptime(start_date[i], "%d.%m.%Y")
    if date < datetime(2020, 1, 1):
        old_employees.append(employees[i])  

print(old_employees)
