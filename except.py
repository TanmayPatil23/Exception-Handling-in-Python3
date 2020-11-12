# Handling NameError
try:
    print(x)
except:
    print("NameError: name \'x\' is not defined")
finally:
    print("In here, we try to print an undeclared variable named \'x\'\n")

# Handling ModuleNotFoundError
try:
    import x
except:
    print("ModuleNotFoundError: No module named \'x\'")
finally:
    print("In here, we try to import an arbitrary module named \'x\'\n")

# Handling IndexError
arr = [1, 2]
try:
    print(arr[2])
except:
    print("IndexError: list index out of range")
finally:
    print("In here, we try to dereference the value at index out of bound of list\n")

# Handling TypeError
try:
    print(3 + '3')
except:
    print("TypeError: unsupported operand type(s) for +: \'int\' and \'str\'")
finally:
    print("In here, we try to add a number to string literal\n")

# Handling AttributeError
try:
    import numpy
    numpy.read(10)
except:
    print("AttributeError: module \'numpy\' has no attribute \'read\'")
finally:
    print("In here, we try to use an attribute named \'read\' with the numpy library which indeed doesn't exist\n")

# Handling FileNotFoundError
try:
    f = open("x.txt", "r")
except:
    print("FileNotFoundError: [Errno 2] No such file or directory: \'x.txt\'")
finally:
    print("In here, we try to open a file with no existence\n")

# Handling ZeroDivisionError
try:
    print(1 / 0)
except:
    print("ZeroDivisionError: division by zero")
finally:
    print("In here, we try to divide a number by 0\n")
