from datetime import datetime

now = datetime.now()

day = str(now.day).zfill(2)
month = str(now.month).zfill(2)
year = str(now.year)
hour = str(now.hour).zfill(2)
minute = str(now.minute).zfill(2)

print(f"Data: {day}/{month}/{year}")
print(f"Hora: {hour}:{minute}")