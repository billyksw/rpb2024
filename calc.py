def main():




#1.
print("Hello World")

#2.
def main():
    print("Hello World");

main()


#3.
def func():
    print("Hello World")

if __name__=="__main__":
    print("interpreter")
    print(__name__)

else:
    print("import")
    print(__name__)

import myPythonFile
myPythonFile.func()


#4.
def main():
    print("Let's implement addition. Type two numbers for x and y.")

    x = int(input("x > "))
    y = int(input("y > "))

    print("%d + %d = %d" % (x, y, add(x, y)))

def add(x,y):
    return x+y

if __name__ == "__main__":
    main()
