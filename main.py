try:
    num=int(input("enter a number: "))
    print(f"number entered is: {num}")
except ValueError as ex:
    print(f"Error: {ex}, please enter an integer i.e(1,2,3,...)")