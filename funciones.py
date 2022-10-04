def suma(a, b):
    c = a+b
    return c

def resta(a, b):
    c= a-b
    return c

def sumatoria(*args):
    sum = 0
    for i in args:
        sum = sum + i
        print(sum)
        
def argm(**kargs):
    print(kargs)


# num1 = int(input("Numero 1: "))
# num2 = int(input("Numero 2: "))

# print("La suma es: ", suma(num1, num2))

# print("La resta es: ", resta(num1, num2))

sumatoria(1, 1,1,1,1,1)
argm(nombre="Jose", edad=21, licencia=True)
