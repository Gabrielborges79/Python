import os

ip_host =  input("Digite o IP ou Host a ser verificado: ")

os.system('ping -n 6 {}'.format(ip_host))

