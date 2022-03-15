with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) # rstrip for eliminating these extra blank lines

# can also stores the line of file in a list inside the `with` block

with open(filename) as file_object:
    lines = file_object.readlines() # readlines method

for line in lines:
    print(line.rstrip())