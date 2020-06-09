print ("Hello")
print ("Tyler" * 10)
print "Hello World"

x = 1
print (id(x))
print (type(x))

x = [1, 2, 3, 4]
x.append(5)
print (id(x))

name = ("Tyler Trudgeon")
print(len(name))
print(name[0])
print(name[0:5])
print(name[0:])
print (name)

x = 1
if x == 1:
    print (x)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Int: %d" % myint)
