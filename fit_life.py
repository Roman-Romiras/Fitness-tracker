# Проект FitLife - MVP версия 1.0


user_name = input("Привет! Я фитнес-трекер. Напиши как тебя зовут!")
user_age = input("Приятно познакомиться! Сколько тебе лет?")
age = int(user_age)
user_height = input("Какой у тебя рост в сантиметрах?") # Для удобства пользователя
user_weight = input("Теперь напиши свой вес в килограммах!")
height = float(user_height) / 100
weight = float(user_weight)
bmi = weight / (height ** 2)
imt = round(bmi, 1)
water_ml = weight * 30
water_l = water_ml / 1000
print("-" * 40)
print(f"Отчет для пользователя: {user_name.title()} {age} г.")
print(f"Спасибо, {user_name.title()}! Твой индекс массы тела {imt}")
print(f"Для поддержания водного баланса тебе нужно {water_l} л. жидкости в день")
print(f"Расчет окончен. До свидания, {user_name.title()}, Будьте здоровы! ")