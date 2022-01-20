# modulo operator (%)
# divides one number by another number and returns the remainder:
ans = 4 % 3
print(ans)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")