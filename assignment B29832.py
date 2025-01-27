"""num = int(input("Enter a number"))
if num%3==0:
    print("odd")
else:
    print("even")


Text = "Christina Kirabo"
reversed_Text = Text[::-1]
print(reversed_Text)"""


for a in range(1,7):
    for b in range(1,7):
        result= a*b
        print(f"{a}*{b}={result}")
        print()


"""        number = int(input("enter a number from 1 to 100 "))
        if number%3==0 and number%5==0:
            print("Fizzbuzz")
        elif number%5==0:
            print("Buzz")
        elif number%3==0:
            print("Fizz")
        else:
            print(" ")



def find_maximum(number1, number2, number3):
    return max(number1, number2, number3)

number1 = float(input("enter the first number:"))
number2 = float(input("enter the second number:"))
number3 = float(input("enter the third number:"))
maximum_number = find_maximum(number1, number2, number3)
print(f"The maximum nymber of the three numbers is{maximum_number}")


for i in range(11):
    if i == 4 or i == 8:
        continue
    print(i,end=" ")"""