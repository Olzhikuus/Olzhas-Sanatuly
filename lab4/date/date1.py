import datetime

date = datetime.datetime.now()
subtrac = date - datetime.timedelta(days=5)

print("Substacted date: ", subtrac)

"""
datetime.datetime.now() → Получаем текущую дату и время.
datetime.timedelta(days=5) → Создаём объект, который представляет 5 дней.
date - timedelta(days=5) → Вычисляем дату 5 дней назад.
"""

