import os

filename = "test1"

print os.path
print os.path.dirname
print os.path.abspath(filename)
print os.path.dirname(os.path.dirname(os.path.abspath(filename)))

