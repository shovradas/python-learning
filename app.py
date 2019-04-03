while True:
    print('\r\n---------------')
    print('Welcome')
    print('1. View')
    print('2. Add')
    print('3. Clear')
    print('4. Exit')
    print('---------------')
    choice = input("Enter Choice: ")
    print('---------------')

    if choice=='1':
        f = open('contacts.txt', 'r')
        print(f.read())
        f.close()

    elif choice=='2':
        name = input("Enter Name: ")
        number = input("Enter Number: ")

        f = open('contacts.txt', 'a')
        f.write('%s %s\r\n' % (name, number))
        f.close()

    elif choice=='3':    
        f = open('contacts.txt', 'w')
        f.write('')
        f.close()

    elif choice=='4':    
        break