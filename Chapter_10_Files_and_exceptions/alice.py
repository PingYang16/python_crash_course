def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist.") # or use 'pass' to silent
    else:
        # count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words. ")

filenames = ['text_files/alice.txt', 'text_files/little_women.txt', 'text_files/moby_dick.txt', 'text_files/siddhartha.txt']
for filename in filenames:
    count_words(filename)