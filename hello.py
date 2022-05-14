import re

print("Hello, world!")

"""
	name = input("What's your name? ")
	print("Hello", name, sep=" ")
	print("Hello " + name)
	print(f"Hello {name}")
	print("Hello %s" % (name))
	print("Hello {}".format(name))
"""

a = "str1 str1 str1"
a = re.sub(r"str1$", "", a)
