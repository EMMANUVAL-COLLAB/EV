num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("Select operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice {1/2/3/4}: ")

if choice == "1":
    print(num1+num2)
elif choice == "2":
    print(num1-num2)
elif choice == "3":
    print(num1*num2)
elif choice == "4":
    print(num1/num2)
else:
    print("Inavalid")