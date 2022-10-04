
class Operaciones():
    def __init__(self, a, b):
        self.num1=a
        self.num2=b
    def suma(self):
        c = self.num1 + self.num2
        return c
    def resta(self):
        c = self.num1 - self.num2
        return c
    def mult(self):
        c = self.num1 * self.num2
        return c
    def div(self):
        c = self.num1 / self.num2
        return c

print("Inicio programa")
op = Operaciones(3,4)
print(op.div())
print("Fin programa.")
