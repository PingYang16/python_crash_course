dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250
# error, tuple object does not support item assignment

for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)