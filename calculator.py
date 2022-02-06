#################Creating a calculation
a=int(input("Enter first Number"))
b=int(input("Enter Second Number"))

c=input("Enter What You want to do . Type sum,sub,div,mul")
def sum():
    print(a+b)

def div():
    print(a/b)
def mul():
    print(a*b)

def sub():
    print(a-b)

if c=="sum":
    sum()
elif c=="sub":
    sub()
elif c=="mul":
    mul()
elif c== "div":
    div()
else:
    print("Wrong Input")
