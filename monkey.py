monkey = input("Is Monkey On the Floor?(y/n): ")
chair = input("Is Chair On the Floor?(y/n): ")
position = input("Is Chair On the Center?(y/n): ")
if monkey.lower() == 'y' and chair.lower() == 'y' and position.lower() == 'y':
    print("------------------------------------------------------")
    print("Case is Possible!")
    print("Monkey Eats banana.")
elif monkey.lower() == 'y' and chair.lower() == 'y' and position.lower():
    while 1:
        print("\nMonkey Dragged the Chair...")
        op = input("Continue..?(y/n): ")
        if op.lower() == 'n':
            print("------------------------------------------------------")

            print("Chair is at the Center..")
            print('case is Possible.')
            print("Monkey Eats banana.")
            break
        else:
            print("\nThe Chair continues to pull until it reaches the Center..")
            continue
elif monkey.lower() == 'n' and chair.lower() == 'y' and position.lower() == 'y':
    print("Case is Possible!")
    print("Monkey eats Banana./")
elif monkey.lower() == 'n' or chair.lower() == 'n':
    print("Case is Not Possible!")
else:
    print("Invalid Option.")
