#This calculator is in english strings
num1 = float(input("Calculater: Enter the first numer. You: "))
while True:
    symbol = input("Calculater: Enter symbol. You: ")
    if symbol == "=":
        print(num1)
        break
    num2 = float(input("Calculater: Enter the second numer. You: "))

    if symbol == "+":
        num1 = num1 + num2

    elif symbol == "-":
        num1 = num1 - num2

    elif symbol == "*":
        num1 = num1 * num2

    elif symbol == "/":
        num1 = num1 / num2

    elif symbol == "^":
        num1 = num1 ** num2

    else:print("Wrong operator try agin")
