"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

with open('src/foo.txt', 'r') as f1:
    print(f1.read())

# f1 = open('src/foo.txt', 'r')
# print(f1)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

contents = '''
This is some arbitrary content

It's cool I guess

Not as cool as Python
'''

with open('src/bar.txt', 'w') as f2:
    f2.write(contents)

with open('bar.txt') as f3:
    if f3.read() == contents:
        print("It worked!")
