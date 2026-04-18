try:
    num,num2=eval(input("enter 2 numbers seperated by commas: "))
    result=num/num2
    print(result)
except ZeroDivisionError as ex:
    print(f"Math error!!: {ex}")
except SyntaxError as ex:
    print(f"Please put a comma: ")
except ValueError as ex:
    print(f"Error: {ex}, please enter an integer i.e(1,2,3,...)")