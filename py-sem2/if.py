# a = 21
# b = 12

# if b > a:
#     print("b greater than a")
# elif a == b:
#     print("a and b equals")
# else:
#     print("a greater than b")

# age = int(input("enter age 1 : "))

# if age <= 13:
#     print("child")
# else:
#     if age >= 19:
#         if age >=25:
#             print("senior citisen")
#         else:
#             print("adult")
#     else:
#         print("teen")


# age2 = int(input("Enter Your age: "))

# if age2 > 65:
#     print("Can't vote (Vote expired) [sldkf] Over Kill +++")
# else:
#     if age2 >= 18 :
#         print("Eligible to vote")
#     else:
#         if age2 < 0:
#             print("Invalid age")
#         else:   
#             print("not eligible to vote")

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))

    if num > 5:
        print(num, "is greater than 5")
    elif num < 5:
        print(num, "is less than 5")
    else:
        print("is 5")

print("The Enddddd")