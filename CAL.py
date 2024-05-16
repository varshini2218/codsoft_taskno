def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def module(x,y):
    return x%y

print("select the operation to be performed :")

print("1> ADD")
print("2> SUBTRACT")
print("3> MULTIPLY")
print("4> DIVIDE")
print("5> MODULE")

choice=input("please enter your choice:")
num1=int(input("please enter the first number:"))
num2=int(input("please enter the second number:" ))
if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2))
elif choice=='5':
    print(num1,"%",num2,"=",module(num1%num2))
else:
    print("the given input is invalid!!")