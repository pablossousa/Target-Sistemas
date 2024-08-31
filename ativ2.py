num = int(input("Digite um número: "))

x = 0
y = 1
validador = 0

while x <= num:
    print(x)
    validador = x
    temp = x + y
    x = y
    y = temp
    
if (num == validador):
    print("O número está na sequência de Fibonacci")
else:
    print("O número não está na sequência de Fibonacci")