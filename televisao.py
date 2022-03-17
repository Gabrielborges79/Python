class Televisao:
    def __init__ (self):
        self.ligada = False
        self.canal=5
    def power (self):
        if self.ligada:
            self.ligada=False
        else:
            self.ligada=True
    def aumenta_canal(self):
        self.canal+= 1
    def diminui_canal(self):
        self.canal-=1

tele = Televisao()
print(tele.ligada)
tele.power()
print(tele.ligada)
tele.power()
print(tele.ligada)
