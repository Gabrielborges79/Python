class Calculadora:
    def __init__(self, num1, num2):
        self.a=num1
        self.b=num2
    def soma (self):
        return self.a+self.b
    def subtracao (self):
        return self.a - self.b
    def multiplicacao (self):
        return self.a* self.b
    def divisao (self):
        return self.a/self.b

cal = Calculadora(10, 2 )
print(cal.soma())
print(cal.subtracao())
print(cal.multiplicacao())


