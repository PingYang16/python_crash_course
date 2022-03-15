motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modifying
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements
motorcycles[0] = 'honda'
motorcycles.append('ducati')
print(motorcycles)

# building a list dynamically by append
motor = []
motor.append('honda')
motor.append('yamaha')
print(motor)

# insert
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# remove using the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# remove using the pop() method
# you might want to use the value of an item after you remove it from a list
# pop() method removes the last item in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# pop items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
# summary: when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

# remove an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

