if True:
	print("True")



if False:
	print("False")



if not False: # "not" operator
	print("Not False")



if 1 < 1: # Basic Statement
	print("1 < 1")
else:
	print("Else Reached")



if 1 <= 1:
	print("1 <= 1")


print("###########")# For Better View


if 0 < 1 and 1 > 0: # "and" operator
	print("Condition Passed")




print("###########")# For Better View

if False or 1 > 0: # "or" Operator
	print("Condition Passed")



if (False or 1 > 0) and (1 == 1):
	print("1 is 1 = 1")


if (False or 1 > 0) or (1 == 2):
	print("1 is not 1 = 2")



# Ternary

if 1 > 0: print("1 is 1 > 0")

print("1") if 0 > 1 else print("Else")