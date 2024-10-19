set1 = {"1", "2", "3", "4"}
print(set1)
print(type(set1))

set1_str = {"a", "b", "c", "d"}
print(set1_str)
print(type(set1_str))

set2 = {"a", "a", "a"}
print(set2)
print(len(set2))

set3 = {"a", 1, False}
print(set3)

set4 = set(("a", "b", "c", True, 4))
print(set4)

set1.add("m")
print(set1)

set3.update(set4)
print(set3)

list1 = ["a", 14, False, "b", "c"]
set5 = {4, 5, 6, 7}
print(list1)
print(set5)

set5.update(list1)
print(set5)