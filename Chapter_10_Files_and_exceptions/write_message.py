filename = 'text_files\programming.txt'

with open(filename, 'w') as file_object: # 'w' stands for write mode, 'r' => read, 'a' => append, 'r+' => read+write
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    # python can only write str into text file, so convert numerical data before writing

# can also add content to a file instead of writing over existing content
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")