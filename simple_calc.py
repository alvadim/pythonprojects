print("Hello! I'm a Calc.\nLet's play!")
while True:
    x=input("Give me a num: ")
    while not x.isdigit():
        print("Just numbers please: ")    
        x=input()
    y=input("Now give me a second num: ")
    while not y.isdigit():
        print("Not a letters, only number: ")    
        y=input()
    oper=input("For addition press A  \nFor substraction press S  ")
    if oper.lower() == "a":
        a=float(x)+float(y)
        print(x, "+", y, "=", a)
    else:
        s=float(x)-float(y)
        print(x, "-", y, "=", s)
    q=input("To continue press C , to exit press X.")
    if q.lower() == "x":
        print("Bye!")
        break

