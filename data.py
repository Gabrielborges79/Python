from datetime import date, time, datetime

data_atual = date.today()
print(data_atual.strftime('%d/%m/%y'))
print(data_atual.strftime('%A %B %Y'))
horario= time(hour=15, minute=18, second=30)
print(horario)
data_atual=datetime.now()
print(data_atual)
print(data_atual.strftime('%H:%M:%S'))