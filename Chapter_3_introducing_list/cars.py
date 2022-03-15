# sort a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # now in alphabetical order
# cannot revert to original order

# passing the argument reverse = True to sort()
cars.sort(reverse = True)
print(cars) # now in reverse alphabetical order

# sort a list temporarily with the sorted() function
# maintain the original order of list but present it in a sorted order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)

# print a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# find the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

