Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

# Расчет общего количества посещений
total_visits = sum(Week)

# Расчет средней посещаемости
average_visits = total_visits / len(Week)

# Расчет выручки салона
total_revenue = sum(price * visits for price, visits in zip(Price, Week))

# Расчет выручки по видам маникюра
revenue_by_style = {style: price * visits for style, price, visits in zip(Nail_style, Price, Week)}

# Расчет средней выручки в день по видам маникюра
average_daily_revenue_by_style = {style: revenue / 7 for style, revenue in revenue_by_style.items()}

# Вывод результатов
print(f"Общее количество посещений салона: {total_visits}")
print(f"Среднее значение посещений салона: {average_visits:.2f}")
print(f"Выручка салона: {total_revenue} руб.")
print("Выручка по видам маникюра:")
for style, revenue in revenue_by_style.items():
    print(f"{style}: {revenue} руб.")
print("Средняя выручка в день по видам маникюра:")
for style, avg_revenue in average_daily_revenue_by_style.items():
    print(f"{style}: {avg_revenue:.2f} руб.")