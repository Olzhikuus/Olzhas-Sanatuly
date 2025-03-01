from datetime import datetime

date1 = datetime(2023, 10, 25, 14, 30, 0) 
date2 = datetime(2023, 10, 26, 15, 45, 30) 

difference = date2 - date1

difference_in_seconds = difference.total_seconds()

print(f"The difference between the two dates is {difference_in_seconds} seconds.")