import sys
print(sys.version)

sys.stdout.write('This is a regular message \n')
sys.stderr.write('This is a regular message \n')


# Get the size of elements in bytes
a = 44
b = ("John", "Raymond")
c = ["Gregg", "Travis"]
d = True
e = {"name": "e"}


print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
print(sys.getsizeof(e))

# Use arguments to enject code

print("Here are the sys arguments: ",sys.argv)