while True:
    n1=int(input("Enter a number: "))
    n2=int(input("Enter another number: "))
    op=input("Choose your operation: +,-,*,/ ")

    if op == "+":
        Result=n1+n2
    elif op == "-":
        Result=n1-n2
    elif op == "*":
        Result=n1*n2
    elif op == "/":
        Result=n1/n2
    else:
        print("Wrong choice")
    print("Result is: ",Result)
    
    answer=input("Do you want to continue? Y/N")
    if answer == "N":
        print("Have a good day!")
        break
    else:
        continue
    
