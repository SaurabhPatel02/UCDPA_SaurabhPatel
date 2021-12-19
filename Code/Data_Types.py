# define variable and assign values
a = 4
b= 4

# define function
add = a+b
sub = a-b
mult = a*b
div = a/b

# understand standard calc function
print(add)
print(sub)
print(mult)
print(div)

#  understand core data types string, int, float, bool
a = "testdatatype"
print (type(a))
a = 6
print(type(a))
a = 5.5
print(type(a))
a = True
print(type(a))
a = "543"
print(type(a))

# understand core data structures tuple,list,directory
# understand tuple - immutable ()
a = 1, 2, 3, "test", 5.5
print(type(a))
a = ()
print(type(a))

# print +/- index values
a=(1, 2, 3, "test", 5.5, True)
print(type(a))
print(a[2])
print(a[3], a[-3])

#  print +/- index range values
a=(11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 111, 112)
print(a[3])
print(a[1:6])
print(a[9:12])
print(a[9:])
print(a[9:-1])
print(a[:9])
print(a[5:10])

# update tuple value - immutable
tup=(11, 22, 33, "test", 5.5, True)
print(tup)
# tup[1] = 22.5 # assign new value to tuple
print(tup)  # print new tuple

# understand list - mutable []
lst = [11, 22, "str", False, 5.5]
print(type(lst))
print(type(lst[3]))
lst[1] = 33  # assign new value
print(lst[1])  # print updated value
print(lst)

lst[1:3] = [33, 22]  # update multiple values in range
print(lst)  # print updated list

# understand dictionary - key:value pair {}
dic = {"ID": 10, "Name": "Pank", "Salary": 20000}
print(type(dic))
print(dic["ID"])
print(dic["Salary"])
print(type(dic["ID"]))

# understand advance data structures
# list->numpy array (4 times faster) , store a column -> pandas , store data in tabular format row, column, header in data frane

