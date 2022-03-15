bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles[0].title())

# the index positions start at 0, not 1
print(bicycles[1])
print(bicycles[3])

# index -1, return the last item in the list
print(bicycles[-1])
# index -2, return the second item from the end of the list
print(bicycles[-2])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)