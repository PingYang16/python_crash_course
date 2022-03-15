current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
# continue is to tell Python to ignore the rest of the loop and return to the beginning.
# So, in this situation, when the number is divisible by 2, it will jump the print procedure.