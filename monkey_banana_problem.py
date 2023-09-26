print("Play Monkey banana problem")
monkey=input("Is monkey on the floor?(y/n):")
chair=input("Is chair on the floor?(y/n):")
position=input("Is chair at the center?(y/n):")
if monkey.lower()=='y' and chair.lower()=='y' and position.lower()=='y':
    print("case is possible")
    print('Monkey eats banana')
elif monkey.lower()=='y' and chair.lower()=='y' and position.lower()=='n':
    while True:
        op=input('contionue......?(y/n):')
        if op.lower()=='n':
            print("Chair is at the center")
            print('case is possible')
            print("Monkey eats banana")
            break
        else:
            print("The chair continuous to pull until it reaches the center")
            continue
elif monkey.lower()=='n' and chair.lower()=='n' and position.lower()=='n':
    print("Case is not possible")
    print("monkey can not eat banana ,so monkey is feeling hunger")
elif monkey.lower()=='n' and chair.lower()=='y' and position.lower()=='y':
    print("Case is possible")
    print("monkey eats banana")
else:
    print("Invalid options")