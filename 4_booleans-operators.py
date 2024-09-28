valid = True
not_valid = False

print("-----------------")
print(valid)
print(not_valid)

print("-----------------")
print(valid == True)
print(not_valid == True)

# this "!" means "not" 
print("-----------------")
print(valid != True) # valid is not equals to True
print(not_valid != True) # not_valid is not equals to True

# "not" this returns opposite of the value - behave like: false
print("-----------------")
print(not valid) # false + true = false
print(not not_valid) # false + false = true

# more compare
print("-----------------")
print((10 < 9) == True) # 10 is less then to 9 = false
print((10 > 9) == True) # 10 is greater then to 9 = true 
print((10 <= 10) == True) # 10 is less then or equals to 10 = true
print((10 >= 10) == True) # 10 is greater then or equals to 10 = true
print((10 != 10) == True) # 10 is not equals to 10 = false

# if we need result in booleans then we don't need to add this "== True" 
print("-----------------")
print((10 < 9))
print((10 > 9))
print((10 <= 10))
print((10 >= 10))
print((10 != 10))

print("-----------------")

print((10 > 5 and 10 < 5)) 
	# if all the conditions is True then, it return True.
	# If any conditions is False then, it returns False.

print((10 > 5 or 10 < 5))
	# if any conditions is True
	# then, it returns true & others condistion are getting ignored

# bool() func in python
print("-----------------")

print(bool(0))
	# 0 is a falsey value.
	# bool(0) converts 0 to boolean, which is False.

print(bool(1))
	# 1 (and any non-zero number) is a truthy value.
	# bool(1) converts 1 to boolean, which is True.

print(bool(0) == False)
print(bool(1) == True)

# 
print("-----------------")
print(10 + 10) # normal oparetion
print(10 - 10) # normal oparetion
print(10 * 10) # normal oparetion
print(10 / 10) # normal oparetion

# Floor Division
print(10 // 3) # returns 3 because it rounds down the result of the division
# Exponentiation
print(10 ** 10) # returns 10,000,000,000 because it calculates 10 to the power of 10.
# Remainder
print(10 % 10) # returns 0 because there is no remainder when 10 is divided by 10.

# Compound Assignment Operators
print("-----------------")

x = 10
print(x)

x = x + 4
print(x)
	# we do same thing in a short way

x = 10
print("------")

x += 5  # is x = x + 5
print(x)  # Output: 15

x -= 9  # is to x = x - 9
print(x)  # Output: 6

x *= 10  # is to x = x * 10
print(x)  # Output: 60

x /= 5  # is to x = x / 5
print(x)  # Output: 12.0

x **= 5  # is to x = x ** 5
print(x)  # Output: 248832.0

x %= 7  # is to x = x % 7
print(x)  # Output: 2.0