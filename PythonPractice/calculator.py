def add(a, b):
    res = a+b
    return res


def sub(a, b):
    res = a-b
    return res


def mul(a, b):
    res = a*b
    return res


def div(a, b):
    res = b/a
    return res


def mod(a, b):
    res = a%b
    return res


def exp(a, b):
    res = a**b
    return res


def floor(a, b):
    res = a//b
    return res

#dictionary
calculator = {
    1: add,
    2: sub,
    3: mul,
    4: div,
    5: mod,
    6: exp,
    7: floor
}

ans = " "   #it can be (1 to 9 or " " ->True values) and (False or 0 ->False)
while ans:
    print("""    
    1.Addition 
    2.Subtraction
    3.Multiplication
    4.Division
    5.Modulus
    6.Exponential
    7.Floor
    """)
    # """ -> These are used for Documenetation when you want to print multiple line string
    choice = int(input("Enter your choice : "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number:"))
    #ans datatype may be string or function here,it is changed
    ans = calculator.get(choice, "Invalid Choice")  #used to return key,if key doesn't exist,then print 2nd parameter
    #type is used to check the datatype
    if type(ans) != str:          #if Data Type is not equal to String,then it will call function(callback function)
        print(ans(num1, num2))
    else:
        print(ans)
