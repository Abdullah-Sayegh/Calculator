#This calculator is in english strings
num1 = float(input("Calculater: Enter the first numer. You: "))
symbol = input("Calculater: Enter symbol. You: ")
num2 = float(input("Calculater: Enter the second numer. You: "))

if symbol == "+":
    print(num1 + num2)

elif symbol == "-":
    print(num1 - num2)

elif symbol == "*":
    print(num1 * num2)

elif symbol == "/":
    print(num1 / num2)


else:print("Wrong operator try agin")
