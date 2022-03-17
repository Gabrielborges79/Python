segundos = int(input())


horas = int (segundos/3600)
resto_h = int (segundos%3600)
minutos = int (resto_h/60)
resto_m= int(resto_h%60)

segundos = resto_m
print("{}:{}:{}".format(horas, minutos, segundos))