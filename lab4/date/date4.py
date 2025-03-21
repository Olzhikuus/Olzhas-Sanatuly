from datetime import datetime

date1 = datetime(2023, 10, 25, 14, 30, 0) 
date2 = datetime(2023, 10, 26, 15, 45, 30) 

difference = date2 - date1

difference_in_seconds = difference.total_seconds()

print(f"The difference between the two dates is {difference_in_seconds} seconds.")

""""
Создаем две даты → datetime(год, месяц, день, час, минута, секунда).
Находим разницу → date2 - date1 (возвращает timedelta).
Переводим разницу в секунды → .total_seconds().
Выводим результат.
"""