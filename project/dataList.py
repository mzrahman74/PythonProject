from project import a, c

values = [1, 2, "mohammad", 100, 102]
# list is data type that allows multiple values and can be different data types

print(values[0])

print(values[-1])

print(values[1:4])

values.insert(3, "Rahman")
print(values)

values.append("Yusuf")
print(values)

values[2] = "Mohammad" # updated

print(values)
del values[2]
print(values)

# tuple not immutable

val = [1, 5, 7, 9, "Nuhaa"]
print(val[1])

val[4] = "Alesha"

print(val)

#dic

dic = {a: 2, c: "Nuhaa", "Bangladesh": "Dhaka"}

print(dic["Bangladesh"])

#

dict = {}

dict["firstName"] = "Mohammad"
dict["lastName"] = "Rahman"

print(dict)