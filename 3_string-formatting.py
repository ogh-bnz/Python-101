string1 = "This is a text"
string2 = 'This is a text'
string11 = "This is my txt" # i used this srting later

print(string1)
print(string2)

# //

string3 = """This is --
long text"""

print(string3)

# //

print("This is something- I'm Here")
print('This is something- I"m Here')

# //

print("I\"m here for printing\nprint this \\ backslash\non new line")

# // Hex

print("\\ i can also print using hex: \x41, \x42, \x43")

# // multiply a string

string4 = "this is a text\n" * 10
string5 = "A" * 15

print(string4)
print(string5)

# calculate the len

print(len("B" * 17))
print(len(string5))

# Identify the stored text

string6 = "this is a normal string"
print("normal" in string6)
print("hello" in string6)

	# // startswith

print(string6.startswith("this"))
print(string6.startswith("normal"))

# index count

string7 = "Hello this is a normal text"

print(string7.index("e"))
print(string7.index("n"))

# uppercase & lowercase

string8 = "hello my Name Somethings, i'M coDing wiTH PyThon"

print(string8)
print(string8.upper())
print(string8.lower())

# strip

messy = "  This is a Messy Text"

print(messy)
print(messy.strip())

# replace, strip, uppercase

_string = "     can !!!    "

print(_string.replace("!",".").strip().upper())

# split

all_text = "Simple String"
all_text2 = "Simple,String"



print(all_text.split())
print(all_text2.split(","))

# Encode

string9 = "This is a string!"

print(string9.encode())
print(string9.encode("utf-8"))

# Right justify & left justify

string10 = "Easy Text"

print(string10.rjust(25))
print(string10.rjust(25,"!"))
print(string10.ljust(25))
print(string10.ljust(25,"!"))

# Extra knowledge

print("this is a " + "Simple text")
print("string10 is " + str(len(string10)) + " characters long!")

print(1 + 1)
print("1" + "1")
print(type("1" + "1"))

	# format method
print("string10 is {} characters long!".format(len(string10)))
	# the {} is placeholder for format.

print("{} {} {}".format(len(string10), 5.0, 0x12))
	# here {} {} {} total 3 placeholder for format & the values are placed in three placeholder.

print("{2} {0} {1}".format(len(string10), 5.0, 0x12))
	# we can prevent the placeholder's values by index

print("{str_length}".format(str_length=len(string10)))
	#we can also specify the placeholder.

length = len(string10)
print(f"string10 is {length} characters long!!")
 	# use f method in print

print("string10 is {string10_len:.2f} characters long!!".format(string10_len=len(string10)))
print("string10 is {string10_len:.3f} characters long!!".format(string10_len=len(string10)))
print("string10 is {string10_len:.4f} characters long!!".format(string10_len=len(string10)))
print("string10 is {string10_len:.5f} characters long!!".format(string10_len=len(string10)))
	# we can print also in float data type 

print("string11 is {string11_len:x} characters long!!".format(string11_len=len(string11)))
	# string11 length is representing in hex

print("string11 is {string11_len:b} characters long!!".format(string11_len=len(string11)))
	# string11 length is representing in binary
	
print("string11 is {string11_len:o} characters long!!".format(string11_len=len(string11)))
	# string11 length is representing in octel


# Additional information

	#Here, the % is used for string formatting, not for mathematical
	#operations. It acts as a formatting placeholder, meaning that it
	#replaces the %d (or %f or %o) inside the string with the value to
	#its right, which is len(string10) in this case.

print("string10 is %d characters long!" % len(string10))
	# %d is a format specifier for an integer (decimal)

print("string10 is %f characters long!" % len(string10))
	# %f is a format specifier for a floating-point number

print("string10 is %o characters long!" % len(string10))
	# %o is a format specifier for an integer in octal (base 8)