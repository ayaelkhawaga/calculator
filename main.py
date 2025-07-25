first_num=int(input("enter first number"))
operator=input("enter operator you like (+,-,*,/)")
second_number=int(input("enter second number"))
if (operator=="-"):
    result=first_num - second_number 
    print("the result is", result)
elif(operator=="/"):
    result=first_num / second_number
    print("the result is", result)