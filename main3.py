try:
    num=int(input("enter a number: "))
    if num>=18:
        print("seccess")
    else:
        print("denied")
except ValueError as ex:
    print(f"Error: {ex}, please enter an integer i.e(1,2,3,...")
